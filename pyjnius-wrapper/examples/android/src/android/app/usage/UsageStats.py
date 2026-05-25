from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UsageStats"]

class UsageStats(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/usage/UsageStats"
    __javaconstructor__ = [("(Landroid/app/usage/UsageStats;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getPackageName = JavaMethod("()Ljava/lang/String;")
    getFirstTimeStamp = JavaMethod("()J")
    getLastTimeStamp = JavaMethod("()J")
    getLastTimeUsed = JavaMethod("()J")
    getLastTimeVisible = JavaMethod("()J")
    getTotalTimeInForeground = JavaMethod("()J")
    getTotalTimeVisible = JavaMethod("()J")
    getLastTimeForegroundServiceUsed = JavaMethod("()J")
    getTotalTimeForegroundServiceUsed = JavaMethod("()J")
    add = JavaMethod("(Landroid/app/usage/UsageStats;)V")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")