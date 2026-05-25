from typing import Any, ClassVar, overload

class OnObbStateChangeListener:
    ERROR_ALREADY_MOUNTED: ClassVar[int]
    ERROR_COULD_NOT_MOUNT: ClassVar[int]
    ERROR_COULD_NOT_UNMOUNT: ClassVar[int]
    ERROR_INTERNAL: ClassVar[int]
    ERROR_NOT_MOUNTED: ClassVar[int]
    ERROR_PERMISSION_DENIED: ClassVar[int]
    MOUNTED: ClassVar[int]
    UNMOUNTED: ClassVar[int]
    def __init__(self) -> None: ...
    def onObbStateChange(self, arg0: str, arg1: int) -> None: ...
