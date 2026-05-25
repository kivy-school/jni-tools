from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MeasurementManager"]

class MeasurementManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/measurement/MeasurementManager"
    MEASUREMENT_API_STATE_DISABLED = JavaStaticField("I")
    MEASUREMENT_API_STATE_ENABLED = JavaStaticField("I")
    get = JavaStaticMethod("(Landroid/content/Context;)Landroid/adservices/measurement/MeasurementManager;")
    registerSource = JavaMultipleMethod([("(Landroid/net/Uri;Landroid/view/InputEvent;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V", False, False), ("(Landroid/net/Uri;Landroid/view/InputEvent;Ljava/util/concurrent/Executor;Landroid/adservices/common/AdServicesOutcomeReceiver;)V", False, False), ("(Landroid/adservices/measurement/SourceRegistrationRequest;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V", False, False), ("(Landroid/adservices/measurement/SourceRegistrationRequest;Ljava/util/concurrent/Executor;Landroid/adservices/common/AdServicesOutcomeReceiver;)V", False, False)])
    registerWebSource = JavaMultipleMethod([("(Landroid/adservices/measurement/WebSourceRegistrationRequest;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V", False, False), ("(Landroid/adservices/measurement/WebSourceRegistrationRequest;Ljava/util/concurrent/Executor;Landroid/adservices/common/AdServicesOutcomeReceiver;)V", False, False)])
    registerWebTrigger = JavaMultipleMethod([("(Landroid/adservices/measurement/WebTriggerRegistrationRequest;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V", False, False), ("(Landroid/adservices/measurement/WebTriggerRegistrationRequest;Ljava/util/concurrent/Executor;Landroid/adservices/common/AdServicesOutcomeReceiver;)V", False, False)])
    registerTrigger = JavaMultipleMethod([("(Landroid/net/Uri;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V", False, False), ("(Landroid/net/Uri;Ljava/util/concurrent/Executor;Landroid/adservices/common/AdServicesOutcomeReceiver;)V", False, False)])
    deleteRegistrations = JavaMultipleMethod([("(Landroid/adservices/measurement/DeletionRequest;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V", False, False), ("(Landroid/adservices/measurement/DeletionRequest;Ljava/util/concurrent/Executor;Landroid/adservices/common/AdServicesOutcomeReceiver;)V", False, False)])
    getMeasurementApiStatus = JavaMultipleMethod([("(Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V", False, False), ("(Ljava/util/concurrent/Executor;Landroid/adservices/common/AdServicesOutcomeReceiver;)V", False, False)])