from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GpuHeadroomParams"]

class GpuHeadroomParams(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/GpuHeadroomParams"
    GPU_HEADROOM_CALCULATION_TYPE_AVERAGE = JavaStaticField("I")
    GPU_HEADROOM_CALCULATION_TYPE_MIN = JavaStaticField("I")
    GPU_HEADROOM_CALCULATION_WINDOW_MILLIS_MAX = JavaStaticField("I")
    GPU_HEADROOM_CALCULATION_WINDOW_MILLIS_MIN = JavaStaticField("I")
    getCalculationWindowMillis = JavaMethod("()I")
    getCalculationType = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/os/GpuHeadroomParams$Builder"
        __javaconstructor__ = [("()V", False), ("(Landroid/os/GpuHeadroomParams;)V", False)]
        setCalculationWindowMillis = JavaMethod("(I)Landroid/os/GpuHeadroomParams$Builder;")
        setCalculationType = JavaMethod("(I)Landroid/os/GpuHeadroomParams$Builder;")
        build = JavaMethod("()Landroid/os/GpuHeadroomParams;")