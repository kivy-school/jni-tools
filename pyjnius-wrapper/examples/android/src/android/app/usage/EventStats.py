from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EventStats"]

class EventStats(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/usage/EventStats"
    __javaconstructor__ = [("(Landroid/app/usage/EventStats;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getEventType = JavaMethod("()I")
    getFirstTimeStamp = JavaMethod("()J")
    getLastTimeStamp = JavaMethod("()J")
    getLastEventTime = JavaMethod("()J")
    getCount = JavaMethod("()I")
    getTotalTime = JavaMethod("()J")
    add = JavaMethod("(Landroid/app/usage/EventStats;)V")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")