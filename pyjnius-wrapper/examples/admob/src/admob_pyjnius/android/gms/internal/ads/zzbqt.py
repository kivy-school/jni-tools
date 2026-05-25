from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbqt"]

class zzbqt(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbqt"
    __javaconstructor__ = [("()V", False)]
    getDelegate = JavaMethod("()Landroid/webkit/WebViewClient;")
    shouldOverrideUrlLoading = JavaMultipleMethod([("(Landroid/webkit/WebView;Ljava/lang/String;)Z", False, False), ("(Landroid/webkit/WebView;Landroid/webkit/WebResourceRequest;)Z", False, False)])
    onPageStarted = JavaMethod("(Landroid/webkit/WebView;Ljava/lang/String;Landroid/graphics/Bitmap;)V")
    onPageFinished = JavaMethod("(Landroid/webkit/WebView;Ljava/lang/String;)V")
    onLoadResource = JavaMethod("(Landroid/webkit/WebView;Ljava/lang/String;)V")
    onPageCommitVisible = JavaMethod("(Landroid/webkit/WebView;Ljava/lang/String;)V")
    shouldInterceptRequest = JavaMultipleMethod([("(Landroid/webkit/WebView;Ljava/lang/String;)Landroid/webkit/WebResourceResponse;", False, False), ("(Landroid/webkit/WebView;Landroid/webkit/WebResourceRequest;)Landroid/webkit/WebResourceResponse;", False, False)])
    onTooManyRedirects = JavaMethod("(Landroid/webkit/WebView;Landroid/os/Message;Landroid/os/Message;)V")
    onReceivedError = JavaMultipleMethod([("(Landroid/webkit/WebView;ILjava/lang/String;Ljava/lang/String;)V", False, False), ("(Landroid/webkit/WebView;Landroid/webkit/WebResourceRequest;Landroid/webkit/WebResourceError;)V", False, False)])
    onReceivedHttpError = JavaMethod("(Landroid/webkit/WebView;Landroid/webkit/WebResourceRequest;Landroid/webkit/WebResourceResponse;)V")
    onFormResubmission = JavaMethod("(Landroid/webkit/WebView;Landroid/os/Message;Landroid/os/Message;)V")
    doUpdateVisitedHistory = JavaMethod("(Landroid/webkit/WebView;Ljava/lang/String;Z)V")
    onReceivedSslError = JavaMethod("(Landroid/webkit/WebView;Landroid/webkit/SslErrorHandler;Landroid/net/http/SslError;)V")
    onReceivedClientCertRequest = JavaMethod("(Landroid/webkit/WebView;Landroid/webkit/ClientCertRequest;)V")
    onReceivedHttpAuthRequest = JavaMethod("(Landroid/webkit/WebView;Landroid/webkit/HttpAuthHandler;Ljava/lang/String;Ljava/lang/String;)V")
    shouldOverrideKeyEvent = JavaMethod("(Landroid/webkit/WebView;Landroid/view/KeyEvent;)Z")
    onUnhandledKeyEvent = JavaMethod("(Landroid/webkit/WebView;Landroid/view/KeyEvent;)V")
    onScaleChanged = JavaMethod("(Landroid/webkit/WebView;FF)V")
    onReceivedLoginRequest = JavaMethod("(Landroid/webkit/WebView;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V")
    onRenderProcessGone = JavaMethod("(Landroid/webkit/WebView;Landroid/webkit/RenderProcessGoneDetail;)Z")
    onSafeBrowsingHit = JavaMethod("(Landroid/webkit/WebView;Landroid/webkit/WebResourceRequest;ILandroid/webkit/SafeBrowsingResponse;)V")