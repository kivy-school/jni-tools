from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StrongBoxUnavailableException"]

class StrongBoxUnavailableException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/keystore/StrongBoxUnavailableException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/Throwable;)V", False)]