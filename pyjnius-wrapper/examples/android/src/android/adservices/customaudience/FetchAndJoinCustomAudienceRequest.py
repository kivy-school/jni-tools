from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FetchAndJoinCustomAudienceRequest"]

class FetchAndJoinCustomAudienceRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/customaudience/FetchAndJoinCustomAudienceRequest"
    getFetchUri = JavaMethod("()Landroid/net/Uri;")
    getName = JavaMethod("()Ljava/lang/String;")
    getActivationTime = JavaMethod("()Ljava/time/Instant;")
    getExpirationTime = JavaMethod("()Ljava/time/Instant;")
    getUserBiddingSignals = JavaMethod("()Landroid/adservices/common/AdSelectionSignals;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/customaudience/FetchAndJoinCustomAudienceRequest/Builder"
        __javaconstructor__ = [("(Landroid/net/Uri;)V", False)]
        setFetchUri = JavaMethod("(Landroid/net/Uri;)Landroid/adservices/customaudience/FetchAndJoinCustomAudienceRequest$Builder;")
        setName = JavaMethod("(Ljava/lang/String;)Landroid/adservices/customaudience/FetchAndJoinCustomAudienceRequest$Builder;")
        setActivationTime = JavaMethod("(Ljava/time/Instant;)Landroid/adservices/customaudience/FetchAndJoinCustomAudienceRequest$Builder;")
        setExpirationTime = JavaMethod("(Ljava/time/Instant;)Landroid/adservices/customaudience/FetchAndJoinCustomAudienceRequest$Builder;")
        setUserBiddingSignals = JavaMethod("(Landroid/adservices/common/AdSelectionSignals;)Landroid/adservices/customaudience/FetchAndJoinCustomAudienceRequest$Builder;")
        build = JavaMethod("()Landroid/adservices/customaudience/FetchAndJoinCustomAudienceRequest;")