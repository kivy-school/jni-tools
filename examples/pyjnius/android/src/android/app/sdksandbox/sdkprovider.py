from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class SdkSandboxActivityHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/sdksandbox/sdkprovider/SdkSandboxActivityHandler"
    onActivityCreated = JavaMethod("(Landroid/app/Activity;)V")

class SdkSandboxClientImportanceListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/sdksandbox/sdkprovider/SdkSandboxClientImportanceListener"
    onForegroundImportanceChanged = JavaMethod("(Z)V")

class SdkSandboxController(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/sdksandbox/sdkprovider/SdkSandboxController"
    SDK_SANDBOX_CONTROLLER_SERVICE = JavaStaticField("Ljava/lang/String;")
    getClientPackageName = JavaMethod("()Ljava/lang/String;")
    getClientSharedPreferences = JavaMethod("()Landroid/content/SharedPreferences;")
    registerSdkSandboxActivityHandler = JavaMethod("(Landroid/app/sdksandbox/sdkprovider/SdkSandboxActivityHandler;)Landroid/os/IBinder;")
    registerSdkSandboxClientImportanceListener = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/app/sdksandbox/sdkprovider/SdkSandboxClientImportanceListener;)V")
    unregisterSdkSandboxActivityHandler = JavaMethod("(Landroid/app/sdksandbox/sdkprovider/SdkSandboxActivityHandler;)V")
    unregisterSdkSandboxClientImportanceListener = JavaMethod("(Landroid/app/sdksandbox/sdkprovider/SdkSandboxClientImportanceListener;)V")
    getAppOwnedSdkSandboxInterfaces = JavaMethod("()Ljava/util/List;")
    getSandboxedSdks = JavaMethod("()Ljava/util/List;")
    loadSdk = JavaMethod("(Ljava/lang/String;Landroid/os/Bundle;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")