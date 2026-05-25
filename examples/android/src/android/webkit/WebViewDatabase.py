from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WebViewDatabase"]

class WebViewDatabase(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/WebViewDatabase"
    __javaconstructor__ = [("()V", False)]
    getInstance = JavaStaticMethod("(Landroid/content/Context;)Landroid/webkit/WebViewDatabase;")
    hasUsernamePassword = JavaMethod("()Z")
    clearUsernamePassword = JavaMethod("()V")
    hasHttpAuthUsernamePassword = JavaMethod("()Z")
    clearHttpAuthUsernamePassword = JavaMethod("()V")
    setHttpAuthUsernamePassword = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V")
    getHttpAuthUsernamePassword = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)[Ljava/lang/String;")
    hasFormData = JavaMethod("()Z")
    clearFormData = JavaMethod("()V")