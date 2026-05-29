from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FileSystemLoopException"]

class FileSystemLoopException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/FileSystemLoopException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]