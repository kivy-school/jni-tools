from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IpPrefix"]

class IpPrefix(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/IpPrefix"
    __javaconstructor__ = [("(Ljava/net/InetAddress;I)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getAddress = JavaMethod("()Ljava/net/InetAddress;")
    getRawAddress = JavaMethod("()[B")
    getPrefixLength = JavaMethod("()I")
    contains = JavaMethod("(Ljava/net/InetAddress;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")