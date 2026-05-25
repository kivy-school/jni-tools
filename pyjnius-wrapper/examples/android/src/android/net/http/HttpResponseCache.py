from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HttpResponseCache"]

class HttpResponseCache(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/http/HttpResponseCache"
    getInstalled = JavaStaticMethod("()Landroid/net/http/HttpResponseCache;")
    install = JavaStaticMethod("(Ljava/io/File;J)Landroid/net/http/HttpResponseCache;")
    get = JavaMethod("(Ljava/net/URI;Ljava/lang/String;Ljava/util/Map;)Ljava/net/CacheResponse;")
    put = JavaMethod("(Ljava/net/URI;Ljava/net/URLConnection;)Ljava/net/CacheRequest;")
    size = JavaMethod("()J")
    maxSize = JavaMethod("()J")
    flush = JavaMethod("()V")
    getNetworkCount = JavaMethod("()I")
    getHitCount = JavaMethod("()I")
    getRequestCount = JavaMethod("()I")
    close = JavaMethod("()V")
    delete = JavaMethod("()V")