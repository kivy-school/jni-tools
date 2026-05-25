from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TimelineResponse"]

class TimelineResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/tv/TimelineResponse"
    __javaconstructor__ = [("(IIILjava/lang/String;IIJJ)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getSelector = JavaMethod("()Landroid/net/Uri;")
    getUnitsPerTick = JavaMethod("()I")
    getUnitsPerSecond = JavaMethod("()I")
    getWallClock = JavaMethod("()J")
    getTicks = JavaMethod("()J")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")