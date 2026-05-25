from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UriPermission"]

class UriPermission(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/UriPermission"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    INVALID_TIME = JavaStaticField("J")
    getUri = JavaMethod("()Landroid/net/Uri;")
    isReadPermission = JavaMethod("()Z")
    isWritePermission = JavaMethod("()Z")
    getPersistedTime = JavaMethod("()J")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")