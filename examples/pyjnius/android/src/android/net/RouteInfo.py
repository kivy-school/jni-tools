from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RouteInfo"]

class RouteInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/RouteInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    RTN_THROW = JavaStaticField("I")
    RTN_UNICAST = JavaStaticField("I")
    RTN_UNREACHABLE = JavaStaticField("I")
    getDestination = JavaMethod("()Landroid/net/IpPrefix;")
    getGateway = JavaMethod("()Ljava/net/InetAddress;")
    getInterface = JavaMethod("()Ljava/lang/String;")
    getType = JavaMethod("()I")
    isDefaultRoute = JavaMethod("()Z")
    hasGateway = JavaMethod("()Z")
    matches = JavaMethod("(Ljava/net/InetAddress;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")