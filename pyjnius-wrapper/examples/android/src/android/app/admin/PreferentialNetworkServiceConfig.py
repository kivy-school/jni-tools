from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PreferentialNetworkServiceConfig"]

class PreferentialNetworkServiceConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/admin/PreferentialNetworkServiceConfig"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    PREFERENTIAL_NETWORK_ID_1 = JavaStaticField("I")
    PREFERENTIAL_NETWORK_ID_2 = JavaStaticField("I")
    PREFERENTIAL_NETWORK_ID_3 = JavaStaticField("I")
    PREFERENTIAL_NETWORK_ID_4 = JavaStaticField("I")
    PREFERENTIAL_NETWORK_ID_5 = JavaStaticField("I")
    isEnabled = JavaMethod("()Z")
    isFallbackToDefaultConnectionAllowed = JavaMethod("()Z")
    shouldBlockNonMatchingNetworks = JavaMethod("()Z")
    getIncludedUids = JavaMethod("()[I")
    getExcludedUids = JavaMethod("()[I")
    getNetworkId = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/admin/PreferentialNetworkServiceConfig/Builder"
        __javaconstructor__ = [("()V", False)]
        setEnabled = JavaMethod("(Z)Landroid/app/admin/PreferentialNetworkServiceConfig$Builder;")
        setFallbackToDefaultConnectionAllowed = JavaMethod("(Z)Landroid/app/admin/PreferentialNetworkServiceConfig$Builder;")
        setShouldBlockNonMatchingNetworks = JavaMethod("(Z)Landroid/app/admin/PreferentialNetworkServiceConfig$Builder;")
        setIncludedUids = JavaMethod("([I)Landroid/app/admin/PreferentialNetworkServiceConfig$Builder;")
        setExcludedUids = JavaMethod("([I)Landroid/app/admin/PreferentialNetworkServiceConfig$Builder;")
        build = JavaMethod("()Landroid/app/admin/PreferentialNetworkServiceConfig;")
        setNetworkId = JavaMethod("(I)Landroid/app/admin/PreferentialNetworkServiceConfig$Builder;")