from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WebChromeClient"]

class WebChromeClient(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/WebChromeClient"
    __javaconstructor__ = [("()V", False)]
    onReceivedIcon = JavaMethod("(Landroid/webkit/WebView;Landroid/graphics/Bitmap;)V")
    getVisitedHistory = JavaMethod("(Landroid/webkit/ValueCallback;)V")
    getDefaultVideoPoster = JavaMethod("()Landroid/graphics/Bitmap;")
    getVideoLoadingProgressView = JavaMethod("()Landroid/view/View;")
    onCloseWindow = JavaMethod("(Landroid/webkit/WebView;)V")
    onConsoleMessage = JavaMultipleMethod([("(Ljava/lang/String;ILjava/lang/String;)V", False, False), ("(Landroid/webkit/ConsoleMessage;)Z", False, False)])
    onCreateWindow = JavaMethod("(Landroid/webkit/WebView;ZZLandroid/os/Message;)Z")
    onExceededDatabaseQuota = JavaMethod("(Ljava/lang/String;Ljava/lang/String;JJJLandroid/webkit/WebStorage$QuotaUpdater;)V")
    onGeolocationPermissionsHidePrompt = JavaMethod("()V")
    onGeolocationPermissionsShowPrompt = JavaMethod("(Ljava/lang/String;Landroid/webkit/GeolocationPermissions$Callback;)V")
    onHideCustomView = JavaMethod("()V")
    onJsAlert = JavaMethod("(Landroid/webkit/WebView;Ljava/lang/String;Ljava/lang/String;Landroid/webkit/JsResult;)Z")
    onJsBeforeUnload = JavaMethod("(Landroid/webkit/WebView;Ljava/lang/String;Ljava/lang/String;Landroid/webkit/JsResult;)Z")
    onJsConfirm = JavaMethod("(Landroid/webkit/WebView;Ljava/lang/String;Ljava/lang/String;Landroid/webkit/JsResult;)Z")
    onJsPrompt = JavaMethod("(Landroid/webkit/WebView;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Landroid/webkit/JsPromptResult;)Z")
    onJsTimeout = JavaMethod("()Z")
    onPermissionRequest = JavaMethod("(Landroid/webkit/PermissionRequest;)V")
    onPermissionRequestCanceled = JavaMethod("(Landroid/webkit/PermissionRequest;)V")
    onReceivedTitle = JavaMethod("(Landroid/webkit/WebView;Ljava/lang/String;)V")
    onReceivedTouchIconUrl = JavaMethod("(Landroid/webkit/WebView;Ljava/lang/String;Z)V")
    onRequestFocus = JavaMethod("(Landroid/webkit/WebView;)V")
    onShowCustomView = JavaMultipleMethod([("(Landroid/view/View;ILandroid/webkit/WebChromeClient$CustomViewCallback;)V", False, False), ("(Landroid/view/View;Landroid/webkit/WebChromeClient$CustomViewCallback;)V", False, False)])
    onShowFileChooser = JavaMethod("(Landroid/webkit/WebView;Landroid/webkit/ValueCallback;Landroid/webkit/WebChromeClient$FileChooserParams;)Z")
    onProgressChanged = JavaMethod("(Landroid/webkit/WebView;I)V")

    class FileChooserParams(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/webkit/WebChromeClient$FileChooserParams"
        __javaconstructor__ = [("()V", False)]
        MODE_OPEN = JavaStaticField("I")
        MODE_OPEN_MULTIPLE = JavaStaticField("I")
        MODE_SAVE = JavaStaticField("I")
        getMode = JavaMethod("()I")
        getTitle = JavaMethod("()Ljava/lang/CharSequence;")
        createIntent = JavaMethod("()Landroid/content/Intent;")
        getAcceptTypes = JavaMethod("()[Ljava/lang/String;")
        getFilenameHint = JavaMethod("()Ljava/lang/String;")
        isCaptureEnabled = JavaMethod("()Z")
        parseResult = JavaStaticMethod("(ILandroid/content/Intent;)[Landroid/net/Uri;")

    class CustomViewCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/webkit/WebChromeClient$CustomViewCallback"
        onCustomViewHidden = JavaMethod("()V")