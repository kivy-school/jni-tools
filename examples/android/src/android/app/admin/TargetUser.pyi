from typing import Any, ClassVar, overload

class TargetUser:
    GLOBAL: ClassVar["TargetUser"]
    LOCAL_USER: ClassVar["TargetUser"]
    PARENT_USER: ClassVar["TargetUser"]
    UNKNOWN_USER: ClassVar["TargetUser"]
    def equals(self, arg0: Any) -> bool: ...
    def hashCode(self) -> int: ...
