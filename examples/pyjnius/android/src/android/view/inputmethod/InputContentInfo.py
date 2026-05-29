from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InputContentInfo"]

class InputContentInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inputmethod/InputContentInfo"
    __javaconstructor__ = [("(Landroid/net/Uri;Landroid/content/ClipDescription;)V", False), ("(Landroid/net/Uri;Landroid/content/ClipDescription;Landroid/net/Uri;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getContentUri = JavaMethod("()Landroid/net/Uri;")
    releasePermission = JavaMethod("()V")
    requestPermission = JavaMethod("()V")
    getLinkUri = JavaMethod("()Landroid/net/Uri;")
    getDescription = JavaMethod("()Landroid/content/ClipDescription;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")