from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SecurityStateManager"]

class SecurityStateManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/SecurityStateManager"
    KEY_KERNEL_VERSION = JavaStaticField("Ljava/lang/String;")
    KEY_SYSTEM_SPL = JavaStaticField("Ljava/lang/String;")
    KEY_VENDOR_SPL = JavaStaticField("Ljava/lang/String;")
    getGlobalSecurityState = JavaMethod("()Landroid/os/Bundle;")