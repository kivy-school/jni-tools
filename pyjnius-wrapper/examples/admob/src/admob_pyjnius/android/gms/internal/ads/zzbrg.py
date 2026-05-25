from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbrg"]

class zzbrg(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbrg"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/webkit/WebView;)V", False)]
    zza = JavaMethod("()V")
    zzb = JavaMethod("(Landroid/webkit/WebViewClient;)V")
    getDelegate = JavaMethod("()Landroid/webkit/WebViewClient;")
    shouldOverrideUrlLoading = JavaMultipleMethod([("(Landroid/webkit/WebView;Landroid/webkit/WebResourceRequest;)Z", False, False), ("(Landroid/webkit/WebView;Ljava/lang/String;)Z", False, False)])
    onLoadResource = JavaMethod("(Landroid/webkit/WebView;Ljava/lang/String;)V")