from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NetworkSecurityPolicy"]

class NetworkSecurityPolicy(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/NetworkSecurityPolicy"
    getInstance = JavaStaticMethod("()Landroid/security/NetworkSecurityPolicy;")
    isCleartextTrafficPermitted = JavaMultipleMethod([("()Z", False, False), ("(Ljava/lang/String;)Z", False, False)])