from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HttpConnectionParams"]

class HttpConnectionParams(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/apache/http/params/HttpConnectionParams"
    CONNECTION_TIMEOUT = JavaStaticField("Ljava/lang/String;")
    MAX_HEADER_COUNT = JavaStaticField("Ljava/lang/String;")
    MAX_LINE_LENGTH = JavaStaticField("Ljava/lang/String;")
    SOCKET_BUFFER_SIZE = JavaStaticField("Ljava/lang/String;")
    SO_LINGER = JavaStaticField("Ljava/lang/String;")
    SO_TIMEOUT = JavaStaticField("Ljava/lang/String;")
    STALE_CONNECTION_CHECK = JavaStaticField("Ljava/lang/String;")
    TCP_NODELAY = JavaStaticField("Ljava/lang/String;")
    getLinger = JavaStaticMethod("(Lorg/apache/http/params/HttpParams;)I")
    getConnectionTimeout = JavaStaticMethod("(Lorg/apache/http/params/HttpParams;)I")
    getSocketBufferSize = JavaStaticMethod("(Lorg/apache/http/params/HttpParams;)I")
    isStaleCheckingEnabled = JavaStaticMethod("(Lorg/apache/http/params/HttpParams;)Z")
    setConnectionTimeout = JavaStaticMethod("(Lorg/apache/http/params/HttpParams;I)V")
    setLinger = JavaStaticMethod("(Lorg/apache/http/params/HttpParams;I)V")
    setSocketBufferSize = JavaStaticMethod("(Lorg/apache/http/params/HttpParams;I)V")
    setStaleCheckingEnabled = JavaStaticMethod("(Lorg/apache/http/params/HttpParams;Z)V")
    setSoTimeout = JavaStaticMethod("(Lorg/apache/http/params/HttpParams;I)V")
    getSoTimeout = JavaStaticMethod("(Lorg/apache/http/params/HttpParams;)I")
    setTcpNoDelay = JavaStaticMethod("(Lorg/apache/http/params/HttpParams;Z)V")
    getTcpNoDelay = JavaStaticMethod("(Lorg/apache/http/params/HttpParams;)Z")