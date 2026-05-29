from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Vibrator"]

class Vibrator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/Vibrator"
    VIBRATION_EFFECT_SUPPORT_NO = JavaStaticField("I")
    VIBRATION_EFFECT_SUPPORT_UNKNOWN = JavaStaticField("I")
    VIBRATION_EFFECT_SUPPORT_YES = JavaStaticField("I")
    vibrate = JavaMultipleMethod([("([JI)V", False, False), ("(JLandroid/media/AudioAttributes;)V", False, False), ("(J)V", False, False), ("(Landroid/os/VibrationEffect;Landroid/os/VibrationAttributes;)V", False, False), ("(Landroid/os/VibrationEffect;Landroid/media/AudioAttributes;)V", False, False), ("(Landroid/os/VibrationEffect;)V", False, False), ("([JILandroid/media/AudioAttributes;)V", False, False)])
    hasVibrator = JavaMethod("()Z")
    areAllEffectsSupported = JavaMethod("([I)I", varargs=True)
    areAllPrimitivesSupported = JavaMethod("([I)Z", varargs=True)
    areEffectsSupported = JavaMethod("([I)[I", varargs=True)
    areEnvelopeEffectsSupported = JavaMethod("()Z")
    getQFactor = JavaMethod("()F")
    arePrimitivesSupported = JavaMethod("([I)[Z", varargs=True)
    getEnvelopeEffectInfo = JavaMethod("()Landroid/os/vibrator/VibratorEnvelopeEffectInfo;")
    getFrequencyProfile = JavaMethod("()Landroid/os/vibrator/VibratorFrequencyProfile;")
    getPrimitiveDurations = JavaMethod("([I)[I", varargs=True)
    getResonantFrequency = JavaMethod("()F")
    hasAmplitudeControl = JavaMethod("()Z")
    getId = JavaMethod("()I")
    cancel = JavaMethod("()V")