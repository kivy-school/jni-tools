from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["H5AdsWebViewClient"]

class H5AdsWebViewClient(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/h5/H5AdsWebViewClient"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/webkit/WebView;)V", False)]
    clearAdObjects = JavaMethod("()V")
    setDelegateWebViewClient = JavaMethod("(Landroid/webkit/WebViewClient;)V")
    getDelegateWebViewClient = JavaMethod("()Landroid/webkit/WebViewClient;")
    getDelegate = JavaMethod("()Landroid/webkit/WebViewClient;")