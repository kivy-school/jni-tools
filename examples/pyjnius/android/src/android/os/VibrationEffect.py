from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VibrationEffect"]

class VibrationEffect(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/VibrationEffect"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    DEFAULT_AMPLITUDE = JavaStaticField("I")
    EFFECT_CLICK = JavaStaticField("I")
    EFFECT_DOUBLE_CLICK = JavaStaticField("I")
    EFFECT_HEAVY_CLICK = JavaStaticField("I")
    EFFECT_TICK = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    createOneShot = JavaStaticMethod("(JI)Landroid/os/VibrationEffect;")
    createPredefined = JavaStaticMethod("(I)Landroid/os/VibrationEffect;")
    createRepeatingEffect = JavaMultipleMethod([("(Landroid/os/VibrationEffect;Landroid/os/VibrationEffect;)Landroid/os/VibrationEffect;", True, False), ("(Landroid/os/VibrationEffect;)Landroid/os/VibrationEffect;", True, False)])
    createWaveform = JavaMultipleMethod([("([J[II)Landroid/os/VibrationEffect;", True, False), ("([JI)Landroid/os/VibrationEffect;", True, False)])
    startComposition = JavaStaticMethod("()Landroid/os/VibrationEffect$Composition;")
    describeContents = JavaMethod("()I")

    class WaveformEnvelopeBuilder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/os/VibrationEffect$WaveformEnvelopeBuilder"
        __javaconstructor__ = [("()V", False)]
        setInitialFrequencyHz = JavaMethod("(F)Landroid/os/VibrationEffect$WaveformEnvelopeBuilder;")
        addControlPoint = JavaMethod("(FFJ)Landroid/os/VibrationEffect$WaveformEnvelopeBuilder;")
        build = JavaMethod("()Landroid/os/VibrationEffect;")

    class Composition(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/os/VibrationEffect$Composition"
        DELAY_TYPE_PAUSE = JavaStaticField("I")
        DELAY_TYPE_RELATIVE_START_OFFSET = JavaStaticField("I")
        PRIMITIVE_CLICK = JavaStaticField("I")
        PRIMITIVE_LOW_TICK = JavaStaticField("I")
        PRIMITIVE_QUICK_FALL = JavaStaticField("I")
        PRIMITIVE_QUICK_RISE = JavaStaticField("I")
        PRIMITIVE_SLOW_RISE = JavaStaticField("I")
        PRIMITIVE_SPIN = JavaStaticField("I")
        PRIMITIVE_THUD = JavaStaticField("I")
        PRIMITIVE_TICK = JavaStaticField("I")
        addPrimitive = JavaMultipleMethod([("(IFII)Landroid/os/VibrationEffect$Composition;", False, False), ("(IF)Landroid/os/VibrationEffect$Composition;", False, False), ("(I)Landroid/os/VibrationEffect$Composition;", False, False), ("(IFI)Landroid/os/VibrationEffect$Composition;", False, False)])
        compose = JavaMethod("()Landroid/os/VibrationEffect;")

    class BasicEnvelopeBuilder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/os/VibrationEffect$BasicEnvelopeBuilder"
        __javaconstructor__ = [("()V", False)]
        setInitialSharpness = JavaMethod("(F)Landroid/os/VibrationEffect$BasicEnvelopeBuilder;")
        addControlPoint = JavaMethod("(FFJ)Landroid/os/VibrationEffect$BasicEnvelopeBuilder;")
        build = JavaMethod("()Landroid/os/VibrationEffect;")