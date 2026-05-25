from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IkeIOException"]

class IkeIOException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/exceptions/IkeIOException"
    __javaconstructor__ = [("(Ljava/io/IOException;)V", False)]
    getCause = JavaMethod("()Ljava/io/IOException;")
    initCause = JavaMethod("(Ljava/lang/Throwable;)Ljava/lang/Throwable;")