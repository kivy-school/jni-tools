from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PreciseDataConnectionState"]

class PreciseDataConnectionState(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/PreciseDataConnectionState"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    NETWORK_VALIDATION_FAILURE = JavaStaticField("I")
    NETWORK_VALIDATION_IN_PROGRESS = JavaStaticField("I")
    NETWORK_VALIDATION_NOT_REQUESTED = JavaStaticField("I")
    NETWORK_VALIDATION_SUCCESS = JavaStaticField("I")
    NETWORK_VALIDATION_UNSUPPORTED = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getNetworkType = JavaMethod("()I")
    getApnSetting = JavaMethod("()Landroid/telephony/data/ApnSetting;")
    getLinkProperties = JavaMethod("()Landroid/net/LinkProperties;")
    getNetworkValidationStatus = JavaMethod("()I")
    getTransportType = JavaMethod("()I")
    getLastCauseCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getId = JavaMethod("()I")
    getState = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")