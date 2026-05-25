from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WebResourceRequest"]

class WebResourceRequest(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/WebResourceRequest"
    getUrl = JavaMethod("()Landroid/net/Uri;")
    isForMainFrame = JavaMethod("()Z")
    isRedirect = JavaMethod("()Z")
    hasGesture = JavaMethod("()Z")
    getMethod = JavaMethod("()Ljava/lang/String;")
    getRequestHeaders = JavaMethod("()Ljava/util/Map;")