from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IllegalBlockSizeException"]

class IllegalBlockSizeException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/IllegalBlockSizeException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]