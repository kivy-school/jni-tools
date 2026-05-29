from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UncheckedIOException"]

class UncheckedIOException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/UncheckedIOException"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/io/IOException;)V", False), ("(Ljava/io/IOException;)V", False)]
    getCause = JavaMultipleMethod([("()Ljava/lang/Throwable;", False, False), ("()Ljava/io/IOException;", False, False)])