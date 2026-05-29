from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MacAddress"]

class MacAddress(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/MacAddress"
    BROADCAST_ADDRESS = JavaStaticField("Landroid/net/MacAddress;")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    TYPE_BROADCAST = JavaStaticField("I")
    TYPE_MULTICAST = JavaStaticField("I")
    TYPE_UNICAST = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getLinkLocalIpv6FromEui48Mac = JavaMethod("()Ljava/net/Inet6Address;")
    isLocallyAssigned = JavaMethod("()Z")
    toOuiString = JavaMethod("()Ljava/lang/String;")
    getAddressType = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    matches = JavaMethod("(Landroid/net/MacAddress;Landroid/net/MacAddress;)Z")
    fromBytes = JavaStaticMethod("([B)Landroid/net/MacAddress;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    toByteArray = JavaMethod("()[B")
    fromString = JavaStaticMethod("(Ljava/lang/String;)Landroid/net/MacAddress;")