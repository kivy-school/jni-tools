from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UrlRequest"]

class UrlRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/http/UrlRequest"
    REQUEST_PRIORITY_HIGHEST = JavaStaticField("I")
    REQUEST_PRIORITY_IDLE = JavaStaticField("I")
    REQUEST_PRIORITY_LOW = JavaStaticField("I")
    REQUEST_PRIORITY_LOWEST = JavaStaticField("I")
    REQUEST_PRIORITY_MEDIUM = JavaStaticField("I")
    getHttpMethod = JavaMethod("()Ljava/lang/String;")
    getHeaders = JavaMethod("()Landroid/net/http/HeaderBlock;")
    isCacheDisabled = JavaMethod("()Z")
    isDirectExecutorAllowed = JavaMethod("()Z")
    getPriority = JavaMethod("()I")
    hasTrafficStatsTag = JavaMethod("()Z")
    getTrafficStatsTag = JavaMethod("()I")
    hasTrafficStatsUid = JavaMethod("()Z")
    getTrafficStatsUid = JavaMethod("()I")
    start = JavaMethod("()V")
    followRedirect = JavaMethod("()V")
    read = JavaMethod("(Ljava/nio/ByteBuffer;)V")
    cancel = JavaMethod("()V")
    isDone = JavaMethod("()Z")
    getStatus = JavaMethod("(Landroid/net/http/UrlRequest$StatusListener;)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/http/UrlRequest/Builder"
        setHttpMethod = JavaMethod("(Ljava/lang/String;)Landroid/net/http/UrlRequest$Builder;")
        addHeader = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Landroid/net/http/UrlRequest$Builder;")
        setCacheDisabled = JavaMethod("(Z)Landroid/net/http/UrlRequest$Builder;")
        setPriority = JavaMethod("(I)Landroid/net/http/UrlRequest$Builder;")
        setUploadDataProvider = JavaMethod("(Landroid/net/http/UploadDataProvider;Ljava/util/concurrent/Executor;)Landroid/net/http/UrlRequest$Builder;")
        setDirectExecutorAllowed = JavaMethod("(Z)Landroid/net/http/UrlRequest$Builder;")
        bindToNetwork = JavaMethod("(Landroid/net/Network;)Landroid/net/http/UrlRequest$Builder;")
        setTrafficStatsTag = JavaMethod("(I)Landroid/net/http/UrlRequest$Builder;")
        setTrafficStatsUid = JavaMethod("(I)Landroid/net/http/UrlRequest$Builder;")
        build = JavaMethod("()Landroid/net/http/UrlRequest;")

    class Callback(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/http/UrlRequest/Callback"
        onRedirectReceived = JavaMethod("(Landroid/net/http/UrlRequest;Landroid/net/http/UrlResponseInfo;Ljava/lang/String;)V")
        onResponseStarted = JavaMethod("(Landroid/net/http/UrlRequest;Landroid/net/http/UrlResponseInfo;)V")
        onReadCompleted = JavaMethod("(Landroid/net/http/UrlRequest;Landroid/net/http/UrlResponseInfo;Ljava/nio/ByteBuffer;)V")
        onSucceeded = JavaMethod("(Landroid/net/http/UrlRequest;Landroid/net/http/UrlResponseInfo;)V")
        onFailed = JavaMethod("(Landroid/net/http/UrlRequest;Landroid/net/http/UrlResponseInfo;Landroid/net/http/HttpException;)V")
        onCanceled = JavaMethod("(Landroid/net/http/UrlRequest;Landroid/net/http/UrlResponseInfo;)V")

    class Status(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/http/UrlRequest/Status"
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

    class StatusListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/http/UrlRequest/StatusListener"
        onStatus = JavaMethod("(I)V")