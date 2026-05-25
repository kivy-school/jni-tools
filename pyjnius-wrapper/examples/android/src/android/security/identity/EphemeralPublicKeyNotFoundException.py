from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EphemeralPublicKeyNotFoundException"]

class EphemeralPublicKeyNotFoundException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/identity/EphemeralPublicKeyNotFoundException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False)]