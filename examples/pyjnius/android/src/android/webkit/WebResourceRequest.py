from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WebResourceRequest"]

class WebResourceRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/WebResourceRequest"
    getMethod = JavaMethod("()Ljava/lang/String;")
    getUrl = JavaMethod("()Landroid/net/Uri;")
    getRequestHeaders = JavaMethod("()Ljava/util/Map;")
    hasGesture = JavaMethod("()Z")
    isForMainFrame = JavaMethod("()Z")
    isRedirect = JavaMethod("()Z")