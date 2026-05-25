from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NegativeArraySizeException"]

class NegativeArraySizeException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/NegativeArraySizeException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]