from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ArrayIndexOutOfBoundsException"]

class ArrayIndexOutOfBoundsException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/ArrayIndexOutOfBoundsException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False), ("(I)V", False)]