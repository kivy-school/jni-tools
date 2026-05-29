from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TimelineResponse"]

class TimelineResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/tv/TimelineResponse"
    __javaconstructor__ = [("(IIILjava/lang/String;IIJJ)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    RESPONSE_RESULT_CANCEL = JavaStaticField("I")
    RESPONSE_RESULT_ERROR = JavaStaticField("I")
    RESPONSE_RESULT_OK = JavaStaticField("I")
    getUnitsPerSecond = JavaMethod("()I")
    getTicks = JavaMethod("()J")
    getWallClock = JavaMethod("()J")
    getUnitsPerTick = JavaMethod("()I")
    getSelector = JavaMethod("()Landroid/net/Uri;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")