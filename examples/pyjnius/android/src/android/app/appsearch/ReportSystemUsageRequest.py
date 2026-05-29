from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ReportSystemUsageRequest"]

class ReportSystemUsageRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/ReportSystemUsageRequest"
    getDocumentId = JavaMethod("()Ljava/lang/String;")
    getDatabaseName = JavaMethod("()Ljava/lang/String;")
    getPackageName = JavaMethod("()Ljava/lang/String;")
    getNamespace = JavaMethod("()Ljava/lang/String;")
    getUsageTimestampMillis = JavaMethod("()J")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/appsearch/ReportSystemUsageRequest$Builder"
        __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False)]
        setUsageTimestampMillis = JavaMethod("(J)Landroid/app/appsearch/ReportSystemUsageRequest$Builder;")
        build = JavaMethod("()Landroid/app/appsearch/ReportSystemUsageRequest;")