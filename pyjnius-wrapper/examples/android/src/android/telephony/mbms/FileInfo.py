from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FileInfo"]

class FileInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/mbms/FileInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getUri = JavaMethod("()Landroid/net/Uri;")
    getMimeType = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")