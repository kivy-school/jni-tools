from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HttpConnectionParams"]

class HttpConnectionParams(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/apache/http/params/HttpConnectionParams"
    getSoTimeout = JavaStaticMethod("(Lorg/apache/http/params/HttpParams;)I")
    setSoTimeout = JavaStaticMethod("(Lorg/apache/http/params/HttpParams;I)V")
    getTcpNoDelay = JavaStaticMethod("(Lorg/apache/http/params/HttpParams;)Z")
    setTcpNoDelay = JavaStaticMethod("(Lorg/apache/http/params/HttpParams;Z)V")
    getSocketBufferSize = JavaStaticMethod("(Lorg/apache/http/params/HttpParams;)I")
    setSocketBufferSize = JavaStaticMethod("(Lorg/apache/http/params/HttpParams;I)V")
    getLinger = JavaStaticMethod("(Lorg/apache/http/params/HttpParams;)I")
    setLinger = JavaStaticMethod("(Lorg/apache/http/params/HttpParams;I)V")
    getConnectionTimeout = JavaStaticMethod("(Lorg/apache/http/params/HttpParams;)I")
    setConnectionTimeout = JavaStaticMethod("(Lorg/apache/http/params/HttpParams;I)V")
    isStaleCheckingEnabled = JavaStaticMethod("(Lorg/apache/http/params/HttpParams;)Z")
    setStaleCheckingEnabled = JavaStaticMethod("(Lorg/apache/http/params/HttpParams;Z)V")