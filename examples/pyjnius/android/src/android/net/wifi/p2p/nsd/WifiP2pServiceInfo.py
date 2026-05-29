from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WifiP2pServiceInfo"]

class WifiP2pServiceInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/p2p/nsd/WifiP2pServiceInfo"
    __javaconstructor__ = [("(Landroid/net/wifi/p2p/nsd/WifiP2pUsdBasedServiceConfig;)V", False)]
    SERVICE_TYPE_ALL = JavaStaticField("I")
    SERVICE_TYPE_BONJOUR = JavaStaticField("I")
    SERVICE_TYPE_UPNP = JavaStaticField("I")
    SERVICE_TYPE_VENDOR_SPECIFIC = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getWifiP2pUsdBasedServiceConfig = JavaMethod("()Landroid/net/wifi/p2p/nsd/WifiP2pUsdBasedServiceConfig;")