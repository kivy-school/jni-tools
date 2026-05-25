from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IndexOutOfBoundsException"]

class IndexOutOfBoundsException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/IndexOutOfBoundsException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False), ("(I)V", False), ("(J)V", False)]