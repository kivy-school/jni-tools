from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TimerStat"]

class TimerStat(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/health/TimerStat"
    __javaconstructor__ = [("()V", False), ("(IJ)V", False), ("(Landroid/os/Parcel;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    setCount = JavaMethod("(I)V")
    getCount = JavaMethod("()I")
    setTime = JavaMethod("(J)V")
    getTime = JavaMethod("()J")