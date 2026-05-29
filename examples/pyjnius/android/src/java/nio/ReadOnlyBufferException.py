from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ReadOnlyBufferException"]

class ReadOnlyBufferException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/ReadOnlyBufferException"
    __javaconstructor__ = [("()V", False)]