from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WifiAwareNetworkInfo"]

class WifiAwareNetworkInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/aware/WifiAwareNetworkInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getPeerIpv6Addr = JavaMethod("()Ljava/net/Inet6Address;")
    getPort = JavaMethod("()I")
    getTransportProtocol = JavaMethod("()I")
    getChannelInfoList = JavaMethod("()Ljava/util/List;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")