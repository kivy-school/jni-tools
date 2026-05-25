from typing import Any, ClassVar, overload

class OnDevicePersonalizationException:
    ERROR_ISOLATED_SERVICE_FAILED: ClassVar[int]
    ERROR_PERSONALIZATION_DISABLED: ClassVar[int]
    def getErrorCode(self) -> int: ...
