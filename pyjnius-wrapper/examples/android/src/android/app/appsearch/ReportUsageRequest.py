from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ReportUsageRequest"]

class ReportUsageRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/ReportUsageRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getNamespace = JavaMethod("()Ljava/lang/String;")
    getDocumentId = JavaMethod("()Ljava/lang/String;")
    getUsageTimestampMillis = JavaMethod("()J")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/appsearch/ReportUsageRequest/Builder"
        __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;)V", False)]
        setUsageTimestampMillis = JavaMethod("(J)Landroid/app/appsearch/ReportUsageRequest$Builder;")
        build = JavaMethod("()Landroid/app/appsearch/ReportUsageRequest;")