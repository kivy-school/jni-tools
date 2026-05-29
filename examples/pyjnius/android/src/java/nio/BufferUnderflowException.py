from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BufferUnderflowException"]

class BufferUnderflowException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/BufferUnderflowException"
    __javaconstructor__ = [("()V", False)]