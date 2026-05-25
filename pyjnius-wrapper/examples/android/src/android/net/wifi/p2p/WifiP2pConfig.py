from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WifiP2pConfig"]

class WifiP2pConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/p2p/WifiP2pConfig"
    __javaconstructor__ = [("()V", False), ("(Landroid/net/wifi/p2p/WifiP2pConfig;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    GROUP_CLIENT_IP_PROVISIONING_MODE_IPV4_DHCP = JavaStaticField("I")
    GROUP_CLIENT_IP_PROVISIONING_MODE_IPV6_LINK_LOCAL = JavaStaticField("I")
    GROUP_OWNER_BAND_2GHZ = JavaStaticField("I")
    GROUP_OWNER_BAND_5GHZ = JavaStaticField("I")
    GROUP_OWNER_BAND_AUTO = JavaStaticField("I")
    GROUP_OWNER_INTENT_AUTO = JavaStaticField("I")
    GROUP_OWNER_INTENT_MAX = JavaStaticField("I")
    GROUP_OWNER_INTENT_MIN = JavaStaticField("I")
    deviceAddress = JavaField("Ljava/lang/String;")
    groupOwnerIntent = JavaField("I")
    wps = JavaField("Landroid/net/wifi/WpsInfo;")
    getNetworkName = JavaMethod("()Ljava/lang/String;")
    getPassphrase = JavaMethod("()Ljava/lang/String;")
    getGroupOwnerBand = JavaMethod("()I")
    getNetworkId = JavaMethod("()I")
    getGroupClientIpProvisioningMode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/wifi/p2p/WifiP2pConfig/Builder"
        __javaconstructor__ = [("()V", False)]
        setDeviceAddress = JavaMethod("(Landroid/net/MacAddress;)Landroid/net/wifi/p2p/WifiP2pConfig$Builder;")
        setNetworkName = JavaMethod("(Ljava/lang/String;)Landroid/net/wifi/p2p/WifiP2pConfig$Builder;")
        setPassphrase = JavaMethod("(Ljava/lang/String;)Landroid/net/wifi/p2p/WifiP2pConfig$Builder;")
        setGroupOperatingBand = JavaMethod("(I)Landroid/net/wifi/p2p/WifiP2pConfig$Builder;")
        setGroupOperatingFrequency = JavaMethod("(I)Landroid/net/wifi/p2p/WifiP2pConfig$Builder;")
        enablePersistentMode = JavaMethod("(Z)Landroid/net/wifi/p2p/WifiP2pConfig$Builder;")
        setGroupClientIpProvisioningMode = JavaMethod("(I)Landroid/net/wifi/p2p/WifiP2pConfig$Builder;")
        build = JavaMethod("()Landroid/net/wifi/p2p/WifiP2pConfig;")