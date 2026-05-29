from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ReportUsageRequest"]

class ReportUsageRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/ReportUsageRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getDocumentId = JavaMethod("()Ljava/lang/String;")
    getNamespace = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getUsageTimestampMillis = JavaMethod("()J")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/appsearch/ReportUsageRequest$Builder"
        __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;)V", False)]
        setUsageTimestampMillis = JavaMethod("(J)Landroid/app/appsearch/ReportUsageRequest$Builder;")
        build = JavaMethod("()Landroid/app/appsearch/ReportUsageRequest;")