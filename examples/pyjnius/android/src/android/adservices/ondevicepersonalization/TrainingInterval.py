from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TrainingInterval"]

class TrainingInterval(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/TrainingInterval"
    SCHEDULING_MODE_ONE_TIME = JavaStaticField("I")
    SCHEDULING_MODE_RECURRENT = JavaStaticField("I")
    getSchedulingMode = JavaMethod("()I")
    getMinimumInterval = JavaMethod("()Ljava/time/Duration;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/ondevicepersonalization/TrainingInterval$Builder"
        __javaconstructor__ = [("()V", False)]
        setMinimumInterval = JavaMethod("(Ljava/time/Duration;)Landroid/adservices/ondevicepersonalization/TrainingInterval$Builder;")
        setSchedulingMode = JavaMethod("(I)Landroid/adservices/ondevicepersonalization/TrainingInterval$Builder;")
        build = JavaMethod("()Landroid/adservices/ondevicepersonalization/TrainingInterval;")