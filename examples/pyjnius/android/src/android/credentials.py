from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class ClearCredentialStateRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/credentials/ClearCredentialStateRequest"
    __javaconstructor__ = [("(Landroid/os/Bundle;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getData = JavaMethod("()Landroid/os/Bundle;")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

class GetCredentialRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/credentials/GetCredentialRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getOrigin = JavaMethod("()Ljava/lang/String;")
    alwaysSendAppInfoToProvider = JavaMethod("()Z")
    getCredentialOptions = JavaMethod("()Ljava/util/List;")
    getData = JavaMethod("()Landroid/os/Bundle;")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/credentials/GetCredentialRequest$Builder"
        __javaconstructor__ = [("(Landroid/os/Bundle;)V", False)]
        setCredentialOptions = JavaMethod("(Ljava/util/List;)Landroid/credentials/GetCredentialRequest$Builder;")
        addCredentialOption = JavaMethod("(Landroid/credentials/CredentialOption;)Landroid/credentials/GetCredentialRequest$Builder;")
        setOrigin = JavaMethod("(Ljava/lang/String;)Landroid/credentials/GetCredentialRequest$Builder;")
        setAlwaysSendAppInfoToProvider = JavaMethod("(Z)Landroid/credentials/GetCredentialRequest$Builder;")
        build = JavaMethod("()Landroid/credentials/GetCredentialRequest;")

class CreateCredentialRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/credentials/CreateCredentialRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getOrigin = JavaMethod("()Ljava/lang/String;")
    getCredentialData = JavaMethod("()Landroid/os/Bundle;")
    alwaysSendAppInfoToProvider = JavaMethod("()Z")
    toString = JavaMethod("()Ljava/lang/String;")
    getType = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getCandidateQueryData = JavaMethod("()Landroid/os/Bundle;")
    isSystemProviderRequired = JavaMethod("()Z")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/credentials/CreateCredentialRequest$Builder"
        __javaconstructor__ = [("(Ljava/lang/String;Landroid/os/Bundle;Landroid/os/Bundle;)V", False)]
        setIsSystemProviderRequired = JavaMethod("(Z)Landroid/credentials/CreateCredentialRequest$Builder;")
        setOrigin = JavaMethod("(Ljava/lang/String;)Landroid/credentials/CreateCredentialRequest$Builder;")
        setAlwaysSendAppInfoToProvider = JavaMethod("(Z)Landroid/credentials/CreateCredentialRequest$Builder;")
        build = JavaMethod("()Landroid/credentials/CreateCredentialRequest;")

class RegisterCredentialDescriptionRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/credentials/RegisterCredentialDescriptionRequest"
    __javaconstructor__ = [("(Landroid/credentials/CredentialDescription;)V", False), ("(Ljava/util/Set;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getCredentialDescriptions = JavaMethod("()Ljava/util/Set;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

class CreateCredentialResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/credentials/CreateCredentialResponse"
    __javaconstructor__ = [("(Landroid/os/Bundle;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getData = JavaMethod("()Landroid/os/Bundle;")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

class PrepareGetCredentialResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/credentials/PrepareGetCredentialResponse"
    hasAuthenticationResults = JavaMethod("()Z")
    hasCredentialResults = JavaMethod("(Ljava/lang/String;)Z")
    getPendingGetCredentialHandle = JavaMethod("()Landroid/credentials/PrepareGetCredentialResponse$PendingGetCredentialHandle;")
    hasRemoteResults = JavaMethod("()Z")

    class PendingGetCredentialHandle(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/credentials/PrepareGetCredentialResponse$PendingGetCredentialHandle"

class CredentialDescription(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/credentials/CredentialDescription"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/util/Set;Ljava/util/List;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getSupportedElementKeys = JavaMethod("()Ljava/util/Set;")
    getCredentialEntries = JavaMethod("()Ljava/util/List;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getType = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

class CredentialManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/credentials/CredentialManager"
    clearCredentialState = JavaMethod("(Landroid/credentials/ClearCredentialStateRequest;Landroid/os/CancellationSignal;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    isEnabledCredentialProviderService = JavaMethod("(Landroid/content/ComponentName;)Z")
    createCredential = JavaMethod("(Landroid/content/Context;Landroid/credentials/CreateCredentialRequest;Landroid/os/CancellationSignal;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    prepareGetCredential = JavaMethod("(Landroid/credentials/GetCredentialRequest;Landroid/os/CancellationSignal;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    getCredential = JavaMultipleMethod([("(Landroid/content/Context;Landroid/credentials/PrepareGetCredentialResponse$PendingGetCredentialHandle;Landroid/os/CancellationSignal;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V", False, False), ("(Landroid/content/Context;Landroid/credentials/GetCredentialRequest;Landroid/os/CancellationSignal;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V", False, False)])
    registerCredentialDescription = JavaMethod("(Landroid/credentials/RegisterCredentialDescriptionRequest;)V")
    unregisterCredentialDescription = JavaMethod("(Landroid/credentials/UnregisterCredentialDescriptionRequest;)V")

class CredentialOption(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/credentials/CredentialOption"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    SUPPORTED_ELEMENT_KEYS = JavaStaticField("Ljava/lang/String;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    getType = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getCredentialRetrievalData = JavaMethod("()Landroid/os/Bundle;")
    getAllowedProviders = JavaMethod("()Ljava/util/Set;")
    getCandidateQueryData = JavaMethod("()Landroid/os/Bundle;")
    isSystemProviderRequired = JavaMethod("()Z")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/credentials/CredentialOption$Builder"
        __javaconstructor__ = [("(Ljava/lang/String;Landroid/os/Bundle;Landroid/os/Bundle;)V", False)]
        setIsSystemProviderRequired = JavaMethod("(Z)Landroid/credentials/CredentialOption$Builder;")
        setAllowedProviders = JavaMethod("(Ljava/util/Set;)Landroid/credentials/CredentialOption$Builder;")
        addAllowedProvider = JavaMethod("(Landroid/content/ComponentName;)Landroid/credentials/CredentialOption$Builder;")
        build = JavaMethod("()Landroid/credentials/CredentialOption;")

class UnregisterCredentialDescriptionRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/credentials/UnregisterCredentialDescriptionRequest"
    __javaconstructor__ = [("(Landroid/credentials/CredentialDescription;)V", False), ("(Ljava/util/Set;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getCredentialDescriptions = JavaMethod("()Ljava/util/Set;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

class ClearCredentialStateException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/credentials/ClearCredentialStateException"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/String;)V", False), ("(Ljava/lang/String;)V", False)]
    TYPE_UNKNOWN = JavaStaticField("Ljava/lang/String;")
    getType = JavaMethod("()Ljava/lang/String;")

class GetCredentialException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/credentials/GetCredentialException"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/String;)V", False), ("(Ljava/lang/String;)V", False)]
    TYPE_INTERRUPTED = JavaStaticField("Ljava/lang/String;")
    TYPE_NO_CREDENTIAL = JavaStaticField("Ljava/lang/String;")
    TYPE_UNKNOWN = JavaStaticField("Ljava/lang/String;")
    TYPE_USER_CANCELED = JavaStaticField("Ljava/lang/String;")
    getType = JavaMethod("()Ljava/lang/String;")

class CreateCredentialException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/credentials/CreateCredentialException"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/String;)V", False), ("(Ljava/lang/String;)V", False)]
    TYPE_INTERRUPTED = JavaStaticField("Ljava/lang/String;")
    TYPE_NO_CREATE_OPTIONS = JavaStaticField("Ljava/lang/String;")
    TYPE_UNKNOWN = JavaStaticField("Ljava/lang/String;")
    TYPE_USER_CANCELED = JavaStaticField("Ljava/lang/String;")
    getType = JavaMethod("()Ljava/lang/String;")

class GetCredentialResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/credentials/GetCredentialResponse"
    __javaconstructor__ = [("(Landroid/credentials/Credential;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getCredential = JavaMethod("()Landroid/credentials/Credential;")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

class Credential(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/credentials/Credential"
    __javaconstructor__ = [("(Ljava/lang/String;Landroid/os/Bundle;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    TYPE_PASSWORD_CREDENTIAL = JavaStaticField("Ljava/lang/String;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getData = JavaMethod("()Landroid/os/Bundle;")
    toString = JavaMethod("()Ljava/lang/String;")
    getType = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")