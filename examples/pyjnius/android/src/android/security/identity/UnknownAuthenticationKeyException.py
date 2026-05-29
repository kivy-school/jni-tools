from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UnknownAuthenticationKeyException"]

class UnknownAuthenticationKeyException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/identity/UnknownAuthenticationKeyException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False)]