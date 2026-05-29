from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IpPrefix"]

class IpPrefix(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/IpPrefix"
    __javaconstructor__ = [("(Ljava/net/InetAddress;I)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getRawAddress = JavaMethod("()[B")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    contains = JavaMethod("(Ljava/net/InetAddress;)Z")
    getAddress = JavaMethod("()Ljava/net/InetAddress;")
    getPrefixLength = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")