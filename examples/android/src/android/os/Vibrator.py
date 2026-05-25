from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Vibrator"]

class Vibrator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/Vibrator"
    VIBRATION_EFFECT_SUPPORT_NO = JavaStaticField("I")
    VIBRATION_EFFECT_SUPPORT_UNKNOWN = JavaStaticField("I")
    VIBRATION_EFFECT_SUPPORT_YES = JavaStaticField("I")
    getId = JavaMethod("()I")
    hasVibrator = JavaMethod("()Z")
    hasAmplitudeControl = JavaMethod("()Z")
    getResonantFrequency = JavaMethod("()F")
    getQFactor = JavaMethod("()F")
    vibrate = JavaMultipleMethod([("(J)V", False, False), ("(JLandroid/media/AudioAttributes;)V", False, False), ("([JI)V", False, False), ("([JILandroid/media/AudioAttributes;)V", False, False), ("(Landroid/os/VibrationEffect;)V", False, False), ("(Landroid/os/VibrationEffect;Landroid/media/AudioAttributes;)V", False, False), ("(Landroid/os/VibrationEffect;Landroid/os/VibrationAttributes;)V", False, False)])
    areEffectsSupported = JavaMethod("([I)[I", varargs=True)
    areAllEffectsSupported = JavaMethod("([I)I", varargs=True)
    arePrimitivesSupported = JavaMethod("([I)[Z", varargs=True)
    areAllPrimitivesSupported = JavaMethod("([I)Z", varargs=True)
    getPrimitiveDurations = JavaMethod("([I)[I", varargs=True)
    cancel = JavaMethod("()V")