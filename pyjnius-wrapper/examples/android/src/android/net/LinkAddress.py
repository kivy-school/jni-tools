from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LinkAddress"]

class LinkAddress(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/LinkAddress"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getAddress = JavaMethod("()Ljava/net/InetAddress;")
    getPrefixLength = JavaMethod("()I")
    getFlags = JavaMethod("()I")
    getScope = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")