from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UncheckedIOException"]

class UncheckedIOException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/UncheckedIOException"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/io/IOException;)V", False), ("(Ljava/io/IOException;)V", False)]
    getCause = JavaMethod("()Ljava/io/IOException;")