from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UrlResponseInfo"]

class UrlResponseInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/http/UrlResponseInfo"
    __javaconstructor__ = [("()V", False)]
    getUrl = JavaMethod("()Ljava/lang/String;")
    getUrlChain = JavaMethod("()Ljava/util/List;")
    getHttpStatusCode = JavaMethod("()I")
    getHttpStatusText = JavaMethod("()Ljava/lang/String;")
    getHeaders = JavaMethod("()Landroid/net/http/HeaderBlock;")
    wasCached = JavaMethod("()Z")
    getNegotiatedProtocol = JavaMethod("()Ljava/lang/String;")
    getReceivedByteCount = JavaMethod("()J")