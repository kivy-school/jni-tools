from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HttpResponseCache"]

class HttpResponseCache(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/http/HttpResponseCache"
    getRequestCount = JavaMethod("()I")
    getNetworkCount = JavaMethod("()I")
    getHitCount = JavaMethod("()I")
    getInstalled = JavaStaticMethod("()Landroid/net/http/HttpResponseCache;")
    install = JavaStaticMethod("(Ljava/io/File;J)Landroid/net/http/HttpResponseCache;")
    size = JavaMethod("()J")
    maxSize = JavaMethod("()J")
    put = JavaMethod("(Ljava/net/URI;Ljava/net/URLConnection;)Ljava/net/CacheRequest;")
    flush = JavaMethod("()V")
    get = JavaMethod("(Ljava/net/URI;Ljava/lang/String;Ljava/util/Map;)Ljava/net/CacheResponse;")
    close = JavaMethod("()V")
    delete = JavaMethod("()V")