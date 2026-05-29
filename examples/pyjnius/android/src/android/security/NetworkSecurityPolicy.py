from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NetworkSecurityPolicy"]

class NetworkSecurityPolicy(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/NetworkSecurityPolicy"
    isCertificateTransparencyVerificationRequired = JavaMethod("(Ljava/lang/String;)Z")
    isCleartextTrafficPermitted = JavaMultipleMethod([("()Z", False, False), ("(Ljava/lang/String;)Z", False, False)])
    getInstance = JavaStaticMethod("()Landroid/security/NetworkSecurityPolicy;")