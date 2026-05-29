from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FileSystemNotFoundException"]

class FileSystemNotFoundException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/FileSystemNotFoundException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]