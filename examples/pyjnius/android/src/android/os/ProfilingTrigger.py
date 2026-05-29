from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ProfilingTrigger"]

class ProfilingTrigger(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/ProfilingTrigger"
    TRIGGER_TYPE_ANR = JavaStaticField("I")
    TRIGGER_TYPE_APP_FULLY_DRAWN = JavaStaticField("I")
    TRIGGER_TYPE_NONE = JavaStaticField("I")
    getTriggerType = JavaMethod("()I")
    getRateLimitingPeriodHours = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/os/ProfilingTrigger$Builder"
        __javaconstructor__ = [("(I)V", False)]
        build = JavaMethod("()Landroid/os/ProfilingTrigger;")
        setRateLimitingPeriodHours = JavaMethod("(I)Landroid/os/ProfilingTrigger$Builder;")