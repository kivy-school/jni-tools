from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BufferOverflowException"]

class BufferOverflowException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/BufferOverflowException"
    __javaconstructor__ = [("()V", False)]