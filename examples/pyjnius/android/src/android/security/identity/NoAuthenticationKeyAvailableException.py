from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NoAuthenticationKeyAvailableException"]

class NoAuthenticationKeyAvailableException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/identity/NoAuthenticationKeyAvailableException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False)]