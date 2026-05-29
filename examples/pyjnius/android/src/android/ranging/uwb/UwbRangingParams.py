from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UwbRangingParams"]

class UwbRangingParams(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/ranging/uwb/UwbRangingParams"
    CONFIG_MULTICAST_DS_TWR = JavaStaticField("I")
    CONFIG_PROVISIONED_INDIVIDUAL_MULTICAST_DS_TWR = JavaStaticField("I")
    CONFIG_PROVISIONED_MULTICAST_DS_TWR = JavaStaticField("I")
    CONFIG_PROVISIONED_UNICAST_DS_TWR = JavaStaticField("I")
    CONFIG_PROVISIONED_UNICAST_DS_TWR_VERY_FAST = JavaStaticField("I")
    CONFIG_UNICAST_DS_TWR = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    DURATION_1_MS = JavaStaticField("I")
    DURATION_2_MS = JavaStaticField("I")
    SUB_SESSION_UNDEFINED = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getComplexChannel = JavaMethod("()Landroid/ranging/uwb/UwbComplexChannel;")
    getConfigId = JavaMethod("()I")
    getDeviceAddress = JavaMethod("()Landroid/ranging/uwb/UwbAddress;")
    getPeerAddress = JavaMethod("()Landroid/ranging/uwb/UwbAddress;")
    getRangingUpdateRate = JavaMethod("()I")
    getSessionId = JavaMethod("()I")
    getSessionKeyInfo = JavaMethod("()[B")
    getSlotDuration = JavaMethod("()I")
    getSubSessionId = JavaMethod("()I")
    getSubSessionKeyInfo = JavaMethod("()[B")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/ranging/uwb/UwbRangingParams$Builder"
        __javaconstructor__ = [("(IILandroid/ranging/uwb/UwbAddress;Landroid/ranging/uwb/UwbAddress;)V", False)]
        setComplexChannel = JavaMethod("(Landroid/ranging/uwb/UwbComplexChannel;)Landroid/ranging/uwb/UwbRangingParams$Builder;")
        setRangingUpdateRate = JavaMethod("(I)Landroid/ranging/uwb/UwbRangingParams$Builder;")
        setSubSessionId = JavaMethod("(I)Landroid/ranging/uwb/UwbRangingParams$Builder;")
        setSessionKeyInfo = JavaMethod("([B)Landroid/ranging/uwb/UwbRangingParams$Builder;")
        setSlotDuration = JavaMethod("(I)Landroid/ranging/uwb/UwbRangingParams$Builder;")
        setSubSessionKeyInfo = JavaMethod("([B)Landroid/ranging/uwb/UwbRangingParams$Builder;")
        build = JavaMethod("()Landroid/ranging/uwb/UwbRangingParams;")