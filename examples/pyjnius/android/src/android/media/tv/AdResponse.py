from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdResponse"]

class AdResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/tv/AdResponse"
    __javaconstructor__ = [("(IIJ)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    RESPONSE_TYPE_BUFFERING = JavaStaticField("I")
    RESPONSE_TYPE_ERROR = JavaStaticField("I")
    RESPONSE_TYPE_FINISHED = JavaStaticField("I")
    RESPONSE_TYPE_PLAYING = JavaStaticField("I")
    RESPONSE_TYPE_STOPPED = JavaStaticField("I")
    getId = JavaMethod("()I")
    getResponseType = JavaMethod("()I")
    getElapsedTimeMillis = JavaMethod("()J")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")