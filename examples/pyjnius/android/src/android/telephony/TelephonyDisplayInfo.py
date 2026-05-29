from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TelephonyDisplayInfo"]

class TelephonyDisplayInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/TelephonyDisplayInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    OVERRIDE_NETWORK_TYPE_LTE_ADVANCED_PRO = JavaStaticField("I")
    OVERRIDE_NETWORK_TYPE_LTE_CA = JavaStaticField("I")
    OVERRIDE_NETWORK_TYPE_NONE = JavaStaticField("I")
    OVERRIDE_NETWORK_TYPE_NR_ADVANCED = JavaStaticField("I")
    OVERRIDE_NETWORK_TYPE_NR_NSA = JavaStaticField("I")
    OVERRIDE_NETWORK_TYPE_NR_NSA_MMWAVE = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getNetworkType = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    isRoaming = JavaMethod("()Z")
    getOverrideNetworkType = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")