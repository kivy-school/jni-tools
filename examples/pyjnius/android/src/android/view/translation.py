from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class TranslationCapability(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/translation/TranslationCapability"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    STATE_AVAILABLE_TO_DOWNLOAD = JavaStaticField("I")
    STATE_DOWNLOADING = JavaStaticField("I")
    STATE_NOT_AVAILABLE = JavaStaticField("I")
    STATE_ON_DEVICE = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    getState = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getSourceSpec = JavaMethod("()Landroid/view/translation/TranslationSpec;")
    getSupportedTranslationFlags = JavaMethod("()I")
    getTargetSpec = JavaMethod("()Landroid/view/translation/TranslationSpec;")
    isUiTranslationEnabled = JavaMethod("()Z")

class ViewTranslationResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/translation/ViewTranslationResponse"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getValue = JavaMethod("(Ljava/lang/String;)Landroid/view/translation/TranslationResponseValue;")
    getAutofillId = JavaMethod("()Landroid/view/autofill/AutofillId;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getKeys = JavaMethod("()Ljava/util/Set;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/translation/ViewTranslationResponse$Builder"
        __javaconstructor__ = [("(Landroid/view/autofill/AutofillId;)V", False)]
        setValue = JavaMethod("(Ljava/lang/String;Landroid/view/translation/TranslationResponseValue;)Landroid/view/translation/ViewTranslationResponse$Builder;")
        build = JavaMethod("()Landroid/view/translation/ViewTranslationResponse;")

class TranslationResponseValue(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/translation/TranslationResponseValue"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    EXTRA_DEFINITIONS = JavaStaticField("Ljava/lang/String;")
    STATUS_ERROR = JavaStaticField("I")
    STATUS_SUCCESS = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    forError = JavaStaticMethod("()Landroid/view/translation/TranslationResponseValue;")
    getTransliteration = JavaMethod("()Ljava/lang/CharSequence;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getText = JavaMethod("()Ljava/lang/CharSequence;")
    getExtras = JavaMethod("()Landroid/os/Bundle;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getStatusCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/translation/TranslationResponseValue$Builder"
        __javaconstructor__ = [("(I)V", False)]
        setTransliteration = JavaMethod("(Ljava/lang/CharSequence;)Landroid/view/translation/TranslationResponseValue$Builder;")
        setExtras = JavaMethod("(Landroid/os/Bundle;)Landroid/view/translation/TranslationResponseValue$Builder;")
        build = JavaMethod("()Landroid/view/translation/TranslationResponseValue;")
        setText = JavaMethod("(Ljava/lang/CharSequence;)Landroid/view/translation/TranslationResponseValue$Builder;")

class Translator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/translation/Translator"
    isDestroyed = JavaMethod("()Z")
    destroy = JavaMethod("()V")
    translate = JavaMethod("(Landroid/view/translation/TranslationRequest;Landroid/os/CancellationSignal;Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")

class TranslationContext(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/translation/TranslationContext"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    FLAG_DEFINITIONS = JavaStaticField("I")
    FLAG_LOW_LATENCY = JavaStaticField("I")
    FLAG_TRANSLITERATION = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getTranslationFlags = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getSourceSpec = JavaMethod("()Landroid/view/translation/TranslationSpec;")
    getTargetSpec = JavaMethod("()Landroid/view/translation/TranslationSpec;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/translation/TranslationContext$Builder"
        __javaconstructor__ = [("(Landroid/view/translation/TranslationSpec;Landroid/view/translation/TranslationSpec;)V", False)]
        setTranslationFlags = JavaMethod("(I)Landroid/view/translation/TranslationContext$Builder;")
        build = JavaMethod("()Landroid/view/translation/TranslationContext;")

class TranslationSpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/translation/TranslationSpec"
    __javaconstructor__ = [("(Landroid/icu/util/ULocale;I)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    DATA_FORMAT_TEXT = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getDataFormat = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getLocale = JavaMethod("()Landroid/icu/util/ULocale;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

class UiTranslationStateCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/translation/UiTranslationStateCallback"
    onPaused = JavaMultipleMethod([("()V", False, False), ("(Ljava/lang/String;)V", False, False)])
    onResumed = JavaMultipleMethod([("(Landroid/icu/util/ULocale;Landroid/icu/util/ULocale;)V", False, False), ("(Landroid/icu/util/ULocale;Landroid/icu/util/ULocale;Ljava/lang/String;)V", False, False)])
    onFinished = JavaMultipleMethod([("()V", False, False), ("(Ljava/lang/String;)V", False, False)])
    onStarted = JavaMultipleMethod([("(Landroid/icu/util/ULocale;Landroid/icu/util/ULocale;)V", False, False), ("(Landroid/icu/util/ULocale;Landroid/icu/util/ULocale;Ljava/lang/String;)V", False, False)])

class TranslationRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/translation/TranslationRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    FLAG_DICTIONARY_RESULT = JavaStaticField("I")
    FLAG_PARTIAL_RESPONSES = JavaStaticField("I")
    FLAG_TRANSLATION_RESULT = JavaStaticField("I")
    FLAG_TRANSLITERATION_RESULT = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getTranslationRequestValues = JavaMethod("()Ljava/util/List;")
    getViewTranslationRequests = JavaMethod("()Ljava/util/List;")
    toString = JavaMethod("()Ljava/lang/String;")
    getFlags = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/translation/TranslationRequest$Builder"
        __javaconstructor__ = [("()V", False)]
        setTranslationRequestValues = JavaMethod("(Ljava/util/List;)Landroid/view/translation/TranslationRequest$Builder;")
        setViewTranslationRequests = JavaMethod("(Ljava/util/List;)Landroid/view/translation/TranslationRequest$Builder;")
        setFlags = JavaMethod("(I)Landroid/view/translation/TranslationRequest$Builder;")
        build = JavaMethod("()Landroid/view/translation/TranslationRequest;")

class ViewTranslationRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/translation/ViewTranslationRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    ID_TEXT = JavaStaticField("Ljava/lang/String;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getValue = JavaMethod("(Ljava/lang/String;)Landroid/view/translation/TranslationRequestValue;")
    getAutofillId = JavaMethod("()Landroid/view/autofill/AutofillId;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getKeys = JavaMethod("()Ljava/util/Set;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/translation/ViewTranslationRequest$Builder"
        __javaconstructor__ = [("(Landroid/view/autofill/AutofillId;)V", False), ("(Landroid/view/autofill/AutofillId;J)V", False)]
        setValue = JavaMethod("(Ljava/lang/String;Landroid/view/translation/TranslationRequestValue;)Landroid/view/translation/ViewTranslationRequest$Builder;")
        build = JavaMethod("()Landroid/view/translation/ViewTranslationRequest;")

class TranslationResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/translation/TranslationResponse"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    TRANSLATION_STATUS_CONTEXT_UNSUPPORTED = JavaStaticField("I")
    TRANSLATION_STATUS_SUCCESS = JavaStaticField("I")
    TRANSLATION_STATUS_UNKNOWN_ERROR = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getTranslationStatus = JavaMethod("()I")
    getTranslationResponseValues = JavaMethod("()Landroid/util/SparseArray;")
    getViewTranslationResponses = JavaMethod("()Landroid/util/SparseArray;")
    isFinalResponse = JavaMethod("()Z")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/translation/TranslationResponse$Builder"
        __javaconstructor__ = [("(I)V", False)]
        setTranslationResponseValue = JavaMethod("(ILandroid/view/translation/TranslationResponseValue;)Landroid/view/translation/TranslationResponse$Builder;")
        setFinalResponse = JavaMethod("(Z)Landroid/view/translation/TranslationResponse$Builder;")
        setTranslationResponseValues = JavaMethod("(Landroid/util/SparseArray;)Landroid/view/translation/TranslationResponse$Builder;")
        setViewTranslationResponse = JavaMethod("(ILandroid/view/translation/ViewTranslationResponse;)Landroid/view/translation/TranslationResponse$Builder;")
        setViewTranslationResponses = JavaMethod("(Landroid/util/SparseArray;)Landroid/view/translation/TranslationResponse$Builder;")
        build = JavaMethod("()Landroid/view/translation/TranslationResponse;")

class TranslationManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/translation/TranslationManager"
    getOnDeviceTranslationCapabilities = JavaMethod("(II)Ljava/util/Set;")
    createOnDeviceTranslator = JavaMethod("(Landroid/view/translation/TranslationContext;Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")
    addOnDeviceTranslationCapabilityUpdateListener = JavaMethod("(Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")
    getOnDeviceTranslationSettingsActivityIntent = JavaMethod("()Landroid/app/PendingIntent;")
    removeOnDeviceTranslationCapabilityUpdateListener = JavaMethod("(Ljava/util/function/Consumer;)V")

class UiTranslationManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/translation/UiTranslationManager"
    registerUiTranslationStateCallback = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/view/translation/UiTranslationStateCallback;)V")
    unregisterUiTranslationStateCallback = JavaMethod("(Landroid/view/translation/UiTranslationStateCallback;)V")

class TranslationRequestValue(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/translation/TranslationRequestValue"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getText = JavaMethod("()Ljava/lang/CharSequence;")
    forText = JavaStaticMethod("(Ljava/lang/CharSequence;)Landroid/view/translation/TranslationRequestValue;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

class ViewTranslationCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/translation/ViewTranslationCallback"
    onHideTranslation = JavaMethod("(Landroid/view/View;)Z")
    onClearTranslation = JavaMethod("(Landroid/view/View;)Z")
    onShowTranslation = JavaMethod("(Landroid/view/View;)Z")