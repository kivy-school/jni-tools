from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NetworkRequest"]

class NetworkRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/NetworkRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getNetworkSpecifier = JavaMethod("()Landroid/net/NetworkSpecifier;")
    getSubscriptionIds = JavaMethod("()Ljava/util/Set;")
    hasCapability = JavaMethod("(I)Z")
    hasTransport = JavaMethod("(I)Z")
    canBeSatisfiedBy = JavaMethod("(Landroid/net/NetworkCapabilities;)Z")
    getTransportTypes = JavaMethod("()[I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getCapabilities = JavaMethod("()[I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/NetworkRequest$Builder"
        __javaconstructor__ = [("()V", False), ("(Landroid/net/NetworkRequest;)V", False)]
        setSubscriptionIds = JavaMethod("(Ljava/util/Set;)Landroid/net/NetworkRequest$Builder;")
        removeCapability = JavaMethod("(I)Landroid/net/NetworkRequest$Builder;")
        addCapability = JavaMethod("(I)Landroid/net/NetworkRequest$Builder;")
        addTransportType = JavaMethod("(I)Landroid/net/NetworkRequest$Builder;")
        clearCapabilities = JavaMethod("()Landroid/net/NetworkRequest$Builder;")
        removeTransportType = JavaMethod("(I)Landroid/net/NetworkRequest$Builder;")
        setIncludeOtherUidNetworks = JavaMethod("(Z)Landroid/net/NetworkRequest$Builder;")
        setNetworkSpecifier = JavaMultipleMethod([("(Ljava/lang/String;)Landroid/net/NetworkRequest$Builder;", False, False), ("(Landroid/net/NetworkSpecifier;)Landroid/net/NetworkRequest$Builder;", False, False)])
        build = JavaMethod("()Landroid/net/NetworkRequest;")