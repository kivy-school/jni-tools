from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PreferentialNetworkServiceConfig"]

class PreferentialNetworkServiceConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/admin/PreferentialNetworkServiceConfig"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    PREFERENTIAL_NETWORK_ID_1 = JavaStaticField("I")
    PREFERENTIAL_NETWORK_ID_2 = JavaStaticField("I")
    PREFERENTIAL_NETWORK_ID_3 = JavaStaticField("I")
    PREFERENTIAL_NETWORK_ID_4 = JavaStaticField("I")
    PREFERENTIAL_NETWORK_ID_5 = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    isEnabled = JavaMethod("()Z")
    getNetworkId = JavaMethod("()I")
    getIncludedUids = JavaMethod("()[I")
    isFallbackToDefaultConnectionAllowed = JavaMethod("()Z")
    shouldBlockNonMatchingNetworks = JavaMethod("()Z")
    getExcludedUids = JavaMethod("()[I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/admin/PreferentialNetworkServiceConfig$Builder"
        __javaconstructor__ = [("()V", False)]
        setIncludedUids = JavaMethod("([I)Landroid/app/admin/PreferentialNetworkServiceConfig$Builder;")
        setNetworkId = JavaMethod("(I)Landroid/app/admin/PreferentialNetworkServiceConfig$Builder;")
        setExcludedUids = JavaMethod("([I)Landroid/app/admin/PreferentialNetworkServiceConfig$Builder;")
        setFallbackToDefaultConnectionAllowed = JavaMethod("(Z)Landroid/app/admin/PreferentialNetworkServiceConfig$Builder;")
        setShouldBlockNonMatchingNetworks = JavaMethod("(Z)Landroid/app/admin/PreferentialNetworkServiceConfig$Builder;")
        setEnabled = JavaMethod("(Z)Landroid/app/admin/PreferentialNetworkServiceConfig$Builder;")
        build = JavaMethod("()Landroid/app/admin/PreferentialNetworkServiceConfig;")