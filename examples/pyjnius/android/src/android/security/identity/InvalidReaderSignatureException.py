from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InvalidReaderSignatureException"]

class InvalidReaderSignatureException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/identity/InvalidReaderSignatureException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False)]