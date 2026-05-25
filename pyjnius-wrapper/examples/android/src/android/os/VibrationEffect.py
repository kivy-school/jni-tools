from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VibrationEffect"]

class VibrationEffect(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/VibrationEffect"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    DEFAULT_AMPLITUDE = JavaStaticField("I")
    EFFECT_CLICK = JavaStaticField("I")
    EFFECT_DOUBLE_CLICK = JavaStaticField("I")
    EFFECT_HEAVY_CLICK = JavaStaticField("I")
    EFFECT_TICK = JavaStaticField("I")
    createOneShot = JavaStaticMethod("(JI)Landroid/os/VibrationEffect;")
    createWaveform = JavaMultipleMethod([("([JI)Landroid/os/VibrationEffect;", True, False), ("([J[II)Landroid/os/VibrationEffect;", True, False)])
    createPredefined = JavaStaticMethod("(I)Landroid/os/VibrationEffect;")
    startComposition = JavaStaticMethod("()Landroid/os/VibrationEffect$Composition;")
    describeContents = JavaMethod("()I")

    class Composition(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/os/VibrationEffect/Composition"
        PRIMITIVE_CLICK = JavaStaticField("I")
        PRIMITIVE_LOW_TICK = JavaStaticField("I")
        PRIMITIVE_QUICK_FALL = JavaStaticField("I")
        PRIMITIVE_QUICK_RISE = JavaStaticField("I")
        PRIMITIVE_SLOW_RISE = JavaStaticField("I")
        PRIMITIVE_SPIN = JavaStaticField("I")
        PRIMITIVE_THUD = JavaStaticField("I")
        PRIMITIVE_TICK = JavaStaticField("I")
        addPrimitive = JavaMultipleMethod([("(I)Landroid/os/VibrationEffect$Composition;", False, False), ("(IF)Landroid/os/VibrationEffect$Composition;", False, False), ("(IFI)Landroid/os/VibrationEffect$Composition;", False, False)])
        compose = JavaMethod("()Landroid/os/VibrationEffect;")