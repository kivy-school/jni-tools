from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InvalidAlgorithmParameterException"]

class InvalidAlgorithmParameterException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/InvalidAlgorithmParameterException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/Throwable;)V", False)]