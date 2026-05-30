from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class RoleManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/role/RoleManager"
    ROLE_ASSISTANT = JavaStaticField("Ljava/lang/String;")
    ROLE_BROWSER = JavaStaticField("Ljava/lang/String;")
    ROLE_CALL_REDIRECTION = JavaStaticField("Ljava/lang/String;")
    ROLE_CALL_SCREENING = JavaStaticField("Ljava/lang/String;")
    ROLE_DIALER = JavaStaticField("Ljava/lang/String;")
    ROLE_EMERGENCY = JavaStaticField("Ljava/lang/String;")
    ROLE_HOME = JavaStaticField("Ljava/lang/String;")
    ROLE_NOTES = JavaStaticField("Ljava/lang/String;")
    ROLE_SMS = JavaStaticField("Ljava/lang/String;")
    ROLE_WALLET = JavaStaticField("Ljava/lang/String;")
    createRequestRoleIntent = JavaMethod("(Ljava/lang/String;)Landroid/content/Intent;")
    isRoleAvailable = JavaMethod("(Ljava/lang/String;)Z")
    isRoleHeld = JavaMethod("(Ljava/lang/String;)Z")