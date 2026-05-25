from typing import Any, ClassVar, overload

class MmTelFeature:

    class MmTelCapabilities:
        CAPABILITY_TYPE_CALL_COMPOSER: ClassVar[int]
        CAPABILITY_TYPE_CALL_COMPOSER_BUSINESS_ONLY: ClassVar[int]
        CAPABILITY_TYPE_SMS: ClassVar[int]
        CAPABILITY_TYPE_UT: ClassVar[int]
        CAPABILITY_TYPE_VIDEO: ClassVar[int]
        CAPABILITY_TYPE_VOICE: ClassVar[int]
        def isCapable(self, arg0: int) -> bool: ...
        def toString(self) -> str: ...
        def hashCode(self) -> int: ...
        def equals(self, arg0: Any) -> bool: ...
