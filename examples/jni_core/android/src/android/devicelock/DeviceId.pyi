from typing import Any, ClassVar, overload

class DeviceId:
    DEVICE_ID_TYPE_IMEI: ClassVar[int]
    DEVICE_ID_TYPE_MEID: ClassVar[int]
    def getId(self) -> str: ...
    def getType(self) -> int: ...
