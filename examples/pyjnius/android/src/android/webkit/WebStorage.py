from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WebStorage"]

class WebStorage(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/WebStorage"
    getOrigins = JavaMethod("(Landroid/webkit/ValueCallback;)V")
    deleteAllData = JavaMethod("()V")
    deleteOrigin = JavaMethod("(Ljava/lang/String;)V")
    setQuotaForOrigin = JavaMethod("(Ljava/lang/String;J)V")
    getQuotaForOrigin = JavaMethod("(Ljava/lang/String;Landroid/webkit/ValueCallback;)V")
    getUsageForOrigin = JavaMethod("(Ljava/lang/String;Landroid/webkit/ValueCallback;)V")
    getInstance = JavaStaticMethod("()Landroid/webkit/WebStorage;")

    class QuotaUpdater(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/webkit/WebStorage$QuotaUpdater"
        updateQuota = JavaMethod("(J)V")

    class Origin(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/webkit/WebStorage$Origin"
        getQuota = JavaMethod("()J")
        getOrigin = JavaMethod("()Ljava/lang/String;")
        getUsage = JavaMethod("()J")