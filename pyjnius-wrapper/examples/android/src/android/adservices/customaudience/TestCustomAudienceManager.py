from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TestCustomAudienceManager"]

class TestCustomAudienceManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/customaudience/TestCustomAudienceManager"
    overrideCustomAudienceRemoteInfo = JavaMethod("(Landroid/adservices/customaudience/AddCustomAudienceOverrideRequest;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    removeCustomAudienceRemoteInfoOverride = JavaMethod("(Landroid/adservices/customaudience/RemoveCustomAudienceOverrideRequest;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    resetAllCustomAudienceOverrides = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")