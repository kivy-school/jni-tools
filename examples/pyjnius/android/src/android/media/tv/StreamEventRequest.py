from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StreamEventRequest"]

class StreamEventRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/tv/StreamEventRequest"
    __javaconstructor__ = [("(IILandroid/net/Uri;Ljava/lang/String;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getTargetUri = JavaMethod("()Landroid/net/Uri;")
    getEventName = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")