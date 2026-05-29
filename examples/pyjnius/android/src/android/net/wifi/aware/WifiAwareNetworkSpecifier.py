from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WifiAwareNetworkSpecifier"]

class WifiAwareNetworkSpecifier(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/aware/WifiAwareNetworkSpecifier"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getChannelFrequencyMhz = JavaMethod("()I")
    isChannelRequired = JavaMethod("()Z")
    getWifiAwareDataPathSecurityConfig = JavaMethod("()Landroid/net/wifi/aware/WifiAwareDataPathSecurityConfig;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    canBeSatisfiedBy = JavaMethod("(Landroid/net/NetworkSpecifier;)Z")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/wifi/aware/WifiAwareNetworkSpecifier/Builder"
        __javaconstructor__ = [("(Landroid/net/wifi/aware/DiscoverySession;Landroid/net/wifi/aware/PeerHandle;)V", False), ("(Landroid/net/wifi/aware/PublishDiscoverySession;)V", False)]
        setPskPassphrase = JavaMethod("(Ljava/lang/String;)Landroid/net/wifi/aware/WifiAwareNetworkSpecifier$Builder;")
        setPmk = JavaMethod("([B)Landroid/net/wifi/aware/WifiAwareNetworkSpecifier$Builder;")
        setPort = JavaMethod("(I)Landroid/net/wifi/aware/WifiAwareNetworkSpecifier$Builder;")
        setTransportProtocol = JavaMethod("(I)Landroid/net/wifi/aware/WifiAwareNetworkSpecifier$Builder;")
        setChannelFrequencyMhz = JavaMethod("(IZ)Landroid/net/wifi/aware/WifiAwareNetworkSpecifier$Builder;")
        setDataPathSecurityConfig = JavaMethod("(Landroid/net/wifi/aware/WifiAwareDataPathSecurityConfig;)Landroid/net/wifi/aware/WifiAwareNetworkSpecifier$Builder;")
        build = JavaMethod("()Landroid/net/wifi/aware/WifiAwareNetworkSpecifier;")