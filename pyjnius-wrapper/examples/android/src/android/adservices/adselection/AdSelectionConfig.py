from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdSelectionConfig"]

class AdSelectionConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/adselection/AdSelectionConfig"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getSeller = JavaMethod("()Landroid/adservices/common/AdTechIdentifier;")
    getDecisionLogicUri = JavaMethod("()Landroid/net/Uri;")
    getCustomAudienceBuyers = JavaMethod("()Ljava/util/List;")
    getAdSelectionSignals = JavaMethod("()Landroid/adservices/common/AdSelectionSignals;")
    getSellerSignals = JavaMethod("()Landroid/adservices/common/AdSelectionSignals;")
    getPerBuyerSignals = JavaMethod("()Ljava/util/Map;")
    getPerBuyerSignedContextualAds = JavaMethod("()Ljava/util/Map;")
    getTrustedScoringSignalsUri = JavaMethod("()Landroid/net/Uri;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/adselection/AdSelectionConfig/Builder"
        __javaconstructor__ = [("()V", False)]
        setSeller = JavaMethod("(Landroid/adservices/common/AdTechIdentifier;)Landroid/adservices/adselection/AdSelectionConfig$Builder;")
        setDecisionLogicUri = JavaMethod("(Landroid/net/Uri;)Landroid/adservices/adselection/AdSelectionConfig$Builder;")
        setCustomAudienceBuyers = JavaMethod("(Ljava/util/List;)Landroid/adservices/adselection/AdSelectionConfig$Builder;")
        setAdSelectionSignals = JavaMethod("(Landroid/adservices/common/AdSelectionSignals;)Landroid/adservices/adselection/AdSelectionConfig$Builder;")
        setSellerSignals = JavaMethod("(Landroid/adservices/common/AdSelectionSignals;)Landroid/adservices/adselection/AdSelectionConfig$Builder;")
        setPerBuyerSignals = JavaMethod("(Ljava/util/Map;)Landroid/adservices/adselection/AdSelectionConfig$Builder;")
        setPerBuyerSignedContextualAds = JavaMethod("(Ljava/util/Map;)Landroid/adservices/adselection/AdSelectionConfig$Builder;")
        setTrustedScoringSignalsUri = JavaMethod("(Landroid/net/Uri;)Landroid/adservices/adselection/AdSelectionConfig$Builder;")
        build = JavaMethod("()Landroid/adservices/adselection/AdSelectionConfig;")