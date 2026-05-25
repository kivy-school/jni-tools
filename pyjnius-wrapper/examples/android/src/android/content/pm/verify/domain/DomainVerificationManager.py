from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DomainVerificationManager"]

class DomainVerificationManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/pm/verify/domain/DomainVerificationManager"
    getDomainVerificationUserState = JavaMethod("(Ljava/lang/String;)Landroid/content/pm/verify/domain/DomainVerificationUserState;")