from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdRequest"]

class AdRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/tv/AdRequest"
    __javaconstructor__ = [("(IILandroid/os/ParcelFileDescriptor;JJJLjava/lang/String;Landroid/os/Bundle;)V", False), ("(IILandroid/net/Uri;JJJLandroid/os/Bundle;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    REQUEST_TYPE_START = JavaStaticField("I")
    REQUEST_TYPE_STOP = JavaStaticField("I")
    getId = JavaMethod("()I")
    getRequestType = JavaMethod("()I")
    getFileDescriptor = JavaMethod("()Landroid/os/ParcelFileDescriptor;")
    getUri = JavaMethod("()Landroid/net/Uri;")
    getStartTimeMillis = JavaMethod("()J")
    getStopTimeMillis = JavaMethod("()J")
    getEchoIntervalMillis = JavaMethod("()J")
    getMediaFileType = JavaMethod("()Ljava/lang/String;")
    getMetadata = JavaMethod("()Landroid/os/Bundle;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")