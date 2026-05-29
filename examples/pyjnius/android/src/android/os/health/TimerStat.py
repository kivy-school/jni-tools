from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TimerStat"]

class TimerStat(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/health/TimerStat"
    __javaconstructor__ = [("(IJ)V", False), ("(Landroid/os/Parcel;)V", False), ("()V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    setCount = JavaMethod("(I)V")
    getCount = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getTime = JavaMethod("()J")
    setTime = JavaMethod("(J)V")