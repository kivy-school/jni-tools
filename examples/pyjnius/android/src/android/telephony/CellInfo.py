from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CellInfo"]

class CellInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/CellInfo"
    CONNECTION_NONE = JavaStaticField("I")
    CONNECTION_PRIMARY_SERVING = JavaStaticField("I")
    CONNECTION_SECONDARY_SERVING = JavaStaticField("I")
    CONNECTION_UNKNOWN = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    UNAVAILABLE = JavaStaticField("I")
    UNAVAILABLE_LONG = JavaStaticField("J")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getCellConnectionStatus = JavaMethod("()I")
    getTimeStamp = JavaMethod("()J")
    getCellIdentity = JavaMethod("()Landroid/telephony/CellIdentity;")
    getCellSignalStrength = JavaMethod("()Landroid/telephony/CellSignalStrength;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    isRegistered = JavaMethod("()Z")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getTimestampMillis = JavaMethod("()J")