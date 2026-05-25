from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IsolatedWorker"]

class IsolatedWorker(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/IsolatedWorker"
    onExecute = JavaMethod("(Landroid/adservices/ondevicepersonalization/ExecuteInput;Landroid/os/OutcomeReceiver;)V")
    onDownloadCompleted = JavaMethod("(Landroid/adservices/ondevicepersonalization/DownloadCompletedInput;Landroid/os/OutcomeReceiver;)V")
    onRender = JavaMethod("(Landroid/adservices/ondevicepersonalization/RenderInput;Landroid/os/OutcomeReceiver;)V")
    onEvent = JavaMethod("(Landroid/adservices/ondevicepersonalization/EventInput;Landroid/os/OutcomeReceiver;)V")
    onTrainingExamples = JavaMethod("(Landroid/adservices/ondevicepersonalization/TrainingExamplesInput;Landroid/os/OutcomeReceiver;)V")
    onWebTrigger = JavaMethod("(Landroid/adservices/ondevicepersonalization/WebTriggerInput;Landroid/os/OutcomeReceiver;)V")