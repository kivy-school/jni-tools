from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VibratorFrequencyProfile"]

class VibratorFrequencyProfile(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/vibrator/VibratorFrequencyProfile"
    getMaxFrequencyHz = JavaMethod("()F")
    getFrequencyRange = JavaMethod("(F)Landroid/util/Range;")
    getFrequenciesOutputAcceleration = JavaMethod("()Landroid/util/SparseArray;")
    getMaxOutputAccelerationGs = JavaMethod("()F")
    getMinFrequencyHz = JavaMethod("()F")
    getOutputAccelerationGs = JavaMethod("(F)F")