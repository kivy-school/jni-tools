from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MacAddress"]

class MacAddress(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/MacAddress"
    BROADCAST_ADDRESS = JavaStaticField("Landroid/net/MacAddress;")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    TYPE_BROADCAST = JavaStaticField("I")
    TYPE_MULTICAST = JavaStaticField("I")
    TYPE_UNICAST = JavaStaticField("I")
    getAddressType = JavaMethod("()I")
    isLocallyAssigned = JavaMethod("()Z")
    toByteArray = JavaMethod("()[B")
    toString = JavaMethod("()Ljava/lang/String;")
    toOuiString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    fromString = JavaStaticMethod("(Ljava/lang/String;)Landroid/net/MacAddress;")
    fromBytes = JavaStaticMethod("([B)Landroid/net/MacAddress;")
    matches = JavaMethod("(Landroid/net/MacAddress;Landroid/net/MacAddress;)Z")
    getLinkLocalIpv6FromEui48Mac = JavaMethod("()Ljava/net/Inet6Address;")