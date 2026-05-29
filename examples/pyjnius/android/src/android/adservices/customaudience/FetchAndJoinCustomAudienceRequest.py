from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FetchAndJoinCustomAudienceRequest"]

class FetchAndJoinCustomAudienceRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/customaudience/FetchAndJoinCustomAudienceRequest"
    getActivationTime = JavaMethod("()Ljava/time/Instant;")
    getExpirationTime = JavaMethod("()Ljava/time/Instant;")
    getFetchUri = JavaMethod("()Landroid/net/Uri;")
    getUserBiddingSignals = JavaMethod("()Landroid/adservices/common/AdSelectionSignals;")
    getName = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/customaudience/FetchAndJoinCustomAudienceRequest$Builder"
        __javaconstructor__ = [("(Landroid/net/Uri;)V", False)]
        setUserBiddingSignals = JavaMethod("(Landroid/adservices/common/AdSelectionSignals;)Landroid/adservices/customaudience/FetchAndJoinCustomAudienceRequest$Builder;")
        setExpirationTime = JavaMethod("(Ljava/time/Instant;)Landroid/adservices/customaudience/FetchAndJoinCustomAudienceRequest$Builder;")
        setFetchUri = JavaMethod("(Landroid/net/Uri;)Landroid/adservices/customaudience/FetchAndJoinCustomAudienceRequest$Builder;")
        setActivationTime = JavaMethod("(Ljava/time/Instant;)Landroid/adservices/customaudience/FetchAndJoinCustomAudienceRequest$Builder;")
        setName = JavaMethod("(Ljava/lang/String;)Landroid/adservices/customaudience/FetchAndJoinCustomAudienceRequest$Builder;")
        build = JavaMethod("()Landroid/adservices/customaudience/FetchAndJoinCustomAudienceRequest;")