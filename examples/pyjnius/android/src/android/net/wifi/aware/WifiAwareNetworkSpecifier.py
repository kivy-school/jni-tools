from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WifiAwareNetworkSpecifier"]

class WifiAwareNetworkSpecifier(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/aware/WifiAwareNetworkSpecifier"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    isChannelRequired = JavaMethod("()Z")
    getChannelFrequencyMhz = JavaMethod("()I")
    getWifiAwareDataPathSecurityConfig = JavaMethod("()Landroid/net/wifi/aware/WifiAwareDataPathSecurityConfig;")
    canBeSatisfiedBy = JavaMethod("(Landroid/net/NetworkSpecifier;)Z")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/wifi/aware/WifiAwareNetworkSpecifier$Builder"
        __javaconstructor__ = [("(Landroid/net/wifi/aware/DiscoverySession;Landroid/net/wifi/aware/PeerHandle;)V", False), ("(Landroid/net/wifi/aware/PublishDiscoverySession;)V", False)]
        setPort = JavaMethod("(I)Landroid/net/wifi/aware/WifiAwareNetworkSpecifier$Builder;")
        setChannelFrequencyMhz = JavaMethod("(IZ)Landroid/net/wifi/aware/WifiAwareNetworkSpecifier$Builder;")
        setDataPathSecurityConfig = JavaMethod("(Landroid/net/wifi/aware/WifiAwareDataPathSecurityConfig;)Landroid/net/wifi/aware/WifiAwareNetworkSpecifier$Builder;")
        setPmk = JavaMethod("([B)Landroid/net/wifi/aware/WifiAwareNetworkSpecifier$Builder;")
        setPskPassphrase = JavaMethod("(Ljava/lang/String;)Landroid/net/wifi/aware/WifiAwareNetworkSpecifier$Builder;")
        setTransportProtocol = JavaMethod("(I)Landroid/net/wifi/aware/WifiAwareNetworkSpecifier$Builder;")
        build = JavaMethod("()Landroid/net/wifi/aware/WifiAwareNetworkSpecifier;")