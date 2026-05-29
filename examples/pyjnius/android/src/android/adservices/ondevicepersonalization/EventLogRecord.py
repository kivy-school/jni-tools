from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EventLogRecord"]

class EventLogRecord(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/EventLogRecord"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getRowIndex = JavaMethod("()I")
    getRequestLogRecord = JavaMethod("()Landroid/adservices/ondevicepersonalization/RequestLogRecord;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getType = JavaMethod("()I")
    getData = JavaMethod("()Landroid/content/ContentValues;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getTime = JavaMethod("()Ljava/time/Instant;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/ondevicepersonalization/EventLogRecord$Builder"
        __javaconstructor__ = [("()V", False)]
        setRowIndex = JavaMethod("(I)Landroid/adservices/ondevicepersonalization/EventLogRecord$Builder;")
        setType = JavaMethod("(I)Landroid/adservices/ondevicepersonalization/EventLogRecord$Builder;")
        setData = JavaMethod("(Landroid/content/ContentValues;)Landroid/adservices/ondevicepersonalization/EventLogRecord$Builder;")
        build = JavaMethod("()Landroid/adservices/ondevicepersonalization/EventLogRecord;")
        setRequestLogRecord = JavaMethod("(Landroid/adservices/ondevicepersonalization/RequestLogRecord;)Landroid/adservices/ondevicepersonalization/EventLogRecord$Builder;")