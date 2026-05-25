from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CombinedVibration"]

class CombinedVibration(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/CombinedVibration"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    createParallel = JavaStaticMethod("(Landroid/os/VibrationEffect;)Landroid/os/CombinedVibration;")
    startParallel = JavaStaticMethod("()Landroid/os/CombinedVibration$ParallelCombination;")
    describeContents = JavaMethod("()I")

    class ParallelCombination(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/os/CombinedVibration/ParallelCombination"
        addVibrator = JavaMethod("(ILandroid/os/VibrationEffect;)Landroid/os/CombinedVibration$ParallelCombination;")
        combine = JavaMethod("()Landroid/os/CombinedVibration;")