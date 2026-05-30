from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class AppOwnedSdkSandboxInterface(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/sdksandbox/AppOwnedSdkSandboxInterface"
    __javaconstructor__ = [("(Ljava/lang/String;JLandroid/os/IBinder;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getVersion = JavaMethod("()J")
    getName = JavaMethod("()Ljava/lang/String;")
    getInterface = JavaMethod("()Landroid/os/IBinder;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

class SdkSandboxManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/sdksandbox/SdkSandboxManager"
    EXTRA_DISPLAY_ID = JavaStaticField("Ljava/lang/String;")
    EXTRA_HEIGHT_IN_PIXELS = JavaStaticField("Ljava/lang/String;")
    EXTRA_HOST_TOKEN = JavaStaticField("Ljava/lang/String;")
    EXTRA_SURFACE_PACKAGE = JavaStaticField("Ljava/lang/String;")
    EXTRA_WIDTH_IN_PIXELS = JavaStaticField("Ljava/lang/String;")
    LOAD_SDK_ALREADY_LOADED = JavaStaticField("I")
    LOAD_SDK_INTERNAL_ERROR = JavaStaticField("I")
    LOAD_SDK_NOT_FOUND = JavaStaticField("I")
    LOAD_SDK_SDK_DEFINED_ERROR = JavaStaticField("I")
    LOAD_SDK_SDK_SANDBOX_DISABLED = JavaStaticField("I")
    REQUEST_SURFACE_PACKAGE_INTERNAL_ERROR = JavaStaticField("I")
    REQUEST_SURFACE_PACKAGE_SDK_NOT_LOADED = JavaStaticField("I")
    SDK_SANDBOX_PROCESS_NOT_AVAILABLE = JavaStaticField("I")
    SDK_SANDBOX_SERVICE = JavaStaticField("Ljava/lang/String;")
    SDK_SANDBOX_STATE_DISABLED = JavaStaticField("I")
    SDK_SANDBOX_STATE_ENABLED_PROCESS_ISOLATION = JavaStaticField("I")
    addSdkSandboxProcessDeathCallback = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/app/sdksandbox/SdkSandboxManager$SdkSandboxProcessDeathCallback;)V")
    addSyncedSharedPreferencesKeys = JavaMethod("(Ljava/util/Set;)V")
    getAppOwnedSdkSandboxInterfaces = JavaMethod("()Ljava/util/List;")
    getSandboxedSdks = JavaMethod("()Ljava/util/List;")
    getSdkSandboxState = JavaStaticMethod("()I")
    getSyncedSharedPreferencesKeys = JavaMethod("()Ljava/util/Set;")
    loadSdk = JavaMethod("(Ljava/lang/String;Landroid/os/Bundle;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    registerAppOwnedSdkSandboxInterface = JavaMethod("(Landroid/app/sdksandbox/AppOwnedSdkSandboxInterface;)V")
    removeSdkSandboxProcessDeathCallback = JavaMethod("(Landroid/app/sdksandbox/SdkSandboxManager$SdkSandboxProcessDeathCallback;)V")
    removeSyncedSharedPreferencesKeys = JavaMethod("(Ljava/util/Set;)V")
    startSdkSandboxActivity = JavaMethod("(Landroid/app/Activity;Landroid/os/IBinder;)V")
    unloadSdk = JavaMethod("(Ljava/lang/String;)V")
    unregisterAppOwnedSdkSandboxInterface = JavaMethod("(Ljava/lang/String;)V")
    requestSurfacePackage = JavaMethod("(Ljava/lang/String;Landroid/os/Bundle;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")

    class SdkSandboxProcessDeathCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/sdksandbox/SdkSandboxManager$SdkSandboxProcessDeathCallback"
        onSdkSandboxDied = JavaMethod("()V")

class SandboxedSdkProvider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/sdksandbox/SandboxedSdkProvider"
    __javaconstructor__ = [("()V", False)]
    onLoadSdk = JavaMethod("(Landroid/os/Bundle;)Landroid/app/sdksandbox/SandboxedSdk;")
    beforeUnloadSdk = JavaMethod("()V")
    attachContext = JavaMethod("(Landroid/content/Context;)V")
    getContext = JavaMethod("()Landroid/content/Context;")
    getView = JavaMethod("(Landroid/content/Context;Landroid/os/Bundle;II)Landroid/view/View;")

class LoadSdkException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/sdksandbox/LoadSdkException"
    __javaconstructor__ = [("(Ljava/lang/Throwable;Landroid/os/Bundle;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getExtraInformation = JavaMethod("()Landroid/os/Bundle;")
    getLoadSdkErrorCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

class SandboxedSdk(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/sdksandbox/SandboxedSdk"
    __javaconstructor__ = [("(Landroid/os/IBinder;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getSharedLibraryInfo = JavaMethod("()Landroid/content/pm/SharedLibraryInfo;")
    getInterface = JavaMethod("()Landroid/os/IBinder;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

class RequestSurfacePackageException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/sdksandbox/RequestSurfacePackageException"
    __javaconstructor__ = [("(ILjava/lang/String;)V", False), ("(ILjava/lang/String;Ljava/lang/Throwable;Landroid/os/Bundle;)V", False), ("(ILjava/lang/String;Ljava/lang/Throwable;)V", False)]
    getRequestSurfacePackageErrorCode = JavaMethod("()I")
    getExtraErrorInformation = JavaMethod("()Landroid/os/Bundle;")