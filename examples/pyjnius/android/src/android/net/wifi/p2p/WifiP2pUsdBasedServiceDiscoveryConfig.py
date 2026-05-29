from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WifiP2pUsdBasedServiceDiscoveryConfig"]

class WifiP2pUsdBasedServiceDiscoveryConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/p2p/WifiP2pUsdBasedServiceDiscoveryConfig"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getBand = JavaMethod("()I")
    getFrequenciesMhz = JavaMethod("()[I")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/wifi/p2p/WifiP2pUsdBasedServiceDiscoveryConfig$Builder"
        __javaconstructor__ = [("()V", False)]
        setBand = JavaMethod("(I)Landroid/net/wifi/p2p/WifiP2pUsdBasedServiceDiscoveryConfig$Builder;")
        setFrequenciesMhz = JavaMethod("([I)Landroid/net/wifi/p2p/WifiP2pUsdBasedServiceDiscoveryConfig$Builder;")
        build = JavaMethod("()Landroid/net/wifi/p2p/WifiP2pUsdBasedServiceDiscoveryConfig;")