from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WifiP2pServiceInfo"]

class WifiP2pServiceInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/p2p/nsd/WifiP2pServiceInfo"
    SERVICE_TYPE_ALL = JavaStaticField("I")
    SERVICE_TYPE_BONJOUR = JavaStaticField("I")
    SERVICE_TYPE_UPNP = JavaStaticField("I")
    SERVICE_TYPE_VENDOR_SPECIFIC = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")