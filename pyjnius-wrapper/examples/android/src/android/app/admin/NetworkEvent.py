from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NetworkEvent"]

class NetworkEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/admin/NetworkEvent"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getPackageName = JavaMethod("()Ljava/lang/String;")
    getTimestamp = JavaMethod("()J")
    getId = JavaMethod("()J")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")