from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FileServiceInfo"]

class FileServiceInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/mbms/FileServiceInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getFiles = JavaMethod("()Ljava/util/List;")