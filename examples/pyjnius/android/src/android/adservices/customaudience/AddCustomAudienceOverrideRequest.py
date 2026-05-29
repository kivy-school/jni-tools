from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AddCustomAudienceOverrideRequest"]

class AddCustomAudienceOverrideRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/customaudience/AddCustomAudienceOverrideRequest"
    __javaconstructor__ = [("(Landroid/adservices/common/AdTechIdentifier;Ljava/lang/String;Ljava/lang/String;Landroid/adservices/common/AdSelectionSignals;)V", False)]
    getBuyer = JavaMethod("()Landroid/adservices/common/AdTechIdentifier;")
    getBiddingLogicJs = JavaMethod("()Ljava/lang/String;")
    getBiddingLogicJsVersion = JavaMethod("()J")
    getTrustedBiddingSignals = JavaMethod("()Landroid/adservices/common/AdSelectionSignals;")
    getName = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/customaudience/AddCustomAudienceOverrideRequest$Builder"
        __javaconstructor__ = [("()V", False)]
        setBuyer = JavaMethod("(Landroid/adservices/common/AdTechIdentifier;)Landroid/adservices/customaudience/AddCustomAudienceOverrideRequest$Builder;")
        setBiddingLogicJs = JavaMethod("(Ljava/lang/String;)Landroid/adservices/customaudience/AddCustomAudienceOverrideRequest$Builder;")
        setBiddingLogicJsVersion = JavaMethod("(J)Landroid/adservices/customaudience/AddCustomAudienceOverrideRequest$Builder;")
        setTrustedBiddingSignals = JavaMethod("(Landroid/adservices/common/AdSelectionSignals;)Landroid/adservices/customaudience/AddCustomAudienceOverrideRequest$Builder;")
        setName = JavaMethod("(Ljava/lang/String;)Landroid/adservices/customaudience/AddCustomAudienceOverrideRequest$Builder;")
        build = JavaMethod("()Landroid/adservices/customaudience/AddCustomAudienceOverrideRequest;")