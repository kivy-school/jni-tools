from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SubscribeConfig"]

class SubscribeConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/aware/SubscribeConfig"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    SUBSCRIBE_TYPE_ACTIVE = JavaStaticField("I")
    SUBSCRIBE_TYPE_PASSIVE = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getInstantCommunicationBand = JavaMethod("()I")
    isInstantCommunicationModeEnabled = JavaMethod("()Z")
    getPairingConfig = JavaMethod("()Landroid/net/wifi/aware/AwarePairingConfig;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/wifi/aware/SubscribeConfig$Builder"
        __javaconstructor__ = [("()V", False)]
        setPairingConfig = JavaMethod("(Landroid/net/wifi/aware/AwarePairingConfig;)Landroid/net/wifi/aware/SubscribeConfig$Builder;")
        setMaxDistanceMm = JavaMethod("(I)Landroid/net/wifi/aware/SubscribeConfig$Builder;")
        setMinDistanceMm = JavaMethod("(I)Landroid/net/wifi/aware/SubscribeConfig$Builder;")
        setSubscribeType = JavaMethod("(I)Landroid/net/wifi/aware/SubscribeConfig$Builder;")
        setTtlSec = JavaMethod("(I)Landroid/net/wifi/aware/SubscribeConfig$Builder;")
        setServiceName = JavaMethod("(Ljava/lang/String;)Landroid/net/wifi/aware/SubscribeConfig$Builder;")
        setInstantCommunicationModeEnabled = JavaMethod("(ZI)Landroid/net/wifi/aware/SubscribeConfig$Builder;")
        setTerminateNotificationEnabled = JavaMethod("(Z)Landroid/net/wifi/aware/SubscribeConfig$Builder;")
        setServiceSpecificInfo = JavaMethod("([B)Landroid/net/wifi/aware/SubscribeConfig$Builder;")
        setMatchFilter = JavaMethod("(Ljava/util/List;)Landroid/net/wifi/aware/SubscribeConfig$Builder;")
        build = JavaMethod("()Landroid/net/wifi/aware/SubscribeConfig;")