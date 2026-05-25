from typing import Any, ClassVar, overload

class ImsException:
    CODE_ERROR_INVALID_SUBSCRIPTION: ClassVar[int]
    CODE_ERROR_SERVICE_UNAVAILABLE: ClassVar[int]
    CODE_ERROR_UNSPECIFIED: ClassVar[int]
    CODE_ERROR_UNSUPPORTED_OPERATION: ClassVar[int]
    def getCode(self) -> int: ...
