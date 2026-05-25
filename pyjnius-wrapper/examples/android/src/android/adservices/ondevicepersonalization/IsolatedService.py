from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IsolatedService"]

class IsolatedService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/IsolatedService"
    __javaconstructor__ = [("()V", False)]
    onCreate = JavaMethod("()V")
    onBind = JavaMethod("(Landroid/content/Intent;)Landroid/os/IBinder;")
    onRequest = JavaMethod("(Landroid/adservices/ondevicepersonalization/RequestToken;)Landroid/adservices/ondevicepersonalization/IsolatedWorker;")
    getRemoteData = JavaMethod("(Landroid/adservices/ondevicepersonalization/RequestToken;)Landroid/adservices/ondevicepersonalization/KeyValueStore;")
    getLocalData = JavaMethod("(Landroid/adservices/ondevicepersonalization/RequestToken;)Landroid/adservices/ondevicepersonalization/MutableKeyValueStore;")
    getLogReader = JavaMethod("(Landroid/adservices/ondevicepersonalization/RequestToken;)Landroid/adservices/ondevicepersonalization/LogReader;")
    getEventUrlProvider = JavaMethod("(Landroid/adservices/ondevicepersonalization/RequestToken;)Landroid/adservices/ondevicepersonalization/EventUrlProvider;")
    getUserData = JavaMethod("(Landroid/adservices/ondevicepersonalization/RequestToken;)Landroid/adservices/ondevicepersonalization/UserData;")
    getFederatedComputeScheduler = JavaMethod("(Landroid/adservices/ondevicepersonalization/RequestToken;)Landroid/adservices/ondevicepersonalization/FederatedComputeScheduler;")
    getModelManager = JavaMethod("(Landroid/adservices/ondevicepersonalization/RequestToken;)Landroid/adservices/ondevicepersonalization/ModelManager;")