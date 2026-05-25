from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AuthenticationKeyMetadata"]

class AuthenticationKeyMetadata(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/identity/AuthenticationKeyMetadata"
    getUsageCount = JavaMethod("()I")
    getExpirationDate = JavaMethod("()Ljava/time/Instant;")