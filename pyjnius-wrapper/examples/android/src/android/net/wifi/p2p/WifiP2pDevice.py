from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WifiP2pDevice"]

class WifiP2pDevice(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/p2p/WifiP2pDevice"
    __javaconstructor__ = [("()V", False), ("(Landroid/net/wifi/p2p/WifiP2pDevice;)V", False)]
    AVAILABLE = JavaStaticField("I")
    CONNECTED = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    FAILED = JavaStaticField("I")
    INVITED = JavaStaticField("I")
    UNAVAILABLE = JavaStaticField("I")
    deviceAddress = JavaField("Ljava/lang/String;")
    deviceName = JavaField("Ljava/lang/String;")
    primaryDeviceType = JavaField("Ljava/lang/String;")
    secondaryDeviceType = JavaField("Ljava/lang/String;")
    status = JavaField("I")
    getWfdInfo = JavaMethod("()Landroid/net/wifi/p2p/WifiP2pWfdInfo;")
    wpsPbcSupported = JavaMethod("()Z")
    wpsKeypadSupported = JavaMethod("()Z")
    wpsDisplaySupported = JavaMethod("()Z")
    isServiceDiscoveryCapable = JavaMethod("()Z")
    isGroupOwner = JavaMethod("()Z")
    update = JavaMethod("(Landroid/net/wifi/p2p/WifiP2pDevice;)V")
    getVendorElements = JavaMethod("()Ljava/util/List;")
    getIpAddress = JavaMethod("()Ljava/net/InetAddress;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")