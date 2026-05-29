from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DirectoryIteratorException"]

class DirectoryIteratorException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/DirectoryIteratorException"
    __javaconstructor__ = [("(Ljava/io/IOException;)V", False)]
    getCause = JavaMultipleMethod([("()Ljava/lang/Throwable;", False, False), ("()Ljava/io/IOException;", False, False)])