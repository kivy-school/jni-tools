from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WebStorage"]

class WebStorage(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/WebStorage"
    getOrigins = JavaMethod("(Landroid/webkit/ValueCallback;)V")
    getUsageForOrigin = JavaMethod("(Ljava/lang/String;Landroid/webkit/ValueCallback;)V")
    getQuotaForOrigin = JavaMethod("(Ljava/lang/String;Landroid/webkit/ValueCallback;)V")
    setQuotaForOrigin = JavaMethod("(Ljava/lang/String;J)V")
    deleteOrigin = JavaMethod("(Ljava/lang/String;)V")
    deleteAllData = JavaMethod("()V")
    getInstance = JavaStaticMethod("()Landroid/webkit/WebStorage;")

    class Origin(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/webkit/WebStorage/Origin"
        getOrigin = JavaMethod("()Ljava/lang/String;")
        getQuota = JavaMethod("()J")
        getUsage = JavaMethod("()J")

    class QuotaUpdater(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/webkit/WebStorage/QuotaUpdater"
        updateQuota = JavaMethod("(J)V")