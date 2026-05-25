from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OutOfMemoryError"]

class OutOfMemoryError(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/OutOfMemoryError"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]