from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UsageStats"]

class UsageStats(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/usage/UsageStats"
    __javaconstructor__ = [("(Landroid/app/usage/UsageStats;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getLastTimeVisible = JavaMethod("()J")
    getTotalTimeForegroundServiceUsed = JavaMethod("()J")
    getTotalTimeInForeground = JavaMethod("()J")
    getTotalTimeVisible = JavaMethod("()J")
    getLastTimeForegroundServiceUsed = JavaMethod("()J")
    getLastTimeUsed = JavaMethod("()J")
    getFirstTimeStamp = JavaMethod("()J")
    getLastTimeStamp = JavaMethod("()J")
    add = JavaMethod("(Landroid/app/usage/UsageStats;)V")
    getPackageName = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")