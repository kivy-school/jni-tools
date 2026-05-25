from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EventLogRecord"]

class EventLogRecord(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/EventLogRecord"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getTime = JavaMethod("()Ljava/time/Instant;")
    getRowIndex = JavaMethod("()I")
    getType = JavaMethod("()I")
    getData = JavaMethod("()Landroid/content/ContentValues;")
    getRequestLogRecord = JavaMethod("()Landroid/adservices/ondevicepersonalization/RequestLogRecord;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/ondevicepersonalization/EventLogRecord/Builder"
        __javaconstructor__ = [("()V", False)]
        setRowIndex = JavaMethod("(I)Landroid/adservices/ondevicepersonalization/EventLogRecord$Builder;")
        setType = JavaMethod("(I)Landroid/adservices/ondevicepersonalization/EventLogRecord$Builder;")
        setData = JavaMethod("(Landroid/content/ContentValues;)Landroid/adservices/ondevicepersonalization/EventLogRecord$Builder;")
        setRequestLogRecord = JavaMethod("(Landroid/adservices/ondevicepersonalization/RequestLogRecord;)Landroid/adservices/ondevicepersonalization/EventLogRecord$Builder;")
        build = JavaMethod("()Landroid/adservices/ondevicepersonalization/EventLogRecord;")