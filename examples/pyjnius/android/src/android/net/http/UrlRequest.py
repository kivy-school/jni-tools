from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UrlRequest"]

class UrlRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/http/UrlRequest"
    REQUEST_PRIORITY_HIGHEST = JavaStaticField("I")
    REQUEST_PRIORITY_IDLE = JavaStaticField("I")
    REQUEST_PRIORITY_LOW = JavaStaticField("I")
    REQUEST_PRIORITY_LOWEST = JavaStaticField("I")
    REQUEST_PRIORITY_MEDIUM = JavaStaticField("I")
    getStatus = JavaMethod("(Landroid/net/http/UrlRequest$StatusListener;)V")
    hasTrafficStatsUid = JavaMethod("()Z")
    isCacheDisabled = JavaMethod("()Z")
    hasTrafficStatsTag = JavaMethod("()Z")
    getTrafficStatsUid = JavaMethod("()I")
    getTrafficStatsTag = JavaMethod("()I")
    isDirectExecutorAllowed = JavaMethod("()Z")
    getHttpMethod = JavaMethod("()Ljava/lang/String;")
    followRedirect = JavaMethod("()V")
    getHeaders = JavaMethod("()Landroid/net/http/HeaderBlock;")
    start = JavaMethod("()V")
    getPriority = JavaMethod("()I")
    isDone = JavaMethod("()Z")
    cancel = JavaMethod("()V")
    read = JavaMethod("(Ljava/nio/ByteBuffer;)V")

    class StatusListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/http/UrlRequest$StatusListener"
        onStatus = JavaMethod("(I)V")

    class Status(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/http/UrlRequest$Status"
        CONNECTING = JavaStaticField("I")
        DOWNLOADING_PAC_FILE = JavaStaticField("I")
        ESTABLISHING_PROXY_TUNNEL = JavaStaticField("I")
        IDLE = JavaStaticField("I")
        INVALID = JavaStaticField("I")
        READING_RESPONSE = JavaStaticField("I")
        RESOLVING_HOST = JavaStaticField("I")
        RESOLVING_HOST_IN_PAC_FILE = JavaStaticField("I")
        RESOLVING_PROXY_FOR_URL = JavaStaticField("I")
        SENDING_REQUEST = JavaStaticField("I")
        SSL_HANDSHAKE = JavaStaticField("I")
        WAITING_FOR_AVAILABLE_SOCKET = JavaStaticField("I")
        WAITING_FOR_CACHE = JavaStaticField("I")
        WAITING_FOR_DELEGATE = JavaStaticField("I")
        WAITING_FOR_RESPONSE = JavaStaticField("I")
        WAITING_FOR_STALLED_SOCKET_POOL = JavaStaticField("I")

    class Callback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/http/UrlRequest$Callback"
        onFailed = JavaMethod("(Landroid/net/http/UrlRequest;Landroid/net/http/UrlResponseInfo;Landroid/net/http/HttpException;)V")
        onSucceeded = JavaMethod("(Landroid/net/http/UrlRequest;Landroid/net/http/UrlResponseInfo;)V")
        onReadCompleted = JavaMethod("(Landroid/net/http/UrlRequest;Landroid/net/http/UrlResponseInfo;Ljava/nio/ByteBuffer;)V")
        onRedirectReceived = JavaMethod("(Landroid/net/http/UrlRequest;Landroid/net/http/UrlResponseInfo;Ljava/lang/String;)V")
        onResponseStarted = JavaMethod("(Landroid/net/http/UrlRequest;Landroid/net/http/UrlResponseInfo;)V")
        onCanceled = JavaMethod("(Landroid/net/http/UrlRequest;Landroid/net/http/UrlResponseInfo;)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/http/UrlRequest$Builder"
        bindToNetwork = JavaMethod("(Landroid/net/Network;)Landroid/net/http/UrlRequest$Builder;")
        addHeader = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Landroid/net/http/UrlRequest$Builder;")
        setHttpMethod = JavaMethod("(Ljava/lang/String;)Landroid/net/http/UrlRequest$Builder;")
        setTrafficStatsTag = JavaMethod("(I)Landroid/net/http/UrlRequest$Builder;")
        setTrafficStatsUid = JavaMethod("(I)Landroid/net/http/UrlRequest$Builder;")
        setDirectExecutorAllowed = JavaMethod("(Z)Landroid/net/http/UrlRequest$Builder;")
        setUploadDataProvider = JavaMethod("(Landroid/net/http/UploadDataProvider;Ljava/util/concurrent/Executor;)Landroid/net/http/UrlRequest$Builder;")
        setCacheDisabled = JavaMethod("(Z)Landroid/net/http/UrlRequest$Builder;")
        setPriority = JavaMethod("(I)Landroid/net/http/UrlRequest$Builder;")
        build = JavaMethod("()Landroid/net/http/UrlRequest;")