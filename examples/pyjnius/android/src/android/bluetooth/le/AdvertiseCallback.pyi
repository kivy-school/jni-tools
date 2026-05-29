from typing import Any, ClassVar, overload
from android.bluetooth.le.AdvertiseSettings import AdvertiseSettings

class AdvertiseCallback:
    ADVERTISE_FAILED_ALREADY_STARTED: ClassVar[int]
    ADVERTISE_FAILED_DATA_TOO_LARGE: ClassVar[int]
    ADVERTISE_FAILED_FEATURE_UNSUPPORTED: ClassVar[int]
    ADVERTISE_FAILED_INTERNAL_ERROR: ClassVar[int]
    ADVERTISE_FAILED_TOO_MANY_ADVERTISERS: ClassVar[int]
    def __init__(self) -> None: ...
    def onStartSuccess(self, arg0: AdvertiseSettings) -> None: ...
    def onStartFailure(self, arg0: int) -> None: ...
