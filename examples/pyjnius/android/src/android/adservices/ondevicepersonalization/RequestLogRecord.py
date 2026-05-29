from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RequestLogRecord"]

class RequestLogRecord(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/RequestLogRecord"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getRows = JavaMethod("()Ljava/util/List;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getTime = JavaMethod("()Ljava/time/Instant;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/ondevicepersonalization/RequestLogRecord$Builder"
        __javaconstructor__ = [("()V", False)]
        addRow = JavaMethod("(Landroid/content/ContentValues;)Landroid/adservices/ondevicepersonalization/RequestLogRecord$Builder;")
        setRows = JavaMethod("(Ljava/util/List;)Landroid/adservices/ondevicepersonalization/RequestLogRecord$Builder;")
        build = JavaMethod("()Landroid/adservices/ondevicepersonalization/RequestLogRecord;")