from typing import Any, ClassVar, overload

class Config:
    DEBUG: ClassVar[bool]
    LOGD: ClassVar[bool]
    LOGV: ClassVar[bool]
    PROFILE: ClassVar[bool]
    RELEASE: ClassVar[bool]
