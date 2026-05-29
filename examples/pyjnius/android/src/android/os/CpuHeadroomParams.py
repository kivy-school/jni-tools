from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CpuHeadroomParams"]

class CpuHeadroomParams(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/CpuHeadroomParams"
    CPU_HEADROOM_CALCULATION_TYPE_AVERAGE = JavaStaticField("I")
    CPU_HEADROOM_CALCULATION_TYPE_MIN = JavaStaticField("I")
    toBuilder = JavaMethod("()Landroid/os/CpuHeadroomParams$Builder;")
    getCalculationWindowMillis = JavaMethod("()J")
    getCalculationType = JavaMethod("()I")
    getTids = JavaMethod("()[I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/os/CpuHeadroomParams$Builder"
        __javaconstructor__ = [("(Landroid/os/CpuHeadroomParams;)V", False), ("()V", False)]
        setTids = JavaMethod("([I)Landroid/os/CpuHeadroomParams$Builder;", varargs=True)
        setCalculationWindowMillis = JavaMethod("(I)Landroid/os/CpuHeadroomParams$Builder;")
        setCalculationType = JavaMethod("(I)Landroid/os/CpuHeadroomParams$Builder;")
        build = JavaMethod("()Landroid/os/CpuHeadroomParams;")