from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ClosedFileSystemException"]

class ClosedFileSystemException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/ClosedFileSystemException"
    __javaconstructor__ = [("()V", False)]