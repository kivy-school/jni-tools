from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CacheRequest"]

class CacheRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/CacheRequest"
    __javaconstructor__ = [("()V", False)]
    abort = JavaMethod("()V")
    getBody = JavaMethod("()Ljava/io/OutputStream;")