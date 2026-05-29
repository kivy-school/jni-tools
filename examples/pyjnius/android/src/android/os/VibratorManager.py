from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VibratorManager"]

class VibratorManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/VibratorManager"
    getVibrator = JavaMethod("(I)Landroid/os/Vibrator;")
    vibrate = JavaMultipleMethod([("(Landroid/os/CombinedVibration;)V", False, False), ("(Landroid/os/CombinedVibration;Landroid/os/VibrationAttributes;)V", False, False)])
    getVibratorIds = JavaMethod("()[I")
    getDefaultVibrator = JavaMethod("()Landroid/os/Vibrator;")
    cancel = JavaMethod("()V")