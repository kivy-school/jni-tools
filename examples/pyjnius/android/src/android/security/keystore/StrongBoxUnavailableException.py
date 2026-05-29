from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StrongBoxUnavailableException"]

class StrongBoxUnavailableException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/keystore/StrongBoxUnavailableException"
    __javaconstructor__ = [("(Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;)V", False), ("()V", False)]