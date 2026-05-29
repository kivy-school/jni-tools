from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FederatedComputeScheduler"]

class FederatedComputeScheduler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/FederatedComputeScheduler"
    cancel = JavaMethod("(Landroid/adservices/ondevicepersonalization/FederatedComputeInput;)V")
    schedule = JavaMethod("(Landroid/adservices/ondevicepersonalization/FederatedComputeScheduler$Params;Landroid/adservices/ondevicepersonalization/FederatedComputeInput;)V")

    class Params(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/ondevicepersonalization/FederatedComputeScheduler$Params"
        __javaconstructor__ = [("(Landroid/adservices/ondevicepersonalization/TrainingInterval;)V", False)]
        getTrainingInterval = JavaMethod("()Landroid/adservices/ondevicepersonalization/TrainingInterval;")