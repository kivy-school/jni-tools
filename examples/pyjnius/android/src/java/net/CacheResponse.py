from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CacheResponse"]

class CacheResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/CacheResponse"
    __javaconstructor__ = [("()V", False)]
    getHeaders = JavaMethod("()Ljava/util/Map;")
    getBody = JavaMethod("()Ljava/io/InputStream;")