from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StreamEventResponse"]

class StreamEventResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/tv/StreamEventResponse"
    __javaconstructor__ = [("(IIIIJ[B)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getEventId = JavaMethod("()I")
    getNptMillis = JavaMethod("()J")
    getData = JavaMethod("()[B")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")