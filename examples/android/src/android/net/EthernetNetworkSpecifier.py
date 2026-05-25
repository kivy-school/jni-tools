from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EthernetNetworkSpecifier"]

class EthernetNetworkSpecifier(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/EthernetNetworkSpecifier"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getInterfaceName = JavaMethod("()Ljava/lang/String;")
    canBeSatisfiedBy = JavaMethod("(Landroid/net/NetworkSpecifier;)Z")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")