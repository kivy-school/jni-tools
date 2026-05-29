from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SignedContextualAds"]

class SignedContextualAds(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/adselection/SignedContextualAds"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getDecisionLogicUri = JavaMethod("()Landroid/net/Uri;")
    getBuyer = JavaMethod("()Landroid/adservices/common/AdTechIdentifier;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getSignature = JavaMethod("()[B")
    getAdsWithBid = JavaMethod("()Ljava/util/List;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/adselection/SignedContextualAds$Builder"
        __javaconstructor__ = [("(Landroid/adservices/adselection/SignedContextualAds;)V", False), ("()V", False)]
        setBuyer = JavaMethod("(Landroid/adservices/common/AdTechIdentifier;)Landroid/adservices/adselection/SignedContextualAds$Builder;")
        setDecisionLogicUri = JavaMethod("(Landroid/net/Uri;)Landroid/adservices/adselection/SignedContextualAds$Builder;")
        setSignature = JavaMethod("([B)Landroid/adservices/adselection/SignedContextualAds$Builder;")
        setAdsWithBid = JavaMethod("(Ljava/util/List;)Landroid/adservices/adselection/SignedContextualAds$Builder;")
        build = JavaMethod("()Landroid/adservices/adselection/SignedContextualAds;")