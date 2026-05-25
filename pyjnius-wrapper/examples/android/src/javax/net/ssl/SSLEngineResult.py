from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SSLEngineResult"]

class SSLEngineResult(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/SSLEngineResult"
    __javaconstructor__ = [("(Ljavax/net/ssl/SSLEngineResult$Status;Ljavax/net/ssl/SSLEngineResult$HandshakeStatus;II)V", False)]
    getStatus = JavaMethod("()Ljavax/net/ssl/SSLEngineResult$Status;")
    getHandshakeStatus = JavaMethod("()Ljavax/net/ssl/SSLEngineResult$HandshakeStatus;")
    bytesConsumed = JavaMethod("()I")
    bytesProduced = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")

    class HandshakeStatus(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "javax/net/ssl/SSLEngineResult/HandshakeStatus"
        values = JavaStaticMethod("()[Ljavax/net/ssl/SSLEngineResult$HandshakeStatus;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljavax/net/ssl/SSLEngineResult$HandshakeStatus;")
        NOT_HANDSHAKING = JavaStaticField("Ljavax/net/ssl/SSLEngineResult/HandshakeStatus;")
        FINISHED = JavaStaticField("Ljavax/net/ssl/SSLEngineResult/HandshakeStatus;")
        NEED_TASK = JavaStaticField("Ljavax/net/ssl/SSLEngineResult/HandshakeStatus;")
        NEED_WRAP = JavaStaticField("Ljavax/net/ssl/SSLEngineResult/HandshakeStatus;")
        NEED_UNWRAP = JavaStaticField("Ljavax/net/ssl/SSLEngineResult/HandshakeStatus;")

    class Status(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "javax/net/ssl/SSLEngineResult/Status"
        values = JavaStaticMethod("()[Ljavax/net/ssl/SSLEngineResult$Status;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljavax/net/ssl/SSLEngineResult$Status;")
        BUFFER_UNDERFLOW = JavaStaticField("Ljavax/net/ssl/SSLEngineResult/Status;")
        BUFFER_OVERFLOW = JavaStaticField("Ljavax/net/ssl/SSLEngineResult/Status;")
        OK = JavaStaticField("Ljavax/net/ssl/SSLEngineResult/Status;")
        CLOSED = JavaStaticField("Ljavax/net/ssl/SSLEngineResult/Status;")