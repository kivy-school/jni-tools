from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BidirectionalStream"]

class BidirectionalStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/http/BidirectionalStream"
    __javaconstructor__ = [("()V", False)]
    STREAM_PRIORITY_HIGHEST = JavaStaticField("I")
    STREAM_PRIORITY_IDLE = JavaStaticField("I")
    STREAM_PRIORITY_LOW = JavaStaticField("I")
    STREAM_PRIORITY_LOWEST = JavaStaticField("I")
    STREAM_PRIORITY_MEDIUM = JavaStaticField("I")
    hasTrafficStatsUid = JavaMethod("()Z")
    hasTrafficStatsTag = JavaMethod("()Z")
    getTrafficStatsUid = JavaMethod("()I")
    getTrafficStatsTag = JavaMethod("()I")
    getHttpMethod = JavaMethod("()Ljava/lang/String;")
    isDelayRequestHeadersUntilFirstFlushEnabled = JavaMethod("()Z")
    getHeaders = JavaMethod("()Landroid/net/http/HeaderBlock;")
    flush = JavaMethod("()V")
    start = JavaMethod("()V")
    getPriority = JavaMethod("()I")
    isDone = JavaMethod("()Z")
    cancel = JavaMethod("()V")
    write = JavaMethod("(Ljava/nio/ByteBuffer;Z)V")
    read = JavaMethod("(Ljava/nio/ByteBuffer;)V")

    class Callback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/http/BidirectionalStream$Callback"
        onFailed = JavaMethod("(Landroid/net/http/BidirectionalStream;Landroid/net/http/UrlResponseInfo;Landroid/net/http/HttpException;)V")
        onSucceeded = JavaMethod("(Landroid/net/http/BidirectionalStream;Landroid/net/http/UrlResponseInfo;)V")
        onReadCompleted = JavaMethod("(Landroid/net/http/BidirectionalStream;Landroid/net/http/UrlResponseInfo;Ljava/nio/ByteBuffer;Z)V")
        onStreamReady = JavaMethod("(Landroid/net/http/BidirectionalStream;)V")
        onResponseHeadersReceived = JavaMethod("(Landroid/net/http/BidirectionalStream;Landroid/net/http/UrlResponseInfo;)V")
        onResponseTrailersReceived = JavaMethod("(Landroid/net/http/BidirectionalStream;Landroid/net/http/UrlResponseInfo;Landroid/net/http/HeaderBlock;)V")
        onWriteCompleted = JavaMethod("(Landroid/net/http/BidirectionalStream;Landroid/net/http/UrlResponseInfo;Ljava/nio/ByteBuffer;Z)V")
        onCanceled = JavaMethod("(Landroid/net/http/BidirectionalStream;Landroid/net/http/UrlResponseInfo;)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/http/BidirectionalStream$Builder"
        __javaconstructor__ = [("()V", False)]
        addHeader = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Landroid/net/http/BidirectionalStream$Builder;")
        setDelayRequestHeadersUntilFirstFlushEnabled = JavaMethod("(Z)Landroid/net/http/BidirectionalStream$Builder;")
        setHttpMethod = JavaMethod("(Ljava/lang/String;)Landroid/net/http/BidirectionalStream$Builder;")
        setTrafficStatsTag = JavaMethod("(I)Landroid/net/http/BidirectionalStream$Builder;")
        setTrafficStatsUid = JavaMethod("(I)Landroid/net/http/BidirectionalStream$Builder;")
        setPriority = JavaMethod("(I)Landroid/net/http/BidirectionalStream$Builder;")
        build = JavaMethod("()Landroid/net/http/BidirectionalStream;")