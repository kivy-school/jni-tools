from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WebChromeClient"]

class WebChromeClient(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/WebChromeClient"
    __javaconstructor__ = [("()V", False)]
    onProgressChanged = JavaMethod("(Landroid/webkit/WebView;I)V")
    onReceivedTitle = JavaMethod("(Landroid/webkit/WebView;Ljava/lang/String;)V")
    onReceivedIcon = JavaMethod("(Landroid/webkit/WebView;Landroid/graphics/Bitmap;)V")
    onReceivedTouchIconUrl = JavaMethod("(Landroid/webkit/WebView;Ljava/lang/String;Z)V")
    onShowCustomView = JavaMultipleMethod([("(Landroid/view/View;Landroid/webkit/WebChromeClient$CustomViewCallback;)V", False, False), ("(Landroid/view/View;ILandroid/webkit/WebChromeClient$CustomViewCallback;)V", False, False)])
    onHideCustomView = JavaMethod("()V")
    onCreateWindow = JavaMethod("(Landroid/webkit/WebView;ZZLandroid/os/Message;)Z")
    onRequestFocus = JavaMethod("(Landroid/webkit/WebView;)V")
    onCloseWindow = JavaMethod("(Landroid/webkit/WebView;)V")
    onJsAlert = JavaMethod("(Landroid/webkit/WebView;Ljava/lang/String;Ljava/lang/String;Landroid/webkit/JsResult;)Z")
    onJsConfirm = JavaMethod("(Landroid/webkit/WebView;Ljava/lang/String;Ljava/lang/String;Landroid/webkit/JsResult;)Z")
    onJsPrompt = JavaMethod("(Landroid/webkit/WebView;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Landroid/webkit/JsPromptResult;)Z")
    onJsBeforeUnload = JavaMethod("(Landroid/webkit/WebView;Ljava/lang/String;Ljava/lang/String;Landroid/webkit/JsResult;)Z")
    onExceededDatabaseQuota = JavaMethod("(Ljava/lang/String;Ljava/lang/String;JJJLandroid/webkit/WebStorage$QuotaUpdater;)V")
    onGeolocationPermissionsShowPrompt = JavaMethod("(Ljava/lang/String;Landroid/webkit/GeolocationPermissions$Callback;)V")
    onGeolocationPermissionsHidePrompt = JavaMethod("()V")
    onPermissionRequest = JavaMethod("(Landroid/webkit/PermissionRequest;)V")
    onPermissionRequestCanceled = JavaMethod("(Landroid/webkit/PermissionRequest;)V")
    onJsTimeout = JavaMethod("()Z")
    onConsoleMessage = JavaMultipleMethod([("(Ljava/lang/String;ILjava/lang/String;)V", False, False), ("(Landroid/webkit/ConsoleMessage;)Z", False, False)])
    getDefaultVideoPoster = JavaMethod("()Landroid/graphics/Bitmap;")
    getVideoLoadingProgressView = JavaMethod("()Landroid/view/View;")
    getVisitedHistory = JavaMethod("(Landroid/webkit/ValueCallback;)V")
    onShowFileChooser = JavaMethod("(Landroid/webkit/WebView;Landroid/webkit/ValueCallback;Landroid/webkit/WebChromeClient$FileChooserParams;)Z")

    class CustomViewCallback(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/webkit/WebChromeClient/CustomViewCallback"
        onCustomViewHidden = JavaMethod("()V")

    class FileChooserParams(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/webkit/WebChromeClient/FileChooserParams"
        __javaconstructor__ = [("()V", False)]
        MODE_OPEN = JavaStaticField("I")
        MODE_OPEN_MULTIPLE = JavaStaticField("I")
        MODE_SAVE = JavaStaticField("I")
        parseResult = JavaStaticMethod("(ILandroid/content/Intent;)[Landroid/net/Uri;")
        getMode = JavaMethod("()I")
        getAcceptTypes = JavaMethod("()[Ljava/lang/String;")
        isCaptureEnabled = JavaMethod("()Z")
        getTitle = JavaMethod("()Ljava/lang/CharSequence;")
        getFilenameHint = JavaMethod("()Ljava/lang/String;")
        createIntent = JavaMethod("()Landroid/content/Intent;")