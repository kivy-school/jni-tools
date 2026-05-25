from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SubscribeConfig"]

class SubscribeConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/aware/SubscribeConfig"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    SUBSCRIBE_TYPE_ACTIVE = JavaStaticField("I")
    SUBSCRIBE_TYPE_PASSIVE = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    isInstantCommunicationModeEnabled = JavaMethod("()Z")
    getInstantCommunicationBand = JavaMethod("()I")
    getPairingConfig = JavaMethod("()Landroid/net/wifi/aware/AwarePairingConfig;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/wifi/aware/SubscribeConfig/Builder"
        __javaconstructor__ = [("()V", False)]
        setServiceName = JavaMethod("(Ljava/lang/String;)Landroid/net/wifi/aware/SubscribeConfig$Builder;")
        setServiceSpecificInfo = JavaMethod("([B)Landroid/net/wifi/aware/SubscribeConfig$Builder;")
        setMatchFilter = JavaMethod("(Ljava/util/List;)Landroid/net/wifi/aware/SubscribeConfig$Builder;")
        setSubscribeType = JavaMethod("(I)Landroid/net/wifi/aware/SubscribeConfig$Builder;")
        setTtlSec = JavaMethod("(I)Landroid/net/wifi/aware/SubscribeConfig$Builder;")
        setTerminateNotificationEnabled = JavaMethod("(Z)Landroid/net/wifi/aware/SubscribeConfig$Builder;")
        setMinDistanceMm = JavaMethod("(I)Landroid/net/wifi/aware/SubscribeConfig$Builder;")
        setMaxDistanceMm = JavaMethod("(I)Landroid/net/wifi/aware/SubscribeConfig$Builder;")
        setInstantCommunicationModeEnabled = JavaMethod("(ZI)Landroid/net/wifi/aware/SubscribeConfig$Builder;")
        setPairingConfig = JavaMethod("(Landroid/net/wifi/aware/AwarePairingConfig;)Landroid/net/wifi/aware/SubscribeConfig$Builder;")
        build = JavaMethod("()Landroid/net/wifi/aware/SubscribeConfig;")