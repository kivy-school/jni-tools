from typing import Any, ClassVar, overload

class DevicePolicyIdentifiers:
    ACCOUNT_MANAGEMENT_DISABLED_POLICY: ClassVar[str]
    APPLICATION_HIDDEN_POLICY: ClassVar[str]
    APPLICATION_RESTRICTIONS_POLICY: ClassVar[str]
    AUTO_TIMEZONE_POLICY: ClassVar[str]
    AUTO_TIME_POLICY: ClassVar[str]
    BACKUP_SERVICE_POLICY: ClassVar[str]
    CAMERA_DISABLED_POLICY: ClassVar[str]
    CONTENT_PROTECTION_POLICY: ClassVar[str]
    KEYGUARD_DISABLED_FEATURES_POLICY: ClassVar[str]
    LOCK_TASK_POLICY: ClassVar[str]
    PACKAGES_SUSPENDED_POLICY: ClassVar[str]
    PACKAGE_UNINSTALL_BLOCKED_POLICY: ClassVar[str]
    PASSWORD_COMPLEXITY_POLICY: ClassVar[str]
    PERMISSION_GRANT_POLICY: ClassVar[str]
    PERSISTENT_PREFERRED_ACTIVITY_POLICY: ClassVar[str]
    RESET_PASSWORD_TOKEN_POLICY: ClassVar[str]
    SECURITY_LOGGING_POLICY: ClassVar[str]
    STATUS_BAR_DISABLED_POLICY: ClassVar[str]
    USB_DATA_SIGNALING_POLICY: ClassVar[str]
    USER_CONTROL_DISABLED_PACKAGES_POLICY: ClassVar[str]
    @staticmethod
    def getIdentifierForUserRestriction(p0: str) -> str: ...
