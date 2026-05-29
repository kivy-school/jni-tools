from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ClosedDirectoryStreamException"]

class ClosedDirectoryStreamException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/ClosedDirectoryStreamException"
    __javaconstructor__ = [("()V", False)]