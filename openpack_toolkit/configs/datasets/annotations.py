from .._schema import AnnotConfig
from ...activity import ActSet, ActClass

OPENPACK_OPERATIONS = ActSet((
    ActClass(100, "Picking", is_ignore=False),
    ActClass(200, "RelocateItemLabel", is_ignore=False),
    ActClass(300, "AssembleBox", is_ignore=False),
    ActClass(400, "InsertItems", is_ignore=False),
    ActClass(500, "CloseBox", is_ignore=False),
    ActClass(600, "AttachBoxLabel", is_ignore=False),
    ActClass(700, "ScanLabel", is_ignore=False),
    ActClass(800, "AttachShippingLabel", is_ignore=False),
    ActClass(900, "PutOnRack", is_ignore=False),
    ActClass(1000, "Fill-outOrder", is_ignore=False),
    ActClass(8100, "Null", is_ignore=True),
))

OPENPACK_OPERATIONS_ANNOTATION = AnnotConfig(
    name="openpack-operations",
    version="v3.2.1",
    path={
        "dir": "${path.openpack.rootdir}/${user.name}/annotation/${..name}",
        "fname": "${session}.csv",
    },
    classes=OPENPACK_OPERATIONS,
)


OPENPACK_ACTIONS = ActSet((
    ActClass(101, "PickUp-Sheet", is_ignore=False),
    ActClass(102, "Walk-ToRack", is_ignore=False),
    ActClass(103, "PickUp-Item-FromBox", is_ignore=False),
    ActClass(104, "Pick-UpOrderSheet&Walk-ToRack-v2", is_ignore=False),
    ActClass(105, "Walk-ToWorkBench-v2", is_ignore=False),
    ActClass(106, "Pick-UpOrderSheet&Walk-ToRack-with-PrevPackedBox-v2", is_ignore=False),
    ActClass(107, "PickUp-BoxSheet", is_ignore=False),
    ActClass(108, "Walk-ToWorkBench", is_ignore=False),
    ActClass(201, "Remove-ItemLabel", is_ignore=False),
    ActClass(202, "AttachTo-OrderSheet", is_ignore=False),
    ActClass(203, "Hold-Pen", is_ignore=False),
    ActClass(204, "Write-CheckMark", is_ignore=False),
    ActClass(205, "Put-Item-SmallBag", is_ignore=False),
    ActClass(206, "Relocate-ItemLabel-v2", is_ignore=False),
    ActClass(207, "Write-v2", is_ignore=False),
    ActClass(301, "Pick-Cardboard", is_ignore=False),
    ActClass(302, "Bend-Flap", is_ignore=False),
    ActClass(303, "Attach-Tape", is_ignore=False),
    ActClass(304, "TurnOver-Box", is_ignore=False),
    ActClass(305, "PickUp-AssembledBox", is_ignore=False),
    ActClass(306, "AssembleBox-v2", is_ignore=False),
    ActClass(401, "Insert-Item-into-Box", is_ignore=False),
    ActClass(402, "AirCushion", is_ignore=False),
    ActClass(403, "Separate-AirCushion", is_ignore=False),
    ActClass(404, "Put-Item-SmallBag", is_ignore=False),
    ActClass(405, "Insert-Items-v2", is_ignore=False),
    ActClass(501, "Bend-Flap", is_ignore=False),
    ActClass(502, "Attach-Tape", is_ignore=False),
    ActClass(503, "CloseBox-v2", is_ignore=False),
    ActClass(601, "Attach-BoxLabel", is_ignore=False),
    ActClass(602, "Attach-BoxLabel-v2", is_ignore=False),
    ActClass(701, "PickUp-HT", is_ignore=False),
    ActClass(702, "Scan-OrderSheet", is_ignore=False),
    ActClass(703, "Scan-Box", is_ignore=False),
    ActClass(704, "Scan-Item", is_ignore=False),
    ActClass(705, "Hold-Scanner", is_ignore=False),
    ActClass(706, "Scan-OrderSheet", is_ignore=False),
    ActClass(707, "Scan-Printer", is_ignore=False),
    ActClass(708, "HT-v2", is_ignore=False),
    ActClass(709, "Printer-v2", is_ignore=False),
    ActClass(801, "PickUp-ShippingLabel", is_ignore=False),
    ActClass(802, "Attach-ShippingLabel", is_ignore=False),
    ActClass(802, "Attach-ShippingLabel-v2", is_ignore=False),
    ActClass(901, "PickUp-PackedBox", is_ignore=False),
    ActClass(902, "Put-PackedBox", is_ignore=False),
    ActClass(903, "Put-OnPack-v2", is_ignore=False),
    ActClass(1001, "PickUp-Pen", is_ignore=False),
    ActClass(1002, "Write-Sign", is_ignore=False),
    ActClass(1003, "Push-OrderSheet-IntoTray", is_ignore=False),
    ActClass(1004, "FillOut-v2", is_ignore=False),
    ActClass(1005, "Write-v2", is_ignore=False),
    ActClass(1006, "Insert-v2", is_ignore=False),
    ActClass(8101, "Others", is_ignore=True),
    ActClass(8102, "SystemError", is_ignore=True),
    ActClass(8103, "Ignore", is_ignore=True),
    ActClass(8104, "Unknown", is_ignore=True),
    ActClass(8201, "SystemError", is_ignore=True),
))

OPENPACK_ACTIONS_ANNOTATION = AnnotConfig(
    name="openpack-actions",
    version="v3.2.1",
    path={
        "dir": "${path.openpack.rootdir}/${user.name}/annotation/${..name}",
        "fname": "${session}.csv",
    },
    classes=OPENPACK_ACTIONS,
)
