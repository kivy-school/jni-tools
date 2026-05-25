from typing import Any, ClassVar, overload
from android.content.Intent import Intent

class RoleManager:
    ROLE_ASSISTANT: ClassVar[str]
    ROLE_BROWSER: ClassVar[str]
    ROLE_CALL_REDIRECTION: ClassVar[str]
    ROLE_CALL_SCREENING: ClassVar[str]
    ROLE_DIALER: ClassVar[str]
    ROLE_EMERGENCY: ClassVar[str]
    ROLE_HOME: ClassVar[str]
    ROLE_NOTES: ClassVar[str]
    ROLE_SMS: ClassVar[str]
    ROLE_WALLET: ClassVar[str]
    def createRequestRoleIntent(self, p0: str) -> Intent: ...
    def isRoleAvailable(self, p0: str) -> bool: ...
    def isRoleHeld(self, p0: str) -> bool: ...
