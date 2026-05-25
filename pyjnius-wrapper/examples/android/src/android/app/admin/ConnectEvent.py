from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ConnectEvent"]

class ConnectEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/admin/ConnectEvent"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getInetAddress = JavaMethod("()Ljava/net/InetAddress;")
    getPort = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")