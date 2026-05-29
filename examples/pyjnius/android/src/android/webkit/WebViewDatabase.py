from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WebViewDatabase"]

class WebViewDatabase(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/WebViewDatabase"
    __javaconstructor__ = [("()V", False)]
    clearHttpAuthUsernamePassword = JavaMethod("()V")
    hasFormData = JavaMethod("()Z")
    clearUsernamePassword = JavaMethod("()V")
    hasHttpAuthUsernamePassword = JavaMethod("()Z")
    hasUsernamePassword = JavaMethod("()Z")
    getInstance = JavaStaticMethod("(Landroid/content/Context;)Landroid/webkit/WebViewDatabase;")
    clearFormData = JavaMethod("()V")
    getHttpAuthUsernamePassword = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)[Ljava/lang/String;")
    setHttpAuthUsernamePassword = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V")