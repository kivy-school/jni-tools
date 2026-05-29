from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ErrnoException"]

class ErrnoException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/system/ErrnoException"
    __javaconstructor__ = [("(Ljava/lang/String;I)V", False), ("(Ljava/lang/String;ILjava/lang/Throwable;)V", False)]
    errno = JavaField("I")
    rethrowAsSocketException = JavaMethod("()Ljava/net/SocketException;")
    getMessage = JavaMethod("()Ljava/lang/String;")
    rethrowAsIOException = JavaMethod("()Ljava/io/IOException;")