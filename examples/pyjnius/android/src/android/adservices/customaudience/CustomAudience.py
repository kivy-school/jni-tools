from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CustomAudience"]

class CustomAudience(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/customaudience/CustomAudience"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    FLAG_AUCTION_SERVER_REQUEST_OMIT_ADS = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getBuyer = JavaMethod("()Landroid/adservices/common/AdTechIdentifier;")
    getActivationTime = JavaMethod("()Ljava/time/Instant;")
    getBiddingLogicUri = JavaMethod("()Landroid/net/Uri;")
    getExpirationTime = JavaMethod("()Ljava/time/Instant;")
    getUserBiddingSignals = JavaMethod("()Landroid/adservices/common/AdSelectionSignals;")
    getDailyUpdateUri = JavaMethod("()Landroid/net/Uri;")
    getComponentAds = JavaMethod("()Ljava/util/List;")
    getAds = JavaMethod("()Ljava/util/List;")
    getAuctionServerRequestFlags = JavaMethod("()I")
    getTrustedBiddingData = JavaMethod("()Landroid/adservices/customaudience/TrustedBiddingData;")
    getName = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getPriority = JavaMethod("()D")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/customaudience/CustomAudience$Builder"
        __javaconstructor__ = [("()V", False)]
        setBuyer = JavaMethod("(Landroid/adservices/common/AdTechIdentifier;)Landroid/adservices/customaudience/CustomAudience$Builder;")
        setUserBiddingSignals = JavaMethod("(Landroid/adservices/common/AdSelectionSignals;)Landroid/adservices/customaudience/CustomAudience$Builder;")
        setExpirationTime = JavaMethod("(Ljava/time/Instant;)Landroid/adservices/customaudience/CustomAudience$Builder;")
        setActivationTime = JavaMethod("(Ljava/time/Instant;)Landroid/adservices/customaudience/CustomAudience$Builder;")
        setComponentAds = JavaMethod("(Ljava/util/List;)Landroid/adservices/customaudience/CustomAudience$Builder;")
        setAds = JavaMethod("(Ljava/util/List;)Landroid/adservices/customaudience/CustomAudience$Builder;")
        setDailyUpdateUri = JavaMethod("(Landroid/net/Uri;)Landroid/adservices/customaudience/CustomAudience$Builder;")
        setTrustedBiddingData = JavaMethod("(Landroid/adservices/customaudience/TrustedBiddingData;)Landroid/adservices/customaudience/CustomAudience$Builder;")
        setAuctionServerRequestFlags = JavaMethod("(I)Landroid/adservices/customaudience/CustomAudience$Builder;")
        setBiddingLogicUri = JavaMethod("(Landroid/net/Uri;)Landroid/adservices/customaudience/CustomAudience$Builder;")
        setPriority = JavaMethod("(D)Landroid/adservices/customaudience/CustomAudience$Builder;")
        setName = JavaMethod("(Ljava/lang/String;)Landroid/adservices/customaudience/CustomAudience$Builder;")
        build = JavaMethod("()Landroid/adservices/customaudience/CustomAudience;")