from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RequestLogRecord"]

class RequestLogRecord(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/RequestLogRecord"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getTime = JavaMethod("()Ljava/time/Instant;")
    getRows = JavaMethod("()Ljava/util/List;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/ondevicepersonalization/RequestLogRecord/Builder"
        __javaconstructor__ = [("()V", False)]
        setRows = JavaMethod("(Ljava/util/List;)Landroid/adservices/ondevicepersonalization/RequestLogRecord$Builder;")
        addRow = JavaMethod("(Landroid/content/ContentValues;)Landroid/adservices/ondevicepersonalization/RequestLogRecord$Builder;")
        build = JavaMethod("()Landroid/adservices/ondevicepersonalization/RequestLogRecord;")