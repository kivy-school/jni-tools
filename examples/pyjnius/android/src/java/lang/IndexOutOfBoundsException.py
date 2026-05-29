from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IndexOutOfBoundsException"]

class IndexOutOfBoundsException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/IndexOutOfBoundsException"
    __javaconstructor__ = [("(J)V", False), ("(I)V", False), ("(Ljava/lang/String;)V", False), ("()V", False)]