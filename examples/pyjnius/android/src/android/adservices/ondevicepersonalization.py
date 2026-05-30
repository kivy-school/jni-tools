from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class TrainingInterval(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/TrainingInterval"
    SCHEDULING_MODE_ONE_TIME = JavaStaticField("I")
    SCHEDULING_MODE_RECURRENT = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getMinimumInterval = JavaMethod("()Ljava/time/Duration;")
    getSchedulingMode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/ondevicepersonalization/TrainingInterval$Builder"
        __javaconstructor__ = [("()V", False)]
        build = JavaMethod("()Landroid/adservices/ondevicepersonalization/TrainingInterval;")
        setMinimumInterval = JavaMethod("(Ljava/time/Duration;)Landroid/adservices/ondevicepersonalization/TrainingInterval$Builder;")
        setSchedulingMode = JavaMethod("(I)Landroid/adservices/ondevicepersonalization/TrainingInterval$Builder;")

class OnDevicePersonalizationManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/OnDevicePersonalizationManager"
    execute = JavaMethod("(Landroid/content/ComponentName;Landroid/os/PersistableBundle;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    requestSurfacePackage = JavaMethod("(Landroid/adservices/ondevicepersonalization/SurfacePackageToken;Landroid/os/IBinder;IIILjava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    executeInIsolatedService = JavaMethod("(Landroid/adservices/ondevicepersonalization/ExecuteInIsolatedServiceRequest;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")

    class ExecuteResult(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/ondevicepersonalization/OnDevicePersonalizationManager$ExecuteResult"
        getSurfacePackageToken = JavaMethod("()Landroid/adservices/ondevicepersonalization/SurfacePackageToken;")
        getOutputData = JavaMethod("()[B")

class InferenceInput(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/InferenceInput"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getParams = JavaMethod("()Landroid/adservices/ondevicepersonalization/InferenceInput$Params;")
    getBatchSize = JavaMethod("()I")
    getExpectedOutputStructure = JavaMethod("()Landroid/adservices/ondevicepersonalization/InferenceOutput;")
    getInputData = JavaMethod("()[Ljava/lang/Object;")

    class Params(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/ondevicepersonalization/InferenceInput$Params"
        DELEGATE_CPU = JavaStaticField("I")
        MODEL_TYPE_TENSORFLOW_LITE = JavaStaticField("I")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")
        getDelegateType = JavaMethod("()I")
        getKeyValueStore = JavaMethod("()Landroid/adservices/ondevicepersonalization/KeyValueStore;")
        getModelKey = JavaMethod("()Ljava/lang/String;")
        getModelType = JavaMethod("()I")
        getRecommendedNumThreads = JavaMethod("()I")

        class Builder(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/adservices/ondevicepersonalization/InferenceInput$Params$Builder"
            __javaconstructor__ = [("(Landroid/adservices/ondevicepersonalization/KeyValueStore;Ljava/lang/String;)V", False)]
            setKeyValueStore = JavaMethod("(Landroid/adservices/ondevicepersonalization/KeyValueStore;)Landroid/adservices/ondevicepersonalization/InferenceInput$Params$Builder;")
            setDelegateType = JavaMethod("(I)Landroid/adservices/ondevicepersonalization/InferenceInput$Params$Builder;")
            setModelKey = JavaMethod("(Ljava/lang/String;)Landroid/adservices/ondevicepersonalization/InferenceInput$Params$Builder;")
            setModelType = JavaMethod("(I)Landroid/adservices/ondevicepersonalization/InferenceInput$Params$Builder;")
            setRecommendedNumThreads = JavaMethod("(I)Landroid/adservices/ondevicepersonalization/InferenceInput$Params$Builder;")
            build = JavaMethod("()Landroid/adservices/ondevicepersonalization/InferenceInput$Params;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/ondevicepersonalization/InferenceInput$Builder"
        __javaconstructor__ = [("(Landroid/adservices/ondevicepersonalization/InferenceInput$Params;[Ljava/lang/Object;Landroid/adservices/ondevicepersonalization/InferenceOutput;)V", False)]
        setExpectedOutputStructure = JavaMethod("(Landroid/adservices/ondevicepersonalization/InferenceOutput;)Landroid/adservices/ondevicepersonalization/InferenceInput$Builder;")
        setBatchSize = JavaMethod("(I)Landroid/adservices/ondevicepersonalization/InferenceInput$Builder;")
        setInputData = JavaMethod("([Ljava/lang/Object;)Landroid/adservices/ondevicepersonalization/InferenceInput$Builder;", varargs=True)
        setParams = JavaMethod("(Landroid/adservices/ondevicepersonalization/InferenceInput$Params;)Landroid/adservices/ondevicepersonalization/InferenceInput$Builder;")
        build = JavaMethod("()Landroid/adservices/ondevicepersonalization/InferenceInput;")

class TrainingExamplesInput(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/TrainingExamplesInput"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;[BLjava/lang/String;)V", False)]
    getCollectionName = JavaMethod("()Ljava/lang/String;")
    getPopulationName = JavaMethod("()Ljava/lang/String;")
    getResumptionToken = JavaMethod("()[B")
    getTaskName = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

class FederatedComputeScheduler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/FederatedComputeScheduler"
    cancel = JavaMethod("(Landroid/adservices/ondevicepersonalization/FederatedComputeInput;)V")
    schedule = JavaMethod("(Landroid/adservices/ondevicepersonalization/FederatedComputeScheduler$Params;Landroid/adservices/ondevicepersonalization/FederatedComputeInput;)V")

    class Params(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/ondevicepersonalization/FederatedComputeScheduler$Params"
        __javaconstructor__ = [("(Landroid/adservices/ondevicepersonalization/TrainingInterval;)V", False)]
        getTrainingInterval = JavaMethod("()Landroid/adservices/ondevicepersonalization/TrainingInterval;")

class FederatedComputeInput(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/FederatedComputeInput"
    getPopulationName = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/ondevicepersonalization/FederatedComputeInput$Builder"
        __javaconstructor__ = [("()V", False)]
        setPopulationName = JavaMethod("(Ljava/lang/String;)Landroid/adservices/ondevicepersonalization/FederatedComputeInput$Builder;")
        build = JavaMethod("()Landroid/adservices/ondevicepersonalization/FederatedComputeInput;")

class TrainingExamplesOutput(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/TrainingExamplesOutput"
    getTrainingExampleRecords = JavaMethod("()Ljava/util/List;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/ondevicepersonalization/TrainingExamplesOutput$Builder"
        __javaconstructor__ = [("()V", False)]
        build = JavaMethod("()Landroid/adservices/ondevicepersonalization/TrainingExamplesOutput;")
        addTrainingExampleRecord = JavaMethod("(Landroid/adservices/ondevicepersonalization/TrainingExampleRecord;)Landroid/adservices/ondevicepersonalization/TrainingExamplesOutput$Builder;")
        setTrainingExampleRecords = JavaMethod("(Ljava/util/List;)Landroid/adservices/ondevicepersonalization/TrainingExamplesOutput$Builder;")

class InferenceOutput(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/InferenceOutput"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getDataOutputs = JavaMethod("()Ljava/util/Map;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/ondevicepersonalization/InferenceOutput$Builder"
        __javaconstructor__ = [("()V", False)]
        build = JavaMethod("()Landroid/adservices/ondevicepersonalization/InferenceOutput;")
        addDataOutput = JavaMethod("(ILjava/lang/Object;)Landroid/adservices/ondevicepersonalization/InferenceOutput$Builder;")
        setDataOutputs = JavaMethod("(Ljava/util/Map;)Landroid/adservices/ondevicepersonalization/InferenceOutput$Builder;")

class MutableKeyValueStore(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/MutableKeyValueStore"
    remove = JavaMethod("(Ljava/lang/String;)[B")
    put = JavaMethod("(Ljava/lang/String;[B)[B")

class EventOutput(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/EventOutput"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getEventLogRecord = JavaMethod("()Landroid/adservices/ondevicepersonalization/EventLogRecord;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/ondevicepersonalization/EventOutput$Builder"
        __javaconstructor__ = [("()V", False)]
        build = JavaMethod("()Landroid/adservices/ondevicepersonalization/EventOutput;")
        setEventLogRecord = JavaMethod("(Landroid/adservices/ondevicepersonalization/EventLogRecord;)Landroid/adservices/ondevicepersonalization/EventOutput$Builder;")

class UserData(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/UserData"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getOrientation = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getAppInfos = JavaMethod("()Ljava/util/Map;")
    getCarrier = JavaMethod("()Ljava/lang/String;")
    getBatteryPercentage = JavaMethod("()I")
    getAvailableStorageBytes = JavaMethod("()J")
    getDataNetworkType = JavaMethod("()I")
    getNetworkCapabilities = JavaMethod("()Landroid/net/NetworkCapabilities;")
    getTimezoneUtcOffset = JavaMethod("()Ljava/time/Duration;")

class IsolatedWorker(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/IsolatedWorker"
    onDownloadCompleted = JavaMethod("(Landroid/adservices/ondevicepersonalization/DownloadCompletedInput;Landroid/os/OutcomeReceiver;)V")
    onExecute = JavaMethod("(Landroid/adservices/ondevicepersonalization/ExecuteInput;Landroid/os/OutcomeReceiver;)V")
    onRender = JavaMethod("(Landroid/adservices/ondevicepersonalization/RenderInput;Landroid/os/OutcomeReceiver;)V")
    onTrainingExamples = JavaMethod("(Landroid/adservices/ondevicepersonalization/TrainingExamplesInput;Landroid/os/OutcomeReceiver;)V")
    onWebTrigger = JavaMethod("(Landroid/adservices/ondevicepersonalization/WebTriggerInput;Landroid/os/OutcomeReceiver;)V")
    onEvent = JavaMethod("(Landroid/adservices/ondevicepersonalization/EventInput;Landroid/os/OutcomeReceiver;)V")

class ModelManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/ModelManager"
    run = JavaMethod("(Landroid/adservices/ondevicepersonalization/InferenceInput;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")

class ExecuteInput(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/ExecuteInput"
    __javaconstructor__ = [("(Ljava/lang/String;Landroid/os/PersistableBundle;)V", False)]
    getAppPackageName = JavaMethod("()Ljava/lang/String;")
    getAppParams = JavaMethod("()Landroid/os/PersistableBundle;")

class WebTriggerInput(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/WebTriggerInput"
    __javaconstructor__ = [("(Landroid/net/Uri;Ljava/lang/String;[B)V", False)]
    getDestinationUrl = JavaMethod("()Landroid/net/Uri;")
    getData = JavaMethod("()[B")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getAppPackageName = JavaMethod("()Ljava/lang/String;")

class SurfacePackageToken(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/SurfacePackageToken"

class ExecuteOutput(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/ExecuteOutput"
    getRenderingConfig = JavaMethod("()Landroid/adservices/ondevicepersonalization/RenderingConfig;")
    getBestValue = JavaMethod("()I")
    getEventLogRecords = JavaMethod("()Ljava/util/List;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getOutputData = JavaMethod("()[B")
    getRequestLogRecord = JavaMethod("()Landroid/adservices/ondevicepersonalization/RequestLogRecord;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/ondevicepersonalization/ExecuteOutput$Builder"
        __javaconstructor__ = [("()V", False)]
        addEventLogRecord = JavaMethod("(Landroid/adservices/ondevicepersonalization/EventLogRecord;)Landroid/adservices/ondevicepersonalization/ExecuteOutput$Builder;")
        setBestValue = JavaMethod("(I)Landroid/adservices/ondevicepersonalization/ExecuteOutput$Builder;")
        setEventLogRecords = JavaMethod("(Ljava/util/List;)Landroid/adservices/ondevicepersonalization/ExecuteOutput$Builder;")
        setOutputData = JavaMethod("([B)Landroid/adservices/ondevicepersonalization/ExecuteOutput$Builder;", varargs=True)
        setRenderingConfig = JavaMethod("(Landroid/adservices/ondevicepersonalization/RenderingConfig;)Landroid/adservices/ondevicepersonalization/ExecuteOutput$Builder;")
        setRequestLogRecord = JavaMethod("(Landroid/adservices/ondevicepersonalization/RequestLogRecord;)Landroid/adservices/ondevicepersonalization/ExecuteOutput$Builder;")
        build = JavaMethod("()Landroid/adservices/ondevicepersonalization/ExecuteOutput;")

class LogReader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/LogReader"
    getJoinedEvents = JavaMethod("(Ljava/time/Instant;Ljava/time/Instant;)Ljava/util/List;")
    getRequests = JavaMethod("(Ljava/time/Instant;Ljava/time/Instant;)Ljava/util/List;")

class EventUrlProvider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/EventUrlProvider"
    createEventTrackingUrlWithRedirect = JavaMethod("(Landroid/os/PersistableBundle;Landroid/net/Uri;)Landroid/net/Uri;")
    createEventTrackingUrlWithResponse = JavaMethod("(Landroid/os/PersistableBundle;[BLjava/lang/String;)Landroid/net/Uri;")

class RenderingConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/RenderingConfig"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getKeys = JavaMethod("()Ljava/util/List;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/ondevicepersonalization/RenderingConfig$Builder"
        __javaconstructor__ = [("()V", False)]
        build = JavaMethod("()Landroid/adservices/ondevicepersonalization/RenderingConfig;")
        addKey = JavaMethod("(Ljava/lang/String;)Landroid/adservices/ondevicepersonalization/RenderingConfig$Builder;")
        setKeys = JavaMethod("(Ljava/util/List;)Landroid/adservices/ondevicepersonalization/RenderingConfig$Builder;")

class DownloadCompletedInput(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/DownloadCompletedInput"
    __javaconstructor__ = [("(Landroid/adservices/ondevicepersonalization/KeyValueStore;)V", False)]
    getDownloadedContents = JavaMethod("()Landroid/adservices/ondevicepersonalization/KeyValueStore;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

class OnDevicePersonalizationException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/OnDevicePersonalizationException"
    ERROR_INFERENCE_FAILED = JavaStaticField("I")
    ERROR_INFERENCE_MODEL_NOT_FOUND = JavaStaticField("I")
    ERROR_INVALID_TRAINING_MANIFEST = JavaStaticField("I")
    ERROR_ISOLATED_SERVICE_FAILED = JavaStaticField("I")
    ERROR_ISOLATED_SERVICE_LOADING_FAILED = JavaStaticField("I")
    ERROR_ISOLATED_SERVICE_MANIFEST_PARSING_FAILED = JavaStaticField("I")
    ERROR_ISOLATED_SERVICE_TIMEOUT = JavaStaticField("I")
    ERROR_PERSONALIZATION_DISABLED = JavaStaticField("I")
    ERROR_SCHEDULE_TRAINING_FAILED = JavaStaticField("I")
    getErrorCode = JavaMethod("()I")

class IsolatedService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/IsolatedService"
    __javaconstructor__ = [("()V", False)]
    START_CONTINUATION_MASK = JavaStaticField("I")
    START_FLAG_REDELIVERY = JavaStaticField("I")
    START_FLAG_RETRY = JavaStaticField("I")
    START_NOT_STICKY = JavaStaticField("I")
    START_REDELIVER_INTENT = JavaStaticField("I")
    START_STICKY = JavaStaticField("I")
    START_STICKY_COMPATIBILITY = JavaStaticField("I")
    STOP_FOREGROUND_DETACH = JavaStaticField("I")
    STOP_FOREGROUND_LEGACY = JavaStaticField("I")
    STOP_FOREGROUND_REMOVE = JavaStaticField("I")
    TRIM_MEMORY_BACKGROUND = JavaStaticField("I")
    TRIM_MEMORY_COMPLETE = JavaStaticField("I")
    TRIM_MEMORY_MODERATE = JavaStaticField("I")
    TRIM_MEMORY_RUNNING_CRITICAL = JavaStaticField("I")
    TRIM_MEMORY_RUNNING_LOW = JavaStaticField("I")
    TRIM_MEMORY_RUNNING_MODERATE = JavaStaticField("I")
    TRIM_MEMORY_UI_HIDDEN = JavaStaticField("I")
    ACCESSIBILITY_SERVICE = JavaStaticField("Ljava/lang/String;")
    ACCOUNT_SERVICE = JavaStaticField("Ljava/lang/String;")
    ACTIVITY_SERVICE = JavaStaticField("Ljava/lang/String;")
    ADVANCED_PROTECTION_SERVICE = JavaStaticField("Ljava/lang/String;")
    ALARM_SERVICE = JavaStaticField("Ljava/lang/String;")
    APPWIDGET_SERVICE = JavaStaticField("Ljava/lang/String;")
    APP_FUNCTION_SERVICE = JavaStaticField("Ljava/lang/String;")
    APP_OPS_SERVICE = JavaStaticField("Ljava/lang/String;")
    APP_SEARCH_SERVICE = JavaStaticField("Ljava/lang/String;")
    AUDIO_SERVICE = JavaStaticField("Ljava/lang/String;")
    BATTERY_SERVICE = JavaStaticField("Ljava/lang/String;")
    BIND_ABOVE_CLIENT = JavaStaticField("I")
    BIND_ADJUST_WITH_ACTIVITY = JavaStaticField("I")
    BIND_ALLOW_ACTIVITY_STARTS = JavaStaticField("I")
    BIND_ALLOW_OOM_MANAGEMENT = JavaStaticField("I")
    BIND_AUTO_CREATE = JavaStaticField("I")
    BIND_DEBUG_UNBIND = JavaStaticField("I")
    BIND_EXTERNAL_SERVICE = JavaStaticField("I")
    BIND_EXTERNAL_SERVICE_LONG = JavaStaticField("J")
    BIND_IMPORTANT = JavaStaticField("I")
    BIND_INCLUDE_CAPABILITIES = JavaStaticField("I")
    BIND_NOT_FOREGROUND = JavaStaticField("I")
    BIND_NOT_PERCEPTIBLE = JavaStaticField("I")
    BIND_PACKAGE_ISOLATED_PROCESS = JavaStaticField("I")
    BIND_SHARED_ISOLATED_PROCESS = JavaStaticField("I")
    BIND_WAIVE_PRIORITY = JavaStaticField("I")
    BIOMETRIC_SERVICE = JavaStaticField("Ljava/lang/String;")
    BLOB_STORE_SERVICE = JavaStaticField("Ljava/lang/String;")
    BLUETOOTH_SERVICE = JavaStaticField("Ljava/lang/String;")
    BUGREPORT_SERVICE = JavaStaticField("Ljava/lang/String;")
    CAMERA_SERVICE = JavaStaticField("Ljava/lang/String;")
    CAPTIONING_SERVICE = JavaStaticField("Ljava/lang/String;")
    CARRIER_CONFIG_SERVICE = JavaStaticField("Ljava/lang/String;")
    CLIPBOARD_SERVICE = JavaStaticField("Ljava/lang/String;")
    COMPANION_DEVICE_SERVICE = JavaStaticField("Ljava/lang/String;")
    CONNECTIVITY_DIAGNOSTICS_SERVICE = JavaStaticField("Ljava/lang/String;")
    CONNECTIVITY_SERVICE = JavaStaticField("Ljava/lang/String;")
    CONSUMER_IR_SERVICE = JavaStaticField("Ljava/lang/String;")
    CONTACT_KEYS_SERVICE = JavaStaticField("Ljava/lang/String;")
    CONTEXT_IGNORE_SECURITY = JavaStaticField("I")
    CONTEXT_INCLUDE_CODE = JavaStaticField("I")
    CONTEXT_RESTRICTED = JavaStaticField("I")
    CREDENTIAL_SERVICE = JavaStaticField("Ljava/lang/String;")
    CROSS_PROFILE_APPS_SERVICE = JavaStaticField("Ljava/lang/String;")
    DEVICE_ID_DEFAULT = JavaStaticField("I")
    DEVICE_ID_INVALID = JavaStaticField("I")
    DEVICE_LOCK_SERVICE = JavaStaticField("Ljava/lang/String;")
    DEVICE_POLICY_SERVICE = JavaStaticField("Ljava/lang/String;")
    DISPLAY_HASH_SERVICE = JavaStaticField("Ljava/lang/String;")
    DISPLAY_SERVICE = JavaStaticField("Ljava/lang/String;")
    DOMAIN_VERIFICATION_SERVICE = JavaStaticField("Ljava/lang/String;")
    DOWNLOAD_SERVICE = JavaStaticField("Ljava/lang/String;")
    DROPBOX_SERVICE = JavaStaticField("Ljava/lang/String;")
    EUICC_SERVICE = JavaStaticField("Ljava/lang/String;")
    FILE_INTEGRITY_SERVICE = JavaStaticField("Ljava/lang/String;")
    FINGERPRINT_SERVICE = JavaStaticField("Ljava/lang/String;")
    GAME_SERVICE = JavaStaticField("Ljava/lang/String;")
    GRAMMATICAL_INFLECTION_SERVICE = JavaStaticField("Ljava/lang/String;")
    HARDWARE_PROPERTIES_SERVICE = JavaStaticField("Ljava/lang/String;")
    HEALTHCONNECT_SERVICE = JavaStaticField("Ljava/lang/String;")
    INPUT_METHOD_SERVICE = JavaStaticField("Ljava/lang/String;")
    INPUT_SERVICE = JavaStaticField("Ljava/lang/String;")
    IPSEC_SERVICE = JavaStaticField("Ljava/lang/String;")
    JOB_SCHEDULER_SERVICE = JavaStaticField("Ljava/lang/String;")
    KEYGUARD_SERVICE = JavaStaticField("Ljava/lang/String;")
    KEYSTORE_SERVICE = JavaStaticField("Ljava/lang/String;")
    LAUNCHER_APPS_SERVICE = JavaStaticField("Ljava/lang/String;")
    LAYOUT_INFLATER_SERVICE = JavaStaticField("Ljava/lang/String;")
    LOCALE_SERVICE = JavaStaticField("Ljava/lang/String;")
    LOCATION_SERVICE = JavaStaticField("Ljava/lang/String;")
    MEDIA_COMMUNICATION_SERVICE = JavaStaticField("Ljava/lang/String;")
    MEDIA_METRICS_SERVICE = JavaStaticField("Ljava/lang/String;")
    MEDIA_PROJECTION_SERVICE = JavaStaticField("Ljava/lang/String;")
    MEDIA_QUALITY_SERVICE = JavaStaticField("Ljava/lang/String;")
    MEDIA_ROUTER_SERVICE = JavaStaticField("Ljava/lang/String;")
    MEDIA_SESSION_SERVICE = JavaStaticField("Ljava/lang/String;")
    MIDI_SERVICE = JavaStaticField("Ljava/lang/String;")
    MODE_APPEND = JavaStaticField("I")
    MODE_ENABLE_WRITE_AHEAD_LOGGING = JavaStaticField("I")
    MODE_MULTI_PROCESS = JavaStaticField("I")
    MODE_NO_LOCALIZED_COLLATORS = JavaStaticField("I")
    MODE_PRIVATE = JavaStaticField("I")
    MODE_WORLD_READABLE = JavaStaticField("I")
    MODE_WORLD_WRITEABLE = JavaStaticField("I")
    NETWORK_STATS_SERVICE = JavaStaticField("Ljava/lang/String;")
    NFC_SERVICE = JavaStaticField("Ljava/lang/String;")
    NOTIFICATION_SERVICE = JavaStaticField("Ljava/lang/String;")
    NSD_SERVICE = JavaStaticField("Ljava/lang/String;")
    OVERLAY_SERVICE = JavaStaticField("Ljava/lang/String;")
    PEOPLE_SERVICE = JavaStaticField("Ljava/lang/String;")
    PERFORMANCE_HINT_SERVICE = JavaStaticField("Ljava/lang/String;")
    PERSISTENT_DATA_BLOCK_SERVICE = JavaStaticField("Ljava/lang/String;")
    POWER_SERVICE = JavaStaticField("Ljava/lang/String;")
    PRINT_SERVICE = JavaStaticField("Ljava/lang/String;")
    PROFILING_SERVICE = JavaStaticField("Ljava/lang/String;")
    RECEIVER_EXPORTED = JavaStaticField("I")
    RECEIVER_NOT_EXPORTED = JavaStaticField("I")
    RECEIVER_VISIBLE_TO_INSTANT_APPS = JavaStaticField("I")
    RESTRICTIONS_SERVICE = JavaStaticField("Ljava/lang/String;")
    ROLE_SERVICE = JavaStaticField("Ljava/lang/String;")
    SATELLITE_SERVICE = JavaStaticField("Ljava/lang/String;")
    SEARCH_SERVICE = JavaStaticField("Ljava/lang/String;")
    SECURITY_STATE_SERVICE = JavaStaticField("Ljava/lang/String;")
    SENSOR_SERVICE = JavaStaticField("Ljava/lang/String;")
    SHORTCUT_SERVICE = JavaStaticField("Ljava/lang/String;")
    STATUS_BAR_SERVICE = JavaStaticField("Ljava/lang/String;")
    STORAGE_SERVICE = JavaStaticField("Ljava/lang/String;")
    STORAGE_STATS_SERVICE = JavaStaticField("Ljava/lang/String;")
    SYSTEM_HEALTH_SERVICE = JavaStaticField("Ljava/lang/String;")
    TELECOM_SERVICE = JavaStaticField("Ljava/lang/String;")
    TELEPHONY_IMS_SERVICE = JavaStaticField("Ljava/lang/String;")
    TELEPHONY_SERVICE = JavaStaticField("Ljava/lang/String;")
    TELEPHONY_SUBSCRIPTION_SERVICE = JavaStaticField("Ljava/lang/String;")
    TETHERING_SERVICE = JavaStaticField("Ljava/lang/String;")
    TEXT_CLASSIFICATION_SERVICE = JavaStaticField("Ljava/lang/String;")
    TEXT_SERVICES_MANAGER_SERVICE = JavaStaticField("Ljava/lang/String;")
    TV_AD_SERVICE = JavaStaticField("Ljava/lang/String;")
    TV_INPUT_SERVICE = JavaStaticField("Ljava/lang/String;")
    TV_INTERACTIVE_APP_SERVICE = JavaStaticField("Ljava/lang/String;")
    UI_MODE_SERVICE = JavaStaticField("Ljava/lang/String;")
    USAGE_STATS_SERVICE = JavaStaticField("Ljava/lang/String;")
    USB_SERVICE = JavaStaticField("Ljava/lang/String;")
    USER_SERVICE = JavaStaticField("Ljava/lang/String;")
    VIBRATOR_MANAGER_SERVICE = JavaStaticField("Ljava/lang/String;")
    VIBRATOR_SERVICE = JavaStaticField("Ljava/lang/String;")
    VIRTUAL_DEVICE_SERVICE = JavaStaticField("Ljava/lang/String;")
    VPN_MANAGEMENT_SERVICE = JavaStaticField("Ljava/lang/String;")
    WALLPAPER_SERVICE = JavaStaticField("Ljava/lang/String;")
    WIFI_AWARE_SERVICE = JavaStaticField("Ljava/lang/String;")
    WIFI_P2P_SERVICE = JavaStaticField("Ljava/lang/String;")
    WIFI_RTT_RANGING_SERVICE = JavaStaticField("Ljava/lang/String;")
    WIFI_SERVICE = JavaStaticField("Ljava/lang/String;")
    WINDOW_SERVICE = JavaStaticField("Ljava/lang/String;")
    getUserData = JavaMethod("(Landroid/adservices/ondevicepersonalization/RequestToken;)Landroid/adservices/ondevicepersonalization/UserData;")
    onBind = JavaMethod("(Landroid/content/Intent;)Landroid/os/IBinder;")
    onCreate = JavaMethod("()V")
    getFederatedComputeScheduler = JavaMethod("(Landroid/adservices/ondevicepersonalization/RequestToken;)Landroid/adservices/ondevicepersonalization/FederatedComputeScheduler;")
    getLocalData = JavaMethod("(Landroid/adservices/ondevicepersonalization/RequestToken;)Landroid/adservices/ondevicepersonalization/MutableKeyValueStore;")
    getEventUrlProvider = JavaMethod("(Landroid/adservices/ondevicepersonalization/RequestToken;)Landroid/adservices/ondevicepersonalization/EventUrlProvider;")
    getLogReader = JavaMethod("(Landroid/adservices/ondevicepersonalization/RequestToken;)Landroid/adservices/ondevicepersonalization/LogReader;")
    getModelManager = JavaMethod("(Landroid/adservices/ondevicepersonalization/RequestToken;)Landroid/adservices/ondevicepersonalization/ModelManager;")
    getRemoteData = JavaMethod("(Landroid/adservices/ondevicepersonalization/RequestToken;)Landroid/adservices/ondevicepersonalization/KeyValueStore;")
    onRequest = JavaMethod("(Landroid/adservices/ondevicepersonalization/RequestToken;)Landroid/adservices/ondevicepersonalization/IsolatedWorker;")

class ExecuteInIsolatedServiceRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/ExecuteInIsolatedServiceRequest"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getService = JavaMethod("()Landroid/content/ComponentName;")
    getAppParams = JavaMethod("()Landroid/os/PersistableBundle;")
    getOutputSpec = JavaMethod("()Landroid/adservices/ondevicepersonalization/ExecuteInIsolatedServiceRequest$OutputSpec;")

    class OutputSpec(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/ondevicepersonalization/ExecuteInIsolatedServiceRequest$OutputSpec"
        DEFAULT = JavaStaticField("Landroid/adservices/ondevicepersonalization/ExecuteInIsolatedServiceRequest$OutputSpec;")
        OUTPUT_TYPE_BEST_VALUE = JavaStaticField("I")
        OUTPUT_TYPE_NULL = JavaStaticField("I")
        buildBestValueSpec = JavaStaticMethod("(I)Landroid/adservices/ondevicepersonalization/ExecuteInIsolatedServiceRequest$OutputSpec;")
        getOutputType = JavaMethod("()I")
        getMaxIntValue = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/ondevicepersonalization/ExecuteInIsolatedServiceRequest$Builder"
        __javaconstructor__ = [("(Landroid/content/ComponentName;)V", False)]
        build = JavaMethod("()Landroid/adservices/ondevicepersonalization/ExecuteInIsolatedServiceRequest;")
        setAppParams = JavaMethod("(Landroid/os/PersistableBundle;)Landroid/adservices/ondevicepersonalization/ExecuteInIsolatedServiceRequest$Builder;")
        setOutputSpec = JavaMethod("(Landroid/adservices/ondevicepersonalization/ExecuteInIsolatedServiceRequest$OutputSpec;)Landroid/adservices/ondevicepersonalization/ExecuteInIsolatedServiceRequest$Builder;")

class ExecuteInIsolatedServiceResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/ExecuteInIsolatedServiceResponse"
    __javaconstructor__ = [("(Landroid/adservices/ondevicepersonalization/SurfacePackageToken;I)V", False)]
    DEFAULT_BEST_VALUE = JavaStaticField("I")
    getBestValue = JavaMethod("()I")
    getSurfacePackageToken = JavaMethod("()Landroid/adservices/ondevicepersonalization/SurfacePackageToken;")

class EventInput(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/EventInput"
    __javaconstructor__ = [("(Landroid/adservices/ondevicepersonalization/RequestLogRecord;Landroid/os/PersistableBundle;)V", False)]
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getParameters = JavaMethod("()Landroid/os/PersistableBundle;")
    getRequestLogRecord = JavaMethod("()Landroid/adservices/ondevicepersonalization/RequestLogRecord;")

class RenderInput(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/RenderInput"
    __javaconstructor__ = [("(IILandroid/adservices/ondevicepersonalization/RenderingConfig;)V", False)]
    getRenderingConfig = JavaMethod("()Landroid/adservices/ondevicepersonalization/RenderingConfig;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getHeight = JavaMethod("()I")
    getWidth = JavaMethod("()I")

class RenderOutput(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/RenderOutput"
    getTemplateParams = JavaMethod("()Landroid/os/PersistableBundle;")
    getTemplateId = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getContent = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/ondevicepersonalization/RenderOutput$Builder"
        __javaconstructor__ = [("()V", False)]
        setTemplateId = JavaMethod("(Ljava/lang/String;)Landroid/adservices/ondevicepersonalization/RenderOutput$Builder;")
        setTemplateParams = JavaMethod("(Landroid/os/PersistableBundle;)Landroid/adservices/ondevicepersonalization/RenderOutput$Builder;")
        setContent = JavaMethod("(Ljava/lang/String;)Landroid/adservices/ondevicepersonalization/RenderOutput$Builder;")
        build = JavaMethod("()Landroid/adservices/ondevicepersonalization/RenderOutput;")

class RequestToken(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/RequestToken"

class WebTriggerOutput(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/WebTriggerOutput"
    getEventLogRecords = JavaMethod("()Ljava/util/List;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getRequestLogRecord = JavaMethod("()Landroid/adservices/ondevicepersonalization/RequestLogRecord;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/ondevicepersonalization/WebTriggerOutput$Builder"
        __javaconstructor__ = [("()V", False)]
        addEventLogRecord = JavaMethod("(Landroid/adservices/ondevicepersonalization/EventLogRecord;)Landroid/adservices/ondevicepersonalization/WebTriggerOutput$Builder;")
        setEventLogRecords = JavaMethod("(Ljava/util/List;)Landroid/adservices/ondevicepersonalization/WebTriggerOutput$Builder;")
        setRequestLogRecord = JavaMethod("(Landroid/adservices/ondevicepersonalization/RequestLogRecord;)Landroid/adservices/ondevicepersonalization/WebTriggerOutput$Builder;")
        build = JavaMethod("()Landroid/adservices/ondevicepersonalization/WebTriggerOutput;")

class TrainingExampleRecord(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/TrainingExampleRecord"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getResumptionToken = JavaMethod("()[B")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getTrainingExample = JavaMethod("()[B")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/ondevicepersonalization/TrainingExampleRecord$Builder"
        __javaconstructor__ = [("()V", False)]
        setResumptionToken = JavaMethod("([B)Landroid/adservices/ondevicepersonalization/TrainingExampleRecord$Builder;", varargs=True)
        setTrainingExample = JavaMethod("([B)Landroid/adservices/ondevicepersonalization/TrainingExampleRecord$Builder;", varargs=True)
        build = JavaMethod("()Landroid/adservices/ondevicepersonalization/TrainingExampleRecord;")

class DownloadCompletedOutput(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/DownloadCompletedOutput"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getRetainedKeys = JavaMethod("()Ljava/util/List;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/ondevicepersonalization/DownloadCompletedOutput$Builder"
        __javaconstructor__ = [("()V", False)]
        addRetainedKey = JavaMethod("(Ljava/lang/String;)Landroid/adservices/ondevicepersonalization/DownloadCompletedOutput$Builder;")
        setRetainedKeys = JavaMethod("(Ljava/util/List;)Landroid/adservices/ondevicepersonalization/DownloadCompletedOutput$Builder;")
        build = JavaMethod("()Landroid/adservices/ondevicepersonalization/DownloadCompletedOutput;")

class IsolatedServiceException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/IsolatedServiceException"
    __javaconstructor__ = [("(ILjava/lang/Throwable;)V", False), ("(ILjava/lang/String;Ljava/lang/Throwable;)V", False), ("(I)V", False)]
    getErrorCode = JavaMethod("()I")

class RequestLogRecord(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/RequestLogRecord"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getRows = JavaMethod("()Ljava/util/List;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getTime = JavaMethod("()Ljava/time/Instant;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/ondevicepersonalization/RequestLogRecord$Builder"
        __javaconstructor__ = [("()V", False)]
        setRows = JavaMethod("(Ljava/util/List;)Landroid/adservices/ondevicepersonalization/RequestLogRecord$Builder;")
        addRow = JavaMethod("(Landroid/content/ContentValues;)Landroid/adservices/ondevicepersonalization/RequestLogRecord$Builder;")
        build = JavaMethod("()Landroid/adservices/ondevicepersonalization/RequestLogRecord;")

class AppInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/AppInfo"
    __javaconstructor__ = [("(Z)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    isInstalled = JavaMethod("()Z")

class EventLogRecord(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/EventLogRecord"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getData = JavaMethod("()Landroid/content/ContentValues;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getType = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getRequestLogRecord = JavaMethod("()Landroid/adservices/ondevicepersonalization/RequestLogRecord;")
    getRowIndex = JavaMethod("()I")
    getTime = JavaMethod("()Ljava/time/Instant;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/ondevicepersonalization/EventLogRecord$Builder"
        __javaconstructor__ = [("()V", False)]
        setRequestLogRecord = JavaMethod("(Landroid/adservices/ondevicepersonalization/RequestLogRecord;)Landroid/adservices/ondevicepersonalization/EventLogRecord$Builder;")
        setData = JavaMethod("(Landroid/content/ContentValues;)Landroid/adservices/ondevicepersonalization/EventLogRecord$Builder;")
        setType = JavaMethod("(I)Landroid/adservices/ondevicepersonalization/EventLogRecord$Builder;")
        setRowIndex = JavaMethod("(I)Landroid/adservices/ondevicepersonalization/EventLogRecord$Builder;")
        build = JavaMethod("()Landroid/adservices/ondevicepersonalization/EventLogRecord;")

class KeyValueStore(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/KeyValueStore"
    get = JavaMethod("(Ljava/lang/String;)[B")
    keySet = JavaMethod("()Ljava/util/Set;")