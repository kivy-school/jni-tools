from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RouteInfo"]

class RouteInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/RouteInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    RTN_THROW = JavaStaticField("I")
    RTN_UNICAST = JavaStaticField("I")
    RTN_UNREACHABLE = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getDestination = JavaMethod("()Landroid/net/IpPrefix;")
    getGateway = JavaMethod("()Ljava/net/InetAddress;")
    hasGateway = JavaMethod("()Z")
    isDefaultRoute = JavaMethod("()Z")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    matches = JavaMethod("(Ljava/net/InetAddress;)Z")
    getType = JavaMethod("()I")
    getInterface = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")