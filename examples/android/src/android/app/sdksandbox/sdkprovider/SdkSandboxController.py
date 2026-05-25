from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SdkSandboxController"]

class SdkSandboxController(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/sdksandbox/sdkprovider/SdkSandboxController"
    SDK_SANDBOX_CONTROLLER_SERVICE = JavaStaticField("Ljava/lang/String;")
    getAppOwnedSdkSandboxInterfaces = JavaMethod("()Ljava/util/List;")
    getSandboxedSdks = JavaMethod("()Ljava/util/List;")
    loadSdk = JavaMethod("(Ljava/lang/String;Landroid/os/Bundle;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    getClientSharedPreferences = JavaMethod("()Landroid/content/SharedPreferences;")
    registerSdkSandboxActivityHandler = JavaMethod("(Landroid/app/sdksandbox/sdkprovider/SdkSandboxActivityHandler;)Landroid/os/IBinder;")
    unregisterSdkSandboxActivityHandler = JavaMethod("(Landroid/app/sdksandbox/sdkprovider/SdkSandboxActivityHandler;)V")
    getClientPackageName = JavaMethod("()Ljava/lang/String;")