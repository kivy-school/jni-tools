from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FileAlreadyExistsException"]

class FileAlreadyExistsException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/FileAlreadyExistsException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False)]