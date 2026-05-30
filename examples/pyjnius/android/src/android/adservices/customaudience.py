from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class LeaveCustomAudienceRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/customaudience/LeaveCustomAudienceRequest"
    getBuyer = JavaMethod("()Landroid/adservices/common/AdTechIdentifier;")
    getName = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/customaudience/LeaveCustomAudienceRequest$Builder"
        __javaconstructor__ = [("()V", False)]
        setBuyer = JavaMethod("(Landroid/adservices/common/AdTechIdentifier;)Landroid/adservices/customaudience/LeaveCustomAudienceRequest$Builder;")
        setName = JavaMethod("(Ljava/lang/String;)Landroid/adservices/customaudience/LeaveCustomAudienceRequest$Builder;")
        build = JavaMethod("()Landroid/adservices/customaudience/LeaveCustomAudienceRequest;")

class ScheduleCustomAudienceUpdateRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/customaudience/ScheduleCustomAudienceUpdateRequest"
    getPartialCustomAudienceList = JavaMethod("()Ljava/util/List;")
    getUpdateUri = JavaMethod("()Landroid/net/Uri;")
    shouldReplacePendingUpdates = JavaMethod("()Z")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getMinDelay = JavaMethod("()Ljava/time/Duration;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/customaudience/ScheduleCustomAudienceUpdateRequest$Builder"
        __javaconstructor__ = [("(Landroid/net/Uri;Ljava/time/Duration;Ljava/util/List;)V", False), ("(Landroid/net/Uri;Ljava/time/Duration;)V", False)]
        setPartialCustomAudienceList = JavaMethod("(Ljava/util/List;)Landroid/adservices/customaudience/ScheduleCustomAudienceUpdateRequest$Builder;")
        setMinDelay = JavaMethod("(Ljava/time/Duration;)Landroid/adservices/customaudience/ScheduleCustomAudienceUpdateRequest$Builder;")
        setShouldReplacePendingUpdates = JavaMethod("(Z)Landroid/adservices/customaudience/ScheduleCustomAudienceUpdateRequest$Builder;")
        setUpdateUri = JavaMethod("(Landroid/net/Uri;)Landroid/adservices/customaudience/ScheduleCustomAudienceUpdateRequest$Builder;")
        build = JavaMethod("()Landroid/adservices/customaudience/ScheduleCustomAudienceUpdateRequest;")

class FetchAndJoinCustomAudienceRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/customaudience/FetchAndJoinCustomAudienceRequest"
    getExpirationTime = JavaMethod("()Ljava/time/Instant;")
    getFetchUri = JavaMethod("()Landroid/net/Uri;")
    getActivationTime = JavaMethod("()Ljava/time/Instant;")
    getUserBiddingSignals = JavaMethod("()Landroid/adservices/common/AdSelectionSignals;")
    getName = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/customaudience/FetchAndJoinCustomAudienceRequest$Builder"
        __javaconstructor__ = [("(Landroid/net/Uri;)V", False)]
        setActivationTime = JavaMethod("(Ljava/time/Instant;)Landroid/adservices/customaudience/FetchAndJoinCustomAudienceRequest$Builder;")
        setExpirationTime = JavaMethod("(Ljava/time/Instant;)Landroid/adservices/customaudience/FetchAndJoinCustomAudienceRequest$Builder;")
        setFetchUri = JavaMethod("(Landroid/net/Uri;)Landroid/adservices/customaudience/FetchAndJoinCustomAudienceRequest$Builder;")
        setUserBiddingSignals = JavaMethod("(Landroid/adservices/common/AdSelectionSignals;)Landroid/adservices/customaudience/FetchAndJoinCustomAudienceRequest$Builder;")
        setName = JavaMethod("(Ljava/lang/String;)Landroid/adservices/customaudience/FetchAndJoinCustomAudienceRequest$Builder;")
        build = JavaMethod("()Landroid/adservices/customaudience/FetchAndJoinCustomAudienceRequest;")

class JoinCustomAudienceRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/customaudience/JoinCustomAudienceRequest"
    getCustomAudience = JavaMethod("()Landroid/adservices/customaudience/CustomAudience;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/customaudience/JoinCustomAudienceRequest$Builder"
        __javaconstructor__ = [("()V", False)]
        setCustomAudience = JavaMethod("(Landroid/adservices/customaudience/CustomAudience;)Landroid/adservices/customaudience/JoinCustomAudienceRequest$Builder;")
        build = JavaMethod("()Landroid/adservices/customaudience/JoinCustomAudienceRequest;")

class CustomAudience(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/customaudience/CustomAudience"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    FLAG_AUCTION_SERVER_REQUEST_OMIT_ADS = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getBuyer = JavaMethod("()Landroid/adservices/common/AdTechIdentifier;")
    getExpirationTime = JavaMethod("()Ljava/time/Instant;")
    getActivationTime = JavaMethod("()Ljava/time/Instant;")
    getUserBiddingSignals = JavaMethod("()Landroid/adservices/common/AdSelectionSignals;")
    getAds = JavaMethod("()Ljava/util/List;")
    getBiddingLogicUri = JavaMethod("()Landroid/net/Uri;")
    getAuctionServerRequestFlags = JavaMethod("()I")
    getComponentAds = JavaMethod("()Ljava/util/List;")
    getDailyUpdateUri = JavaMethod("()Landroid/net/Uri;")
    getTrustedBiddingData = JavaMethod("()Landroid/adservices/customaudience/TrustedBiddingData;")
    getName = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getPriority = JavaMethod("()D")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/customaudience/CustomAudience$Builder"
        __javaconstructor__ = [("()V", False)]
        setBuyer = JavaMethod("(Landroid/adservices/common/AdTechIdentifier;)Landroid/adservices/customaudience/CustomAudience$Builder;")
        setActivationTime = JavaMethod("(Ljava/time/Instant;)Landroid/adservices/customaudience/CustomAudience$Builder;")
        setExpirationTime = JavaMethod("(Ljava/time/Instant;)Landroid/adservices/customaudience/CustomAudience$Builder;")
        setUserBiddingSignals = JavaMethod("(Landroid/adservices/common/AdSelectionSignals;)Landroid/adservices/customaudience/CustomAudience$Builder;")
        setAds = JavaMethod("(Ljava/util/List;)Landroid/adservices/customaudience/CustomAudience$Builder;")
        setBiddingLogicUri = JavaMethod("(Landroid/net/Uri;)Landroid/adservices/customaudience/CustomAudience$Builder;")
        setComponentAds = JavaMethod("(Ljava/util/List;)Landroid/adservices/customaudience/CustomAudience$Builder;")
        setAuctionServerRequestFlags = JavaMethod("(I)Landroid/adservices/customaudience/CustomAudience$Builder;")
        setDailyUpdateUri = JavaMethod("(Landroid/net/Uri;)Landroid/adservices/customaudience/CustomAudience$Builder;")
        setTrustedBiddingData = JavaMethod("(Landroid/adservices/customaudience/TrustedBiddingData;)Landroid/adservices/customaudience/CustomAudience$Builder;")
        setPriority = JavaMethod("(D)Landroid/adservices/customaudience/CustomAudience$Builder;")
        setName = JavaMethod("(Ljava/lang/String;)Landroid/adservices/customaudience/CustomAudience$Builder;")
        build = JavaMethod("()Landroid/adservices/customaudience/CustomAudience;")

class PartialCustomAudience(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/customaudience/PartialCustomAudience"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getExpirationTime = JavaMethod("()Ljava/time/Instant;")
    getActivationTime = JavaMethod("()Ljava/time/Instant;")
    getUserBiddingSignals = JavaMethod("()Landroid/adservices/common/AdSelectionSignals;")
    getName = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/customaudience/PartialCustomAudience$Builder"
        __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
        setActivationTime = JavaMethod("(Ljava/time/Instant;)Landroid/adservices/customaudience/PartialCustomAudience$Builder;")
        setExpirationTime = JavaMethod("(Ljava/time/Instant;)Landroid/adservices/customaudience/PartialCustomAudience$Builder;")
        setUserBiddingSignals = JavaMethod("(Landroid/adservices/common/AdSelectionSignals;)Landroid/adservices/customaudience/PartialCustomAudience$Builder;")
        build = JavaMethod("()Landroid/adservices/customaudience/PartialCustomAudience;")

class CustomAudienceManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/customaudience/CustomAudienceManager"
    joinCustomAudience = JavaMethod("(Landroid/adservices/customaudience/JoinCustomAudienceRequest;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    leaveCustomAudience = JavaMethod("(Landroid/adservices/customaudience/LeaveCustomAudienceRequest;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    getTestCustomAudienceManager = JavaMethod("()Landroid/adservices/customaudience/TestCustomAudienceManager;")
    fetchAndJoinCustomAudience = JavaMethod("(Landroid/adservices/customaudience/FetchAndJoinCustomAudienceRequest;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    scheduleCustomAudienceUpdate = JavaMethod("(Landroid/adservices/customaudience/ScheduleCustomAudienceUpdateRequest;Ljava/util/concurrent/Executor;Landroid/adservices/common/AdServicesOutcomeReceiver;)V")
    get = JavaStaticMethod("(Landroid/content/Context;)Landroid/adservices/customaudience/CustomAudienceManager;")

class RemoveCustomAudienceOverrideRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/customaudience/RemoveCustomAudienceOverrideRequest"
    __javaconstructor__ = [("(Landroid/adservices/common/AdTechIdentifier;Ljava/lang/String;)V", False)]
    getBuyer = JavaMethod("()Landroid/adservices/common/AdTechIdentifier;")
    getName = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/customaudience/RemoveCustomAudienceOverrideRequest$Builder"
        __javaconstructor__ = [("()V", False)]
        setBuyer = JavaMethod("(Landroid/adservices/common/AdTechIdentifier;)Landroid/adservices/customaudience/RemoveCustomAudienceOverrideRequest$Builder;")
        setName = JavaMethod("(Ljava/lang/String;)Landroid/adservices/customaudience/RemoveCustomAudienceOverrideRequest$Builder;")
        build = JavaMethod("()Landroid/adservices/customaudience/RemoveCustomAudienceOverrideRequest;")

class TestCustomAudienceManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/customaudience/TestCustomAudienceManager"
    overrideCustomAudienceRemoteInfo = JavaMethod("(Landroid/adservices/customaudience/AddCustomAudienceOverrideRequest;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    removeCustomAudienceRemoteInfoOverride = JavaMethod("(Landroid/adservices/customaudience/RemoveCustomAudienceOverrideRequest;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    resetAllCustomAudienceOverrides = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")

class AddCustomAudienceOverrideRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/customaudience/AddCustomAudienceOverrideRequest"
    __javaconstructor__ = [("(Landroid/adservices/common/AdTechIdentifier;Ljava/lang/String;Ljava/lang/String;Landroid/adservices/common/AdSelectionSignals;)V", False)]
    getBuyer = JavaMethod("()Landroid/adservices/common/AdTechIdentifier;")
    getBiddingLogicJsVersion = JavaMethod("()J")
    getBiddingLogicJs = JavaMethod("()Ljava/lang/String;")
    getTrustedBiddingSignals = JavaMethod("()Landroid/adservices/common/AdSelectionSignals;")
    getName = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/customaudience/AddCustomAudienceOverrideRequest$Builder"
        __javaconstructor__ = [("()V", False)]
        setBuyer = JavaMethod("(Landroid/adservices/common/AdTechIdentifier;)Landroid/adservices/customaudience/AddCustomAudienceOverrideRequest$Builder;")
        setBiddingLogicJsVersion = JavaMethod("(J)Landroid/adservices/customaudience/AddCustomAudienceOverrideRequest$Builder;")
        setBiddingLogicJs = JavaMethod("(Ljava/lang/String;)Landroid/adservices/customaudience/AddCustomAudienceOverrideRequest$Builder;")
        setTrustedBiddingSignals = JavaMethod("(Landroid/adservices/common/AdSelectionSignals;)Landroid/adservices/customaudience/AddCustomAudienceOverrideRequest$Builder;")
        setName = JavaMethod("(Ljava/lang/String;)Landroid/adservices/customaudience/AddCustomAudienceOverrideRequest$Builder;")
        build = JavaMethod("()Landroid/adservices/customaudience/AddCustomAudienceOverrideRequest;")

class TrustedBiddingData(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/customaudience/TrustedBiddingData"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getTrustedBiddingKeys = JavaMethod("()Ljava/util/List;")
    getTrustedBiddingUri = JavaMethod("()Landroid/net/Uri;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/customaudience/TrustedBiddingData$Builder"
        __javaconstructor__ = [("()V", False)]
        setTrustedBiddingKeys = JavaMethod("(Ljava/util/List;)Landroid/adservices/customaudience/TrustedBiddingData$Builder;")
        setTrustedBiddingUri = JavaMethod("(Landroid/net/Uri;)Landroid/adservices/customaudience/TrustedBiddingData$Builder;")
        build = JavaMethod("()Landroid/adservices/customaudience/TrustedBiddingData;")