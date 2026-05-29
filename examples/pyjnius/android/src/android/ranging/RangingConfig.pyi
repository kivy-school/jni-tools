from typing import Any, ClassVar, overload

class RangingConfig:
    RANGING_SESSION_OOB: ClassVar[int]
    RANGING_SESSION_RAW: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def toString(self) -> str: ...
    def getRangingSessionType(self) -> int: ...
