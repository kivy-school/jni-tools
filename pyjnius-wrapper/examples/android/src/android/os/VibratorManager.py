from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VibratorManager"]

class VibratorManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/VibratorManager"
    getVibratorIds = JavaMethod("()[I")
    getVibrator = JavaMethod("(I)Landroid/os/Vibrator;")
    getDefaultVibrator = JavaMethod("()Landroid/os/Vibrator;")
    vibrate = JavaMultipleMethod([("(Landroid/os/CombinedVibration;)V", False, False), ("(Landroid/os/CombinedVibration;Landroid/os/VibrationAttributes;)V", False, False)])
    cancel = JavaMethod("()V")