from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IkeIOException"]

class IkeIOException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/exceptions/IkeIOException"
    __javaconstructor__ = [("(Ljava/io/IOException;)V", False)]
    getCause = JavaMultipleMethod([("()Ljava/lang/Throwable;", False, False), ("()Ljava/io/IOException;", False, False)])
    initCause = JavaMethod("(Ljava/lang/Throwable;)Ljava/lang/Throwable;")