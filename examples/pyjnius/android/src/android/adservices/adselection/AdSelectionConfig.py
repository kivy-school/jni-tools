from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdSelectionConfig"]

class AdSelectionConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/adselection/AdSelectionConfig"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getAdSelectionSignals = JavaMethod("()Landroid/adservices/common/AdSelectionSignals;")
    getCustomAudienceBuyers = JavaMethod("()Ljava/util/List;")
    getDecisionLogicUri = JavaMethod("()Landroid/net/Uri;")
    getPerBuyerSignals = JavaMethod("()Ljava/util/Map;")
    getSeller = JavaMethod("()Landroid/adservices/common/AdTechIdentifier;")
    getPerBuyerSignedContextualAds = JavaMethod("()Ljava/util/Map;")
    getSellerSignals = JavaMethod("()Landroid/adservices/common/AdSelectionSignals;")
    getTrustedScoringSignalsUri = JavaMethod("()Landroid/net/Uri;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/adselection/AdSelectionConfig$Builder"
        __javaconstructor__ = [("()V", False)]
        setCustomAudienceBuyers = JavaMethod("(Ljava/util/List;)Landroid/adservices/adselection/AdSelectionConfig$Builder;")
        setAdSelectionSignals = JavaMethod("(Landroid/adservices/common/AdSelectionSignals;)Landroid/adservices/adselection/AdSelectionConfig$Builder;")
        setDecisionLogicUri = JavaMethod("(Landroid/net/Uri;)Landroid/adservices/adselection/AdSelectionConfig$Builder;")
        setPerBuyerSignals = JavaMethod("(Ljava/util/Map;)Landroid/adservices/adselection/AdSelectionConfig$Builder;")
        setPerBuyerSignedContextualAds = JavaMethod("(Ljava/util/Map;)Landroid/adservices/adselection/AdSelectionConfig$Builder;")
        setSeller = JavaMethod("(Landroid/adservices/common/AdTechIdentifier;)Landroid/adservices/adselection/AdSelectionConfig$Builder;")
        setSellerSignals = JavaMethod("(Landroid/adservices/common/AdSelectionSignals;)Landroid/adservices/adselection/AdSelectionConfig$Builder;")
        setTrustedScoringSignalsUri = JavaMethod("(Landroid/net/Uri;)Landroid/adservices/adselection/AdSelectionConfig$Builder;")
        build = JavaMethod("()Landroid/adservices/adselection/AdSelectionConfig;")