from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CookieManager"]

class CookieManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/CookieManager"
    __javaconstructor__ = [("()V", False)]
    flush = JavaMethod("()V")
    getInstance = JavaStaticMethod("()Landroid/webkit/CookieManager;")
    removeAllCookie = JavaMethod("()V")
    removeExpiredCookie = JavaMethod("()V")
    removeAllCookies = JavaMethod("(Landroid/webkit/ValueCallback;)V")
    setAcceptCookie = JavaMethod("(Z)V")
    removeSessionCookie = JavaMethod("()V")
    removeSessionCookies = JavaMethod("(Landroid/webkit/ValueCallback;)V")
    setAcceptFileSchemeCookies = JavaStaticMethod("(Z)V")
    setAcceptThirdPartyCookies = JavaMethod("(Landroid/webkit/WebView;Z)V")
    setCookie = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;)V", False, False), ("(Ljava/lang/String;Ljava/lang/String;Landroid/webkit/ValueCallback;)V", False, False)])
    allowFileSchemeCookies = JavaStaticMethod("()Z")
    getCookie = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    hasCookies = JavaMethod("()Z")
    acceptThirdPartyCookies = JavaMethod("(Landroid/webkit/WebView;)Z")
    acceptCookie = JavaMethod("()Z")