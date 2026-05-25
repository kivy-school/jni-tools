from typing import Any, ClassVar, overload

class BiometricManager:
    BIOMETRIC_ERROR_HW_UNAVAILABLE: ClassVar[int]
    BIOMETRIC_ERROR_NONE_ENROLLED: ClassVar[int]
    BIOMETRIC_ERROR_NO_HARDWARE: ClassVar[int]
    BIOMETRIC_ERROR_SECURITY_UPDATE_REQUIRED: ClassVar[int]
    BIOMETRIC_NO_AUTHENTICATION: ClassVar[int]
    BIOMETRIC_SUCCESS: ClassVar[int]
    @overload
    def canAuthenticate(self, p0: int) -> int: ...
    @overload
    def canAuthenticate(self) -> int: ...
    def getStrings(self, p0: int) -> Any: ...
    def getLastAuthenticationTime(self, p0: int) -> int: ...

    class Strings:
        def getButtonLabel(self) -> str: ...
        def getPromptMessage(self) -> str: ...
        def getSettingName(self) -> str: ...

    class Authenticators:
        BIOMETRIC_STRONG: ClassVar[int]
        BIOMETRIC_WEAK: ClassVar[int]
        DEVICE_CREDENTIAL: ClassVar[int]
