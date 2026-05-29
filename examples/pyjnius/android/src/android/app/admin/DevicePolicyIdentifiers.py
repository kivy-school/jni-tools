from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DevicePolicyIdentifiers"]

class DevicePolicyIdentifiers(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/admin/DevicePolicyIdentifiers"
    ACCOUNT_MANAGEMENT_DISABLED_POLICY = JavaStaticField("Ljava/lang/String;")
    APPLICATION_HIDDEN_POLICY = JavaStaticField("Ljava/lang/String;")
    APPLICATION_RESTRICTIONS_POLICY = JavaStaticField("Ljava/lang/String;")
    AUTO_TIMEZONE_POLICY = JavaStaticField("Ljava/lang/String;")
    AUTO_TIME_POLICY = JavaStaticField("Ljava/lang/String;")
    BACKUP_SERVICE_POLICY = JavaStaticField("Ljava/lang/String;")
    CAMERA_DISABLED_POLICY = JavaStaticField("Ljava/lang/String;")
    CONTENT_PROTECTION_POLICY = JavaStaticField("Ljava/lang/String;")
    KEYGUARD_DISABLED_FEATURES_POLICY = JavaStaticField("Ljava/lang/String;")
    LOCK_TASK_POLICY = JavaStaticField("Ljava/lang/String;")
    PACKAGES_SUSPENDED_POLICY = JavaStaticField("Ljava/lang/String;")
    PACKAGE_UNINSTALL_BLOCKED_POLICY = JavaStaticField("Ljava/lang/String;")
    PASSWORD_COMPLEXITY_POLICY = JavaStaticField("Ljava/lang/String;")
    PERMISSION_GRANT_POLICY = JavaStaticField("Ljava/lang/String;")
    PERSISTENT_PREFERRED_ACTIVITY_POLICY = JavaStaticField("Ljava/lang/String;")
    RESET_PASSWORD_TOKEN_POLICY = JavaStaticField("Ljava/lang/String;")
    SECURITY_LOGGING_POLICY = JavaStaticField("Ljava/lang/String;")
    STATUS_BAR_DISABLED_POLICY = JavaStaticField("Ljava/lang/String;")
    USB_DATA_SIGNALING_POLICY = JavaStaticField("Ljava/lang/String;")
    USER_CONTROL_DISABLED_PACKAGES_POLICY = JavaStaticField("Ljava/lang/String;")
    getIdentifierForUserRestriction = JavaStaticMethod("(Ljava/lang/String;)Ljava/lang/String;")