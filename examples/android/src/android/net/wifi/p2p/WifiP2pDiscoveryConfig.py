from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WifiP2pDiscoveryConfig"]

class WifiP2pDiscoveryConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/p2p/WifiP2pDiscoveryConfig"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getScanType = JavaMethod("()I")
    getFrequencyMhz = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/wifi/p2p/WifiP2pDiscoveryConfig/Builder"
        __javaconstructor__ = [("(I)V", False)]
        setFrequencyMhz = JavaMethod("(I)Landroid/net/wifi/p2p/WifiP2pDiscoveryConfig$Builder;")
        build = JavaMethod("()Landroid/net/wifi/p2p/WifiP2pDiscoveryConfig;")