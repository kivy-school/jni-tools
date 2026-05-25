from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FileSystemException"]

class FileSystemException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/FileSystemException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False)]
    getFile = JavaMethod("()Ljava/lang/String;")
    getOtherFile = JavaMethod("()Ljava/lang/String;")
    getReason = JavaMethod("()Ljava/lang/String;")
    getMessage = JavaMethod("()Ljava/lang/String;")