from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NetworkRequest"]

class NetworkRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/NetworkRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    hasCapability = JavaMethod("(I)Z")
    canBeSatisfiedBy = JavaMethod("(Landroid/net/NetworkCapabilities;)Z")
    hasTransport = JavaMethod("(I)Z")
    getNetworkSpecifier = JavaMethod("()Landroid/net/NetworkSpecifier;")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getCapabilities = JavaMethod("()[I")
    getTransportTypes = JavaMethod("()[I")
    getSubscriptionIds = JavaMethod("()Ljava/util/Set;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/NetworkRequest/Builder"
        __javaconstructor__ = [("()V", False), ("(Landroid/net/NetworkRequest;)V", False)]
        build = JavaMethod("()Landroid/net/NetworkRequest;")
        addCapability = JavaMethod("(I)Landroid/net/NetworkRequest$Builder;")
        removeCapability = JavaMethod("(I)Landroid/net/NetworkRequest$Builder;")
        clearCapabilities = JavaMethod("()Landroid/net/NetworkRequest$Builder;")
        addTransportType = JavaMethod("(I)Landroid/net/NetworkRequest$Builder;")
        removeTransportType = JavaMethod("(I)Landroid/net/NetworkRequest$Builder;")
        setNetworkSpecifier = JavaMultipleMethod([("(Ljava/lang/String;)Landroid/net/NetworkRequest$Builder;", False, False), ("(Landroid/net/NetworkSpecifier;)Landroid/net/NetworkRequest$Builder;", False, False)])
        setSubscriptionIds = JavaMethod("(Ljava/util/Set;)Landroid/net/NetworkRequest$Builder;")
        setIncludeOtherUidNetworks = JavaMethod("(Z)Landroid/net/NetworkRequest$Builder;")