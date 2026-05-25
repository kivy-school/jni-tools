from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HttpEngine"]

class HttpEngine(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/http/HttpEngine"
    getVersionString = JavaStaticMethod("()Ljava/lang/String;")
    shutdown = JavaMethod("()V")
    bindToNetwork = JavaMethod("(Landroid/net/Network;)V")
    openConnection = JavaMethod("(Ljava/net/URL;)Ljava/net/URLConnection;")
    createUrlStreamHandlerFactory = JavaMethod("()Ljava/net/URLStreamHandlerFactory;")
    newUrlRequestBuilder = JavaMethod("(Ljava/lang/String;Ljava/util/concurrent/Executor;Landroid/net/http/UrlRequest$Callback;)Landroid/net/http/UrlRequest$Builder;")
    newBidirectionalStreamBuilder = JavaMethod("(Ljava/lang/String;Ljava/util/concurrent/Executor;Landroid/net/http/BidirectionalStream$Callback;)Landroid/net/http/BidirectionalStream$Builder;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/http/HttpEngine/Builder"
        __javaconstructor__ = [("(Landroid/content/Context;)V", False)]
        HTTP_CACHE_DISABLED = JavaStaticField("I")
        HTTP_CACHE_DISK = JavaStaticField("I")
        HTTP_CACHE_DISK_NO_HTTP = JavaStaticField("I")
        HTTP_CACHE_IN_MEMORY = JavaStaticField("I")
        getDefaultUserAgent = JavaMethod("()Ljava/lang/String;")
        setUserAgent = JavaMethod("(Ljava/lang/String;)Landroid/net/http/HttpEngine$Builder;")
        setStoragePath = JavaMethod("(Ljava/lang/String;)Landroid/net/http/HttpEngine$Builder;")
        setEnableQuic = JavaMethod("(Z)Landroid/net/http/HttpEngine$Builder;")
        setEnableHttp2 = JavaMethod("(Z)Landroid/net/http/HttpEngine$Builder;")
        setEnableBrotli = JavaMethod("(Z)Landroid/net/http/HttpEngine$Builder;")
        setEnableHttpCache = JavaMethod("(IJ)Landroid/net/http/HttpEngine$Builder;")
        addQuicHint = JavaMethod("(Ljava/lang/String;II)Landroid/net/http/HttpEngine$Builder;")
        addPublicKeyPins = JavaMethod("(Ljava/lang/String;Ljava/util/Set;ZLjava/time/Instant;)Landroid/net/http/HttpEngine$Builder;")
        setEnablePublicKeyPinningBypassForLocalTrustAnchors = JavaMethod("(Z)Landroid/net/http/HttpEngine$Builder;")
        setQuicOptions = JavaMethod("(Landroid/net/http/QuicOptions;)Landroid/net/http/HttpEngine$Builder;")
        setDnsOptions = JavaMethod("(Landroid/net/http/DnsOptions;)Landroid/net/http/HttpEngine$Builder;")
        setConnectionMigrationOptions = JavaMethod("(Landroid/net/http/ConnectionMigrationOptions;)Landroid/net/http/HttpEngine$Builder;")
        build = JavaMethod("()Landroid/net/http/HttpEngine;")