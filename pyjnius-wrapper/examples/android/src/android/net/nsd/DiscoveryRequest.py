from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DiscoveryRequest"]

class DiscoveryRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/nsd/DiscoveryRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getServiceType = JavaMethod("()Ljava/lang/String;")
    getSubtype = JavaMethod("()Ljava/lang/String;")
    getNetwork = JavaMethod("()Landroid/net/Network;")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/nsd/DiscoveryRequest/Builder"
        __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
        setSubtype = JavaMethod("(Ljava/lang/String;)Landroid/net/nsd/DiscoveryRequest$Builder;")
        setNetwork = JavaMethod("(Landroid/net/Network;)Landroid/net/nsd/DiscoveryRequest$Builder;")
        build = JavaMethod("()Landroid/net/nsd/DiscoveryRequest;")