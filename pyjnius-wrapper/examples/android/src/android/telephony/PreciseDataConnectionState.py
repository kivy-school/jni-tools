from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PreciseDataConnectionState"]

class PreciseDataConnectionState(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/PreciseDataConnectionState"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    NETWORK_VALIDATION_FAILURE = JavaStaticField("I")
    NETWORK_VALIDATION_IN_PROGRESS = JavaStaticField("I")
    NETWORK_VALIDATION_NOT_REQUESTED = JavaStaticField("I")
    NETWORK_VALIDATION_SUCCESS = JavaStaticField("I")
    NETWORK_VALIDATION_UNSUPPORTED = JavaStaticField("I")
    getTransportType = JavaMethod("()I")
    getId = JavaMethod("()I")
    getState = JavaMethod("()I")
    getNetworkType = JavaMethod("()I")
    getLinkProperties = JavaMethod("()Landroid/net/LinkProperties;")
    getLastCauseCode = JavaMethod("()I")
    getApnSetting = JavaMethod("()Landroid/telephony/data/ApnSetting;")
    getNetworkValidationStatus = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")