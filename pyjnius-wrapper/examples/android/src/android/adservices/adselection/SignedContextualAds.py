from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SignedContextualAds"]

class SignedContextualAds(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/adselection/SignedContextualAds"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getBuyer = JavaMethod("()Landroid/adservices/common/AdTechIdentifier;")
    getDecisionLogicUri = JavaMethod("()Landroid/net/Uri;")
    getAdsWithBid = JavaMethod("()Ljava/util/List;")
    getSignature = JavaMethod("()[B")
    toString = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/adselection/SignedContextualAds/Builder"
        __javaconstructor__ = [("()V", False), ("(Landroid/adservices/adselection/SignedContextualAds;)V", False)]
        setBuyer = JavaMethod("(Landroid/adservices/common/AdTechIdentifier;)Landroid/adservices/adselection/SignedContextualAds$Builder;")
        setDecisionLogicUri = JavaMethod("(Landroid/net/Uri;)Landroid/adservices/adselection/SignedContextualAds$Builder;")
        setAdsWithBid = JavaMethod("(Ljava/util/List;)Landroid/adservices/adselection/SignedContextualAds$Builder;")
        setSignature = JavaMethod("([B)Landroid/adservices/adselection/SignedContextualAds$Builder;")
        build = JavaMethod("()Landroid/adservices/adselection/SignedContextualAds;")