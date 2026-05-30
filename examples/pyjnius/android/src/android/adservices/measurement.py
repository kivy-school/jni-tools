from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class WebSourceRegistrationRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/measurement/WebSourceRegistrationRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getInputEvent = JavaMethod("()Landroid/view/InputEvent;")
    getAppDestination = JavaMethod("()Landroid/net/Uri;")
    getTopOriginUri = JavaMethod("()Landroid/net/Uri;")
    getVerifiedDestination = JavaMethod("()Landroid/net/Uri;")
    getSourceParams = JavaMethod("()Ljava/util/List;")
    getWebDestination = JavaMethod("()Landroid/net/Uri;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/measurement/WebSourceRegistrationRequest$Builder"
        __javaconstructor__ = [("(Ljava/util/List;Landroid/net/Uri;)V", False)]
        setInputEvent = JavaMethod("(Landroid/view/InputEvent;)Landroid/adservices/measurement/WebSourceRegistrationRequest$Builder;")
        setWebDestination = JavaMethod("(Landroid/net/Uri;)Landroid/adservices/measurement/WebSourceRegistrationRequest$Builder;")
        setAppDestination = JavaMethod("(Landroid/net/Uri;)Landroid/adservices/measurement/WebSourceRegistrationRequest$Builder;")
        setVerifiedDestination = JavaMethod("(Landroid/net/Uri;)Landroid/adservices/measurement/WebSourceRegistrationRequest$Builder;")
        build = JavaMethod("()Landroid/adservices/measurement/WebSourceRegistrationRequest;")

class SourceRegistrationRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/measurement/SourceRegistrationRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getInputEvent = JavaMethod("()Landroid/view/InputEvent;")
    getRegistrationUris = JavaMethod("()Ljava/util/List;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/measurement/SourceRegistrationRequest$Builder"
        __javaconstructor__ = [("(Ljava/util/List;)V", False)]
        setInputEvent = JavaMethod("(Landroid/view/InputEvent;)Landroid/adservices/measurement/SourceRegistrationRequest$Builder;")
        build = JavaMethod("()Landroid/adservices/measurement/SourceRegistrationRequest;")

class WebSourceParams(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/measurement/WebSourceParams"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getRegistrationUri = JavaMethod("()Landroid/net/Uri;")
    isDebugKeyAllowed = JavaMethod("()Z")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/measurement/WebSourceParams$Builder"
        __javaconstructor__ = [("(Landroid/net/Uri;)V", False)]
        setDebugKeyAllowed = JavaMethod("(Z)Landroid/adservices/measurement/WebSourceParams$Builder;")
        build = JavaMethod("()Landroid/adservices/measurement/WebSourceParams;")

class MeasurementManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/measurement/MeasurementManager"
    MEASUREMENT_API_STATE_DISABLED = JavaStaticField("I")
    MEASUREMENT_API_STATE_ENABLED = JavaStaticField("I")
    get = JavaStaticMethod("(Landroid/content/Context;)Landroid/adservices/measurement/MeasurementManager;")
    registerSource = JavaMultipleMethod([("(Landroid/adservices/measurement/SourceRegistrationRequest;Ljava/util/concurrent/Executor;Landroid/adservices/common/AdServicesOutcomeReceiver;)V", False, False), ("(Landroid/adservices/measurement/SourceRegistrationRequest;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V", False, False), ("(Landroid/net/Uri;Landroid/view/InputEvent;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V", False, False), ("(Landroid/net/Uri;Landroid/view/InputEvent;Ljava/util/concurrent/Executor;Landroid/adservices/common/AdServicesOutcomeReceiver;)V", False, False)])
    deleteRegistrations = JavaMultipleMethod([("(Landroid/adservices/measurement/DeletionRequest;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V", False, False), ("(Landroid/adservices/measurement/DeletionRequest;Ljava/util/concurrent/Executor;Landroid/adservices/common/AdServicesOutcomeReceiver;)V", False, False)])
    getMeasurementApiStatus = JavaMultipleMethod([("(Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V", False, False), ("(Ljava/util/concurrent/Executor;Landroid/adservices/common/AdServicesOutcomeReceiver;)V", False, False)])
    registerTrigger = JavaMultipleMethod([("(Landroid/net/Uri;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V", False, False), ("(Landroid/net/Uri;Ljava/util/concurrent/Executor;Landroid/adservices/common/AdServicesOutcomeReceiver;)V", False, False)])
    registerWebSource = JavaMultipleMethod([("(Landroid/adservices/measurement/WebSourceRegistrationRequest;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V", False, False), ("(Landroid/adservices/measurement/WebSourceRegistrationRequest;Ljava/util/concurrent/Executor;Landroid/adservices/common/AdServicesOutcomeReceiver;)V", False, False)])
    registerWebTrigger = JavaMultipleMethod([("(Landroid/adservices/measurement/WebTriggerRegistrationRequest;Ljava/util/concurrent/Executor;Landroid/adservices/common/AdServicesOutcomeReceiver;)V", False, False), ("(Landroid/adservices/measurement/WebTriggerRegistrationRequest;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V", False, False)])

class WebTriggerRegistrationRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/measurement/WebTriggerRegistrationRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getDestination = JavaMethod("()Landroid/net/Uri;")
    getTriggerParams = JavaMethod("()Ljava/util/List;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/measurement/WebTriggerRegistrationRequest$Builder"
        __javaconstructor__ = [("(Ljava/util/List;Landroid/net/Uri;)V", False)]
        build = JavaMethod("()Landroid/adservices/measurement/WebTriggerRegistrationRequest;")

class DeletionRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/measurement/DeletionRequest"
    DELETION_MODE_ALL = JavaStaticField("I")
    DELETION_MODE_EXCLUDE_INTERNAL_DATA = JavaStaticField("I")
    MATCH_BEHAVIOR_DELETE = JavaStaticField("I")
    MATCH_BEHAVIOR_PRESERVE = JavaStaticField("I")
    getEnd = JavaMethod("()Ljava/time/Instant;")
    getDomainUris = JavaMethod("()Ljava/util/List;")
    getDeletionMode = JavaMethod("()I")
    getMatchBehavior = JavaMethod("()I")
    getOriginUris = JavaMethod("()Ljava/util/List;")
    getStart = JavaMethod("()Ljava/time/Instant;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/measurement/DeletionRequest$Builder"
        __javaconstructor__ = [("()V", False)]
        setDeletionMode = JavaMethod("(I)Landroid/adservices/measurement/DeletionRequest$Builder;")
        setEnd = JavaMethod("(Ljava/time/Instant;)Landroid/adservices/measurement/DeletionRequest$Builder;")
        setDomainUris = JavaMethod("(Ljava/util/List;)Landroid/adservices/measurement/DeletionRequest$Builder;")
        setMatchBehavior = JavaMethod("(I)Landroid/adservices/measurement/DeletionRequest$Builder;")
        setOriginUris = JavaMethod("(Ljava/util/List;)Landroid/adservices/measurement/DeletionRequest$Builder;")
        setStart = JavaMethod("(Ljava/time/Instant;)Landroid/adservices/measurement/DeletionRequest$Builder;")
        build = JavaMethod("()Landroid/adservices/measurement/DeletionRequest;")

class WebTriggerParams(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/measurement/WebTriggerParams"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getRegistrationUri = JavaMethod("()Landroid/net/Uri;")
    isDebugKeyAllowed = JavaMethod("()Z")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/measurement/WebTriggerParams$Builder"
        __javaconstructor__ = [("(Landroid/net/Uri;)V", False)]
        setDebugKeyAllowed = JavaMethod("(Z)Landroid/adservices/measurement/WebTriggerParams$Builder;")
        build = JavaMethod("()Landroid/adservices/measurement/WebTriggerParams;")