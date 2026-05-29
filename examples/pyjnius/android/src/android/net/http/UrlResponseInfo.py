from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UrlResponseInfo"]

class UrlResponseInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/http/UrlResponseInfo"
    __javaconstructor__ = [("()V", False)]
    wasCached = JavaMethod("()Z")
    getUrlChain = JavaMethod("()Ljava/util/List;")
    getHttpStatusText = JavaMethod("()Ljava/lang/String;")
    getHttpStatusCode = JavaMethod("()I")
    getNegotiatedProtocol = JavaMethod("()Ljava/lang/String;")
    getReceivedByteCount = JavaMethod("()J")
    getHeaders = JavaMethod("()Landroid/net/http/HeaderBlock;")
    getUrl = JavaMethod("()Ljava/lang/String;")