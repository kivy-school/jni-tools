from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ReadOnlyFileSystemException"]

class ReadOnlyFileSystemException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/ReadOnlyFileSystemException"
    __javaconstructor__ = [("()V", False)]