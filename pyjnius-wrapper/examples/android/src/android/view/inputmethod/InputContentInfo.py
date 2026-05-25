from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InputContentInfo"]

class InputContentInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inputmethod/InputContentInfo"
    __javaconstructor__ = [("(Landroid/net/Uri;Landroid/content/ClipDescription;)V", False), ("(Landroid/net/Uri;Landroid/content/ClipDescription;Landroid/net/Uri;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getContentUri = JavaMethod("()Landroid/net/Uri;")
    getDescription = JavaMethod("()Landroid/content/ClipDescription;")
    getLinkUri = JavaMethod("()Landroid/net/Uri;")
    requestPermission = JavaMethod("()V")
    releasePermission = JavaMethod("()V")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")