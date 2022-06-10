from ...activity import ActClass, ActSet
from .._schema import AnnotConfig

OPENPACK_OPERATIONS = ActSet((
    ActClass(100, "Picking"),
    ActClass(200, "MoveItemLabel"),
    ActClass(300, "AssembleBox"),
    ActClass(400, "PackInBox"),
    ActClass(500, "CloseBox"),
    ActClass(600, "AttachLabel"),
    ActClass(700, "ReadLabel"),
    ActClass(900, "PutOnCartRack"),
    ActClass(1000, "Pen"),
    ActClass(8000, "Others"),
))

OPENPACK_OPERATIONS_ANNOTATION = AnnotConfig(
    name="openpack-operations",
    version="v3.0.1",
    classes=OPENPACK_OPERATIONS,
)


OPENPACK_ACTIONS = ActSet((
    ActClass(101, "PickUp-OrderSheet"),
    ActClass(102, "GoTo-Cart"),
    ActClass(103, "PickUp-Item"),
    ActClass(104, "BackTo-Table"),
    ActClass(105, "Put-Items"),
    ActClass(106, "PickUp-PackedBox"),
    ActClass(107, "Put-PackedBox"),
    ActClass(108, "PickUp-Item-FromBox"),
    ActClass(201, "Remove-ItemLabel"),
    ActClass(202, "AttachTo-OrderSheet"),
    ActClass(203, "Hold-Pen"),
    ActClass(204, "Write-CheckMark"),
    ActClass(205, "Put/Release-Pen"),
    ActClass(206, "Put-Iten-SmallBack"),
    ActClass(301, "Pick-Cardboard"),
    ActClass(302, "Assemble-Box"),
    ActClass(303, "Attach-Tape"),
    ActClass(304, "TurnOver-Box"),
    ActClass(305, "PickUp-PremadeBox"),
    ActClass(401, "Put-Item-into-Box"),
    ActClass(402, "Lift-Item"),
    ActClass(403, "Put-Item"),
    ActClass(404, "Pick-AirCushion"),
    ActClass(405, "Separate-AirCushion"),
    ActClass(406, "Put-AirCushion"),
    ActClass(407, "Put-Item-SmallBack"),
    ActClass(501, "Bend-Flap"),
    ActClass(502, "Attach-Tape"),
    ActClass(601, "Pick-BoxLabel"),
    ActClass(602, "PickUp-BoxLabel"),
    ActClass(603, "Attach-BoxLabel"),
    ActClass(701, "PickUp-HT"),
    ActClass(702, "Scan-OrderSheet"),
    ActClass(703, "Scan-Box"),
    ActClass(704, "Scan-Item"),
    ActClass(705, "Push-Button"),
    ActClass(706, "Release-HT"),
    ActClass(707, "Hold-Scanner"),
    ActClass(708, "Scan-OrderSheet2"),
    ActClass(709, "Scan-Printer"),
    ActClass(710, "Release-Scanner"),
    ActClass(801, "PickUp-ShippingLabel"),
    ActClass(802, "Remove-ShippingLabel"),
    ActClass(803, "Attach-ShippingLabel"),
    ActClass(901, "PickUp-PackedBox"),
    ActClass(902, "GoTo-Cart"),
    ActClass(903, "Put-PackedBox"),
    ActClass(904, "Goto-Table"),
    ActClass(1001, "PickUp-Pen"),
    ActClass(1002, "Write-Sign"),
    ActClass(1003, "Release-Pen"),
    ActClass(1004, "PickUp-OrderSheet"),
    ActClass(1005, "Push-OrderSheet-IntoTray"),
))

OPENPACK_ACTIONS_ANNOTATION = AnnotConfig(
    name="openpack-actions",
    version="v3.0.1",
    classes=OPENPACK_ACTIONS,
)
