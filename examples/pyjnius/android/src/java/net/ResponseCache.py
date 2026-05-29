from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ResponseCache"]

class ResponseCache(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/ResponseCache"
    __javaconstructor__ = [("()V", False)]
    getDefault = JavaStaticMethod("()Ljava/net/ResponseCache;")
    setDefault = JavaStaticMethod("(Ljava/net/ResponseCache;)V")
    get = JavaMethod("(Ljava/net/URI;Ljava/lang/String;Ljava/util/Map;)Ljava/net/CacheResponse;")
    put = JavaMethod("(Ljava/net/URI;Ljava/net/URLConnection;)Ljava/net/CacheRequest;")