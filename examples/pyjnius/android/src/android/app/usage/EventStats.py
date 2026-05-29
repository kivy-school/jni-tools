from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EventStats"]

class EventStats(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/usage/EventStats"
    __javaconstructor__ = [("(Landroid/app/usage/EventStats;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getLastEventTime = JavaMethod("()J")
    getTotalTime = JavaMethod("()J")
    getFirstTimeStamp = JavaMethod("()J")
    getLastTimeStamp = JavaMethod("()J")
    add = JavaMethod("(Landroid/app/usage/EventStats;)V")
    getCount = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getEventType = JavaMethod("()I")