from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DsmccRequest"]

class DsmccRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/tv/DsmccRequest"
    __javaconstructor__ = [("(IILandroid/net/Uri;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getUri = JavaMethod("()Landroid/net/Uri;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")