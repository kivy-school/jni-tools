from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PublishConfig"]

class PublishConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/aware/PublishConfig"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    PUBLISH_TYPE_SOLICITED = JavaStaticField("I")
    PUBLISH_TYPE_UNSOLICITED = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    isInstantCommunicationModeEnabled = JavaMethod("()Z")
    getInstantCommunicationBand = JavaMethod("()I")
    getSecurityConfig = JavaMethod("()Landroid/net/wifi/aware/WifiAwareDataPathSecurityConfig;")
    getPairingConfig = JavaMethod("()Landroid/net/wifi/aware/AwarePairingConfig;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/wifi/aware/PublishConfig/Builder"
        __javaconstructor__ = [("()V", False)]
        setServiceName = JavaMethod("(Ljava/lang/String;)Landroid/net/wifi/aware/PublishConfig$Builder;")
        setServiceSpecificInfo = JavaMethod("([B)Landroid/net/wifi/aware/PublishConfig$Builder;")
        setMatchFilter = JavaMethod("(Ljava/util/List;)Landroid/net/wifi/aware/PublishConfig$Builder;")
        setPublishType = JavaMethod("(I)Landroid/net/wifi/aware/PublishConfig$Builder;")
        setTtlSec = JavaMethod("(I)Landroid/net/wifi/aware/PublishConfig$Builder;")
        setTerminateNotificationEnabled = JavaMethod("(Z)Landroid/net/wifi/aware/PublishConfig$Builder;")
        setRangingEnabled = JavaMethod("(Z)Landroid/net/wifi/aware/PublishConfig$Builder;")
        setInstantCommunicationModeEnabled = JavaMethod("(ZI)Landroid/net/wifi/aware/PublishConfig$Builder;")
        setDataPathSecurityConfig = JavaMethod("(Landroid/net/wifi/aware/WifiAwareDataPathSecurityConfig;)Landroid/net/wifi/aware/PublishConfig$Builder;")
        setPairingConfig = JavaMethod("(Landroid/net/wifi/aware/AwarePairingConfig;)Landroid/net/wifi/aware/PublishConfig$Builder;")
        build = JavaMethod("()Landroid/net/wifi/aware/PublishConfig;")