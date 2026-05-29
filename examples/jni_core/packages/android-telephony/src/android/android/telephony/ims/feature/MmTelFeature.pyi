from typing import Any, ClassVar, overload

class MmTelFeature:

    class MmTelCapabilities:
        CAPABILITY_TYPE_CALL_COMPOSER: ClassVar[int]
        CAPABILITY_TYPE_CALL_COMPOSER_BUSINESS_ONLY: ClassVar[int]
        CAPABILITY_TYPE_SMS: ClassVar[int]
        CAPABILITY_TYPE_UT: ClassVar[int]
        CAPABILITY_TYPE_VIDEO: ClassVar[int]
        CAPABILITY_TYPE_VOICE: ClassVar[int]
        def isCapable(self, p0: int) -> bool: ...
        def equals(self, p0: Any) -> bool: ...
        def toString(self) -> str: ...
        def hashCode(self) -> int: ...
