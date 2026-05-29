from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UriPermission"]

class UriPermission(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/UriPermission"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    INVALID_TIME = JavaStaticField("J")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    getUri = JavaMethod("()Landroid/net/Uri;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getPersistedTime = JavaMethod("()J")
    isReadPermission = JavaMethod("()Z")
    isWritePermission = JavaMethod("()Z")