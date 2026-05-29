from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ResponseCache"]

class ResponseCache(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/ResponseCache"
    __javaconstructor__ = [("()V", False)]
    put = JavaMethod("(Ljava/net/URI;Ljava/net/URLConnection;)Ljava/net/CacheRequest;")
    get = JavaMethod("(Ljava/net/URI;Ljava/lang/String;Ljava/util/Map;)Ljava/net/CacheResponse;")
    getDefault = JavaStaticMethod("()Ljava/net/ResponseCache;")
    setDefault = JavaStaticMethod("(Ljava/net/ResponseCache;)V")