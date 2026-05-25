from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FileSystemAlreadyExistsException"]

class FileSystemAlreadyExistsException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/FileSystemAlreadyExistsException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]