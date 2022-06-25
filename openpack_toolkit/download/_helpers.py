import shutil
import urllib.request
from logging import getLogger
from pathlib import Path
from typing import Dict, List

from omegaconf import OmegaConf

from .. import configs

logger = getLogger(__name__)


def _get_release_config(version: str) -> configs.ReleaseConfig:
    """Returns ReleaseConfig.

    Args:
        version (str): e.g., "v0.2.0".

    Returns:
        DictConfig: _description_
    """
    release_conf_name = f"RELEASE_CONFIG_{version.upper()}".replace(".", "_")
    if hasattr(configs.releases, release_conf_name):
        return getattr(configs.releases, release_conf_name)

    raise ValueError(
        f"release {version} is not found. The version seems not to be supported yet.")


def get_released_zip_file_list(
        release_conf: configs.ReleaseConfig) -> Dict:
    """Return a list of DataStreamConfig names included in the releases.

    Args:
        release_conf (configs.ReleaseConfig): _description_

    Returns:
        List: _description_
    Todo:
        Refactoring is required.
    """
    stream_conf_list = dict()

    for category, data in release_conf.streams.items():
        if "repository" in data.keys():
            # NOTE: depth=1
            repo = data["repository"]

            if "fname" in data.keys():
                data["subdirs"] = [{
                    "fname": data["fname"],
                }]

            # FIXME: update release config
            if category == "atr":
                data["subdirs"] = [{
                    "fname": "atr-qags",
                }]

            for stream in data["subdirs"]:
                # FIXME: updata release config
                if category == "annotation":
                    fname = stream
                else:
                    fname = stream.get("fname", None)
                assert fname is not None

                stream_conf_list[fname] = {
                    "zip": "{user}__" + f"{category}.zip",
                    "repo": repo,
                    "category": category,
                }

        else:
            # NOTE: depth=2
            for subcategory, data2 in data.items():
                if "repository" in data2.keys():
                    repo = data2["repository"]

                    for stream in data2["subdirs"]:
                        fname = stream["fname"]
                        stream_conf_list[fname] = {
                            "zip": "{user}__" +
                            f"{category}__{subcategory}.zip",
                            "repo": repo,
                            "category": f"{category}/{subcategory}"}
    return stream_conf_list


def download_openpack_from_zenodo(
        rootdir: Path,
        streams: List[str] = None,
        version: str = None):
    # NOTE: Check rootdir. If the opnepack directory exists, skip this.
    # If not, create a new directory.
    if isinstance(rootdir, str):
        rootdir = Path(rootdir)
    if not rootdir.exists():
        raise FileNotFoundError(
            f"dataset root directory does not found: {rootdir}")

    release_conf = _get_release_config(version)
    zipped_stream_list = get_released_zip_file_list(release_conf)

    path_conf = OmegaConf.create({
        "openpack": {
            "version": version,
            "rootdir": f"{rootdir}/openpack/{version}",
        }
    })

    openpack_rootdir = Path(path_conf.openpack.rootdir)
    openpack_rootdir.mkdir(exist_ok=True, parents=True)

    for stream_conf_name in streams:
        zip_data = zipped_stream_list.get(stream_conf_name, None)
        if zip_data is None:
            continue

        for user, user_data in release_conf.users.items():
            if user_data.exclude is not None:
                if zip_data["stream_category"] in user_data.exclude:
                    continue

            zip_fname = zip_data["zip"].format(user=user)
            url = f"{release_conf.url}/files/{zip_fname}?download=1"

            download_path = Path(
                openpack_rootdir,
                "zenodo",
                f"{zip_fname}.zip")
            if download_path.exists():
                logger.warning(
                    f"Skip download because the zip file is already exists.: {url}")
                continue
            download_path.parent.mkdir(parents=True, exist_ok=True)

            logger.info(f"download {url}")
            urllib.request.urlretrieve(url, download_path)
            logger.info(f"unzip {download_path}")
            shutil.unpack_archive(download_path, openpack_rootdir)
