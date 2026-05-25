from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CacheRequest"]

class CacheRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/CacheRequest"
    __javaconstructor__ = [("()V", False)]
    getBody = JavaMethod("()Ljava/io/OutputStream;")
    abort = JavaMethod("()V")