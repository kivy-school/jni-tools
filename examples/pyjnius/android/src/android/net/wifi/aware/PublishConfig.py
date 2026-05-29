from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PublishConfig"]

class PublishConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/aware/PublishConfig"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    PUBLISH_TYPE_SOLICITED = JavaStaticField("I")
    PUBLISH_TYPE_UNSOLICITED = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getInstantCommunicationBand = JavaMethod("()I")
    isInstantCommunicationModeEnabled = JavaMethod("()Z")
    getPairingConfig = JavaMethod("()Landroid/net/wifi/aware/AwarePairingConfig;")
    getSecurityConfig = JavaMethod("()Landroid/net/wifi/aware/WifiAwareDataPathSecurityConfig;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/wifi/aware/PublishConfig$Builder"
        __javaconstructor__ = [("()V", False)]
        setPublishType = JavaMethod("(I)Landroid/net/wifi/aware/PublishConfig$Builder;")
        setPairingConfig = JavaMethod("(Landroid/net/wifi/aware/AwarePairingConfig;)Landroid/net/wifi/aware/PublishConfig$Builder;")
        setDataPathSecurityConfig = JavaMethod("(Landroid/net/wifi/aware/WifiAwareDataPathSecurityConfig;)Landroid/net/wifi/aware/PublishConfig$Builder;")
        setRangingEnabled = JavaMethod("(Z)Landroid/net/wifi/aware/PublishConfig$Builder;")
        setTtlSec = JavaMethod("(I)Landroid/net/wifi/aware/PublishConfig$Builder;")
        setServiceName = JavaMethod("(Ljava/lang/String;)Landroid/net/wifi/aware/PublishConfig$Builder;")
        setInstantCommunicationModeEnabled = JavaMethod("(ZI)Landroid/net/wifi/aware/PublishConfig$Builder;")
        setTerminateNotificationEnabled = JavaMethod("(Z)Landroid/net/wifi/aware/PublishConfig$Builder;")
        setServiceSpecificInfo = JavaMethod("([B)Landroid/net/wifi/aware/PublishConfig$Builder;")
        setMatchFilter = JavaMethod("(Ljava/util/List;)Landroid/net/wifi/aware/PublishConfig$Builder;")
        build = JavaMethod("()Landroid/net/wifi/aware/PublishConfig;")