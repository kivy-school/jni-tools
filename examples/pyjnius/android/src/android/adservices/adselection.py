from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class DecisionLogic(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/adselection/DecisionLogic"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getLogic = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

class AdSelectionConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/adselection/AdSelectionConfig"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getAdSelectionSignals = JavaMethod("()Landroid/adservices/common/AdSelectionSignals;")
    getCustomAudienceBuyers = JavaMethod("()Ljava/util/List;")
    getPerBuyerSignals = JavaMethod("()Ljava/util/Map;")
    getPerBuyerSignedContextualAds = JavaMethod("()Ljava/util/Map;")
    getSeller = JavaMethod("()Landroid/adservices/common/AdTechIdentifier;")
    getSellerSignals = JavaMethod("()Landroid/adservices/common/AdSelectionSignals;")
    getTrustedScoringSignalsUri = JavaMethod("()Landroid/net/Uri;")
    getDecisionLogicUri = JavaMethod("()Landroid/net/Uri;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/adselection/AdSelectionConfig$Builder"
        __javaconstructor__ = [("()V", False)]
        setAdSelectionSignals = JavaMethod("(Landroid/adservices/common/AdSelectionSignals;)Landroid/adservices/adselection/AdSelectionConfig$Builder;")
        setCustomAudienceBuyers = JavaMethod("(Ljava/util/List;)Landroid/adservices/adselection/AdSelectionConfig$Builder;")
        setSeller = JavaMethod("(Landroid/adservices/common/AdTechIdentifier;)Landroid/adservices/adselection/AdSelectionConfig$Builder;")
        setDecisionLogicUri = JavaMethod("(Landroid/net/Uri;)Landroid/adservices/adselection/AdSelectionConfig$Builder;")
        setPerBuyerSignals = JavaMethod("(Ljava/util/Map;)Landroid/adservices/adselection/AdSelectionConfig$Builder;")
        setPerBuyerSignedContextualAds = JavaMethod("(Ljava/util/Map;)Landroid/adservices/adselection/AdSelectionConfig$Builder;")
        setSellerSignals = JavaMethod("(Landroid/adservices/common/AdSelectionSignals;)Landroid/adservices/adselection/AdSelectionConfig$Builder;")
        setTrustedScoringSignalsUri = JavaMethod("(Landroid/net/Uri;)Landroid/adservices/adselection/AdSelectionConfig$Builder;")
        build = JavaMethod("()Landroid/adservices/adselection/AdSelectionConfig;")

class RemoveAdSelectionOverrideRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/adselection/RemoveAdSelectionOverrideRequest"
    __javaconstructor__ = [("(Landroid/adservices/adselection/AdSelectionConfig;)V", False)]
    getAdSelectionConfig = JavaMethod("()Landroid/adservices/adselection/AdSelectionConfig;")

class GetAdSelectionDataRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/adselection/GetAdSelectionDataRequest"
    getSeller = JavaMethod("()Landroid/adservices/common/AdTechIdentifier;")
    getSellerConfiguration = JavaMethod("()Landroid/adservices/adselection/SellerConfiguration;")
    getCoordinatorOriginUri = JavaMethod("()Landroid/net/Uri;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/adselection/GetAdSelectionDataRequest$Builder"
        __javaconstructor__ = [("()V", False)]
        setSeller = JavaMethod("(Landroid/adservices/common/AdTechIdentifier;)Landroid/adservices/adselection/GetAdSelectionDataRequest$Builder;")
        setCoordinatorOriginUri = JavaMethod("(Landroid/net/Uri;)Landroid/adservices/adselection/GetAdSelectionDataRequest$Builder;")
        setSellerConfiguration = JavaMethod("(Landroid/adservices/adselection/SellerConfiguration;)Landroid/adservices/adselection/GetAdSelectionDataRequest$Builder;")
        build = JavaMethod("()Landroid/adservices/adselection/GetAdSelectionDataRequest;")

class GetAdSelectionDataOutcome(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/adselection/GetAdSelectionDataOutcome"
    getAdSelectionData = JavaMethod("()[B")
    getAdSelectionDataId = JavaMethod("()J")
    getAdSelectionId = JavaMethod("()J")

class SignedContextualAds(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/adselection/SignedContextualAds"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getBuyer = JavaMethod("()Landroid/adservices/common/AdTechIdentifier;")
    getAdsWithBid = JavaMethod("()Ljava/util/List;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getDecisionLogicUri = JavaMethod("()Landroid/net/Uri;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getSignature = JavaMethod("()[B")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/adselection/SignedContextualAds$Builder"
        __javaconstructor__ = [("()V", False), ("(Landroid/adservices/adselection/SignedContextualAds;)V", False)]
        setBuyer = JavaMethod("(Landroid/adservices/common/AdTechIdentifier;)Landroid/adservices/adselection/SignedContextualAds$Builder;")
        setSignature = JavaMethod("([B)Landroid/adservices/adselection/SignedContextualAds$Builder;")
        setAdsWithBid = JavaMethod("(Ljava/util/List;)Landroid/adservices/adselection/SignedContextualAds$Builder;")
        setDecisionLogicUri = JavaMethod("(Landroid/net/Uri;)Landroid/adservices/adselection/SignedContextualAds$Builder;")
        build = JavaMethod("()Landroid/adservices/adselection/SignedContextualAds;")

class PerBuyerDecisionLogic(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/adselection/PerBuyerDecisionLogic"
    __javaconstructor__ = [("(Ljava/util/Map;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    EMPTY = JavaStaticField("Landroid/adservices/adselection/PerBuyerDecisionLogic;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getPerBuyerLogicMap = JavaMethod("()Ljava/util/Map;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

class AdWithBid(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/adselection/AdWithBid"
    __javaconstructor__ = [("(Landroid/adservices/common/AdData;D)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getAdData = JavaMethod("()Landroid/adservices/common/AdData;")
    getBid = JavaMethod("()D")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

class AdSelectionOutcome(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/adselection/AdSelectionOutcome"
    NO_OUTCOME = JavaStaticField("Landroid/adservices/adselection/AdSelectionOutcome;")
    getAdSelectionId = JavaMethod("()J")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getRenderUri = JavaMethod("()Landroid/net/Uri;")
    hasOutcome = JavaMethod("()Z")
    getComponentAdUris = JavaMethod("()Ljava/util/List;")
    getWinningSeller = JavaMethod("()Landroid/adservices/common/AdTechIdentifier;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/adselection/AdSelectionOutcome$Builder"
        __javaconstructor__ = [("()V", False)]
        setAdSelectionId = JavaMethod("(J)Landroid/adservices/adselection/AdSelectionOutcome$Builder;")
        setRenderUri = JavaMethod("(Landroid/net/Uri;)Landroid/adservices/adselection/AdSelectionOutcome$Builder;")
        setComponentAdUris = JavaMethod("(Ljava/util/List;)Landroid/adservices/adselection/AdSelectionOutcome$Builder;")
        build = JavaMethod("()Landroid/adservices/adselection/AdSelectionOutcome;")

class RemoveAdSelectionFromOutcomesOverrideRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/adselection/RemoveAdSelectionFromOutcomesOverrideRequest"
    __javaconstructor__ = [("(Landroid/adservices/adselection/AdSelectionFromOutcomesConfig;)V", False)]
    getAdSelectionFromOutcomesConfig = JavaMethod("()Landroid/adservices/adselection/AdSelectionFromOutcomesConfig;")

class TestAdSelectionManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/adselection/TestAdSelectionManager"
    removeAdSelectionConfigRemoteInfoOverride = JavaMethod("(Landroid/adservices/adselection/RemoveAdSelectionOverrideRequest;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    overrideAdSelectionConfigRemoteInfo = JavaMethod("(Landroid/adservices/adselection/AddAdSelectionOverrideRequest;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    overrideAdSelectionFromOutcomesConfigRemoteInfo = JavaMethod("(Landroid/adservices/adselection/AddAdSelectionFromOutcomesOverrideRequest;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    removeAdSelectionFromOutcomesConfigRemoteInfoOverride = JavaMethod("(Landroid/adservices/adselection/RemoveAdSelectionFromOutcomesOverrideRequest;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    resetAllAdSelectionConfigRemoteOverrides = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    resetAllAdSelectionFromOutcomesConfigRemoteOverrides = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")

class SellerConfiguration(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/adselection/SellerConfiguration"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getMaximumPayloadSizeBytes = JavaMethod("()I")
    getPerBuyerConfigurations = JavaMethod("()Ljava/util/Set;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/adselection/SellerConfiguration$Builder"
        __javaconstructor__ = [("()V", False)]
        setMaximumPayloadSizeBytes = JavaMethod("(I)Landroid/adservices/adselection/SellerConfiguration$Builder;")
        setPerBuyerConfigurations = JavaMethod("(Ljava/util/Set;)Landroid/adservices/adselection/SellerConfiguration$Builder;")
        build = JavaMethod("()Landroid/adservices/adselection/SellerConfiguration;")

class AddAdSelectionFromOutcomesOverrideRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/adselection/AddAdSelectionFromOutcomesOverrideRequest"
    __javaconstructor__ = [("(Landroid/adservices/adselection/AdSelectionFromOutcomesConfig;Ljava/lang/String;Landroid/adservices/common/AdSelectionSignals;)V", False)]
    getOutcomeSelectionLogicJs = JavaMethod("()Ljava/lang/String;")
    getOutcomeSelectionTrustedSignals = JavaMethod("()Landroid/adservices/common/AdSelectionSignals;")
    getAdSelectionFromOutcomesConfig = JavaMethod("()Landroid/adservices/adselection/AdSelectionFromOutcomesConfig;")

class SetAppInstallAdvertisersRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/adselection/SetAppInstallAdvertisersRequest"
    getAdvertisers = JavaMethod("()Ljava/util/Set;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/adselection/SetAppInstallAdvertisersRequest$Builder"
        __javaconstructor__ = [("()V", False)]
        setAdvertisers = JavaMethod("(Ljava/util/Set;)Landroid/adservices/adselection/SetAppInstallAdvertisersRequest$Builder;")
        build = JavaMethod("()Landroid/adservices/adselection/SetAppInstallAdvertisersRequest;")

class UpdateAdCounterHistogramRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/adselection/UpdateAdCounterHistogramRequest"
    getAdEventType = JavaMethod("()I")
    getCallerAdTech = JavaMethod("()Landroid/adservices/common/AdTechIdentifier;")
    getAdSelectionId = JavaMethod("()J")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/adselection/UpdateAdCounterHistogramRequest$Builder"
        __javaconstructor__ = [("(JILandroid/adservices/common/AdTechIdentifier;)V", False)]
        setAdEventType = JavaMethod("(I)Landroid/adservices/adselection/UpdateAdCounterHistogramRequest$Builder;")
        setCallerAdTech = JavaMethod("(Landroid/adservices/common/AdTechIdentifier;)Landroid/adservices/adselection/UpdateAdCounterHistogramRequest$Builder;")
        setAdSelectionId = JavaMethod("(J)Landroid/adservices/adselection/UpdateAdCounterHistogramRequest$Builder;")
        build = JavaMethod("()Landroid/adservices/adselection/UpdateAdCounterHistogramRequest;")

class AdSelectionFromOutcomesConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/adselection/AdSelectionFromOutcomesConfig"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getSeller = JavaMethod("()Landroid/adservices/common/AdTechIdentifier;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getAdSelectionIds = JavaMethod("()Ljava/util/List;")
    getSelectionLogicUri = JavaMethod("()Landroid/net/Uri;")
    getSelectionSignals = JavaMethod("()Landroid/adservices/common/AdSelectionSignals;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/adselection/AdSelectionFromOutcomesConfig$Builder"
        __javaconstructor__ = [("()V", False)]
        setAdSelectionIds = JavaMethod("(Ljava/util/List;)Landroid/adservices/adselection/AdSelectionFromOutcomesConfig$Builder;")
        setSelectionLogicUri = JavaMethod("(Landroid/net/Uri;)Landroid/adservices/adselection/AdSelectionFromOutcomesConfig$Builder;")
        setSelectionSignals = JavaMethod("(Landroid/adservices/common/AdSelectionSignals;)Landroid/adservices/adselection/AdSelectionFromOutcomesConfig$Builder;")
        setSeller = JavaMethod("(Landroid/adservices/common/AdTechIdentifier;)Landroid/adservices/adselection/AdSelectionFromOutcomesConfig$Builder;")
        build = JavaMethod("()Landroid/adservices/adselection/AdSelectionFromOutcomesConfig;")

class AdSelectionManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/adselection/AdSelectionManager"
    reportEvent = JavaMethod("(Landroid/adservices/adselection/ReportEventRequest;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    getTestAdSelectionManager = JavaMethod("()Landroid/adservices/adselection/TestAdSelectionManager;")
    persistAdSelectionResult = JavaMethod("(Landroid/adservices/adselection/PersistAdSelectionResultRequest;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    reportImpression = JavaMethod("(Landroid/adservices/adselection/ReportImpressionRequest;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    selectAds = JavaMultipleMethod([("(Landroid/adservices/adselection/AdSelectionConfig;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V", False, False), ("(Landroid/adservices/adselection/AdSelectionFromOutcomesConfig;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V", False, False)])
    setAppInstallAdvertisers = JavaMethod("(Landroid/adservices/adselection/SetAppInstallAdvertisersRequest;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    updateAdCounterHistogram = JavaMethod("(Landroid/adservices/adselection/UpdateAdCounterHistogramRequest;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    getAdSelectionData = JavaMethod("(Landroid/adservices/adselection/GetAdSelectionDataRequest;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    get = JavaStaticMethod("(Landroid/content/Context;)Landroid/adservices/adselection/AdSelectionManager;")

class PersistAdSelectionResultRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/adselection/PersistAdSelectionResultRequest"
    getAdSelectionResult = JavaMethod("()[B")
    getAdSelectionDataId = JavaMethod("()J")
    getAdSelectionId = JavaMethod("()J")
    getSeller = JavaMethod("()Landroid/adservices/common/AdTechIdentifier;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/adselection/PersistAdSelectionResultRequest$Builder"
        __javaconstructor__ = [("()V", False)]
        setAdSelectionDataId = JavaMethod("(J)Landroid/adservices/adselection/PersistAdSelectionResultRequest$Builder;")
        setAdSelectionResult = JavaMethod("([B)Landroid/adservices/adselection/PersistAdSelectionResultRequest$Builder;")
        setSeller = JavaMethod("(Landroid/adservices/common/AdTechIdentifier;)Landroid/adservices/adselection/PersistAdSelectionResultRequest$Builder;")
        setAdSelectionId = JavaMethod("(J)Landroid/adservices/adselection/PersistAdSelectionResultRequest$Builder;")
        build = JavaMethod("()Landroid/adservices/adselection/PersistAdSelectionResultRequest;")

class PerBuyerConfiguration(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/adselection/PerBuyerConfiguration"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getBuyer = JavaMethod("()Landroid/adservices/common/AdTechIdentifier;")
    getTargetInputSizeBytes = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/adselection/PerBuyerConfiguration$Builder"
        __javaconstructor__ = [("()V", False)]
        setBuyer = JavaMethod("(Landroid/adservices/common/AdTechIdentifier;)Landroid/adservices/adselection/PerBuyerConfiguration$Builder;")
        setTargetInputSizeBytes = JavaMethod("(I)Landroid/adservices/adselection/PerBuyerConfiguration$Builder;")
        build = JavaMethod("()Landroid/adservices/adselection/PerBuyerConfiguration;")

class AddAdSelectionOverrideRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/adselection/AddAdSelectionOverrideRequest"
    __javaconstructor__ = [("(Landroid/adservices/adselection/AdSelectionConfig;Ljava/lang/String;Landroid/adservices/common/AdSelectionSignals;Landroid/adservices/adselection/PerBuyerDecisionLogic;)V", False), ("(Landroid/adservices/adselection/AdSelectionConfig;Ljava/lang/String;Landroid/adservices/common/AdSelectionSignals;)V", False)]
    getPerBuyerDecisionLogic = JavaMethod("()Landroid/adservices/adselection/PerBuyerDecisionLogic;")
    getDecisionLogicJs = JavaMethod("()Ljava/lang/String;")
    getTrustedScoringSignals = JavaMethod("()Landroid/adservices/common/AdSelectionSignals;")
    getAdSelectionConfig = JavaMethod("()Landroid/adservices/adselection/AdSelectionConfig;")

class ReportImpressionRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/adselection/ReportImpressionRequest"
    __javaconstructor__ = [("(J)V", False), ("(JLandroid/adservices/adselection/AdSelectionConfig;)V", False)]
    getAdSelectionId = JavaMethod("()J")
    getAdSelectionConfig = JavaMethod("()Landroid/adservices/adselection/AdSelectionConfig;")

class ReportEventRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/adselection/ReportEventRequest"
    FLAG_REPORTING_DESTINATION_BUYER = JavaStaticField("I")
    FLAG_REPORTING_DESTINATION_COMPONENT_SELLER = JavaStaticField("I")
    FLAG_REPORTING_DESTINATION_SELLER = JavaStaticField("I")
    getInputEvent = JavaMethod("()Landroid/view/InputEvent;")
    getReportingDestinations = JavaMethod("()I")
    getAdSelectionId = JavaMethod("()J")
    getData = JavaMethod("()Ljava/lang/String;")
    getKey = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/adselection/ReportEventRequest$Builder"
        __javaconstructor__ = [("(JLjava/lang/String;Ljava/lang/String;I)V", False)]
        setKey = JavaMethod("(Ljava/lang/String;)Landroid/adservices/adselection/ReportEventRequest$Builder;")
        setReportingDestinations = JavaMethod("(I)Landroid/adservices/adselection/ReportEventRequest$Builder;")
        setInputEvent = JavaMethod("(Landroid/view/InputEvent;)Landroid/adservices/adselection/ReportEventRequest$Builder;")
        setData = JavaMethod("(Ljava/lang/String;)Landroid/adservices/adselection/ReportEventRequest$Builder;")
        setAdSelectionId = JavaMethod("(J)Landroid/adservices/adselection/ReportEventRequest$Builder;")
        build = JavaMethod("()Landroid/adservices/adselection/ReportEventRequest;")