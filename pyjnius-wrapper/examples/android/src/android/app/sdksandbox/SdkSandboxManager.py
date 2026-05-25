from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SdkSandboxManager"]

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
    getSdkSandboxState = JavaStaticMethod("()I")
    addSdkSandboxProcessDeathCallback = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/app/sdksandbox/SdkSandboxManager$SdkSandboxProcessDeathCallback;)V")
    removeSdkSandboxProcessDeathCallback = JavaMethod("(Landroid/app/sdksandbox/SdkSandboxManager$SdkSandboxProcessDeathCallback;)V")
    registerAppOwnedSdkSandboxInterface = JavaMethod("(Landroid/app/sdksandbox/AppOwnedSdkSandboxInterface;)V")
    unregisterAppOwnedSdkSandboxInterface = JavaMethod("(Ljava/lang/String;)V")
    getAppOwnedSdkSandboxInterfaces = JavaMethod("()Ljava/util/List;")
    loadSdk = JavaMethod("(Ljava/lang/String;Landroid/os/Bundle;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    getSandboxedSdks = JavaMethod("()Ljava/util/List;")
    unloadSdk = JavaMethod("(Ljava/lang/String;)V")
    requestSurfacePackage = JavaMethod("(Ljava/lang/String;Landroid/os/Bundle;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    startSdkSandboxActivity = JavaMethod("(Landroid/app/Activity;Landroid/os/IBinder;)V")
    addSyncedSharedPreferencesKeys = JavaMethod("(Ljava/util/Set;)V")
    removeSyncedSharedPreferencesKeys = JavaMethod("(Ljava/util/Set;)V")
    getSyncedSharedPreferencesKeys = JavaMethod("()Ljava/util/Set;")

    class SdkSandboxProcessDeathCallback(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/sdksandbox/SdkSandboxManager/SdkSandboxProcessDeathCallback"
        onSdkSandboxDied = JavaMethod("()V")