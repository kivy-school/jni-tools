from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ModelManager"]

class ModelManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/ModelManager"
    run = JavaMethod("(Landroid/adservices/ondevicepersonalization/InferenceInput;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")