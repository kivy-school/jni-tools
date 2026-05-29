from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InvalidAlgorithmParameterException"]

class InvalidAlgorithmParameterException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/InvalidAlgorithmParameterException"
    __javaconstructor__ = [("(Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;)V", False), ("()V", False)]