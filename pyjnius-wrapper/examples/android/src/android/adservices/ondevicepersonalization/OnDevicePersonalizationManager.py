from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OnDevicePersonalizationManager"]

class OnDevicePersonalizationManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/OnDevicePersonalizationManager"
    execute = JavaMethod("(Landroid/content/ComponentName;Landroid/os/PersistableBundle;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    requestSurfacePackage = JavaMethod("(Landroid/adservices/ondevicepersonalization/SurfacePackageToken;Landroid/os/IBinder;IIILjava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")

    class ExecuteResult(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/ondevicepersonalization/OnDevicePersonalizationManager/ExecuteResult"
        getSurfacePackageToken = JavaMethod("()Landroid/adservices/ondevicepersonalization/SurfacePackageToken;")
        getOutputData = JavaMethod("()[B")