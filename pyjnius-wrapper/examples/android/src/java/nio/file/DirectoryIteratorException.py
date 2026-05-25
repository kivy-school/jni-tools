from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DirectoryIteratorException"]

class DirectoryIteratorException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/DirectoryIteratorException"
    __javaconstructor__ = [("(Ljava/io/IOException;)V", False)]
    getCause = JavaMethod("()Ljava/io/IOException;")