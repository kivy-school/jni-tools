from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdRequest"]

class AdRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/tv/AdRequest"
    __javaconstructor__ = [("(IILandroid/net/Uri;JJJLandroid/os/Bundle;)V", False), ("(IILandroid/os/ParcelFileDescriptor;JJJLjava/lang/String;Landroid/os/Bundle;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    REQUEST_TYPE_START = JavaStaticField("I")
    REQUEST_TYPE_STOP = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getStartTimeMillis = JavaMethod("()J")
    getEchoIntervalMillis = JavaMethod("()J")
    getMediaFileType = JavaMethod("()Ljava/lang/String;")
    getStopTimeMillis = JavaMethod("()J")
    getId = JavaMethod("()I")
    getUri = JavaMethod("()Landroid/net/Uri;")
    getMetadata = JavaMethod("()Landroid/os/Bundle;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getFileDescriptor = JavaMethod("()Landroid/os/ParcelFileDescriptor;")
    getRequestType = JavaMethod("()I")