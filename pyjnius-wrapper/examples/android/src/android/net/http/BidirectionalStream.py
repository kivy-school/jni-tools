from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BidirectionalStream"]

class BidirectionalStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/http/BidirectionalStream"
    __javaconstructor__ = [("()V", False)]
    STREAM_PRIORITY_HIGHEST = JavaStaticField("I")
    STREAM_PRIORITY_IDLE = JavaStaticField("I")
    STREAM_PRIORITY_LOW = JavaStaticField("I")
    STREAM_PRIORITY_LOWEST = JavaStaticField("I")
    STREAM_PRIORITY_MEDIUM = JavaStaticField("I")
    getHttpMethod = JavaMethod("()Ljava/lang/String;")
    hasTrafficStatsTag = JavaMethod("()Z")
    getTrafficStatsTag = JavaMethod("()I")
    hasTrafficStatsUid = JavaMethod("()Z")
    getTrafficStatsUid = JavaMethod("()I")
    getHeaders = JavaMethod("()Landroid/net/http/HeaderBlock;")
    getPriority = JavaMethod("()I")
    isDelayRequestHeadersUntilFirstFlushEnabled = JavaMethod("()Z")
    start = JavaMethod("()V")
    read = JavaMethod("(Ljava/nio/ByteBuffer;)V")
    write = JavaMethod("(Ljava/nio/ByteBuffer;Z)V")
    flush = JavaMethod("()V")
    cancel = JavaMethod("()V")
    isDone = JavaMethod("()Z")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/http/BidirectionalStream/Builder"
        __javaconstructor__ = [("()V", False)]
        setHttpMethod = JavaMethod("(Ljava/lang/String;)Landroid/net/http/BidirectionalStream$Builder;")
        addHeader = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Landroid/net/http/BidirectionalStream$Builder;")
        setPriority = JavaMethod("(I)Landroid/net/http/BidirectionalStream$Builder;")
        setDelayRequestHeadersUntilFirstFlushEnabled = JavaMethod("(Z)Landroid/net/http/BidirectionalStream$Builder;")
        setTrafficStatsTag = JavaMethod("(I)Landroid/net/http/BidirectionalStream$Builder;")
        setTrafficStatsUid = JavaMethod("(I)Landroid/net/http/BidirectionalStream$Builder;")
        build = JavaMethod("()Landroid/net/http/BidirectionalStream;")

    class Callback(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/http/BidirectionalStream/Callback"
        onStreamReady = JavaMethod("(Landroid/net/http/BidirectionalStream;)V")
        onResponseHeadersReceived = JavaMethod("(Landroid/net/http/BidirectionalStream;Landroid/net/http/UrlResponseInfo;)V")
        onReadCompleted = JavaMethod("(Landroid/net/http/BidirectionalStream;Landroid/net/http/UrlResponseInfo;Ljava/nio/ByteBuffer;Z)V")
        onWriteCompleted = JavaMethod("(Landroid/net/http/BidirectionalStream;Landroid/net/http/UrlResponseInfo;Ljava/nio/ByteBuffer;Z)V")
        onResponseTrailersReceived = JavaMethod("(Landroid/net/http/BidirectionalStream;Landroid/net/http/UrlResponseInfo;Landroid/net/http/HeaderBlock;)V")
        onSucceeded = JavaMethod("(Landroid/net/http/BidirectionalStream;Landroid/net/http/UrlResponseInfo;)V")
        onFailed = JavaMethod("(Landroid/net/http/BidirectionalStream;Landroid/net/http/UrlResponseInfo;Landroid/net/http/HttpException;)V")
        onCanceled = JavaMethod("(Landroid/net/http/BidirectionalStream;Landroid/net/http/UrlResponseInfo;)V")