from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ProtectedSignalsManager"]

class ProtectedSignalsManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/signals/ProtectedSignalsManager"
    get = JavaStaticMethod("(Landroid/content/Context;)Landroid/adservices/signals/ProtectedSignalsManager;")
    updateSignals = JavaMethod("(Landroid/adservices/signals/UpdateSignalsRequest;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")