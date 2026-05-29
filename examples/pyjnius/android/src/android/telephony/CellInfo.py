from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

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
    isRegistered = JavaMethod("()Z")
    getTimestampMillis = JavaMethod("()J")
    getTimeStamp = JavaMethod("()J")
    getCellIdentity = JavaMethod("()Landroid/telephony/CellIdentity;")
    getCellSignalStrength = JavaMethod("()Landroid/telephony/CellSignalStrength;")
    getCellConnectionStatus = JavaMethod("()I")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")