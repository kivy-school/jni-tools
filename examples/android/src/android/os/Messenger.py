from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Messenger"]

class Messenger(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/Messenger"
    __javaconstructor__ = [("(Landroid/os/Handler;)V", False), ("(Landroid/os/IBinder;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    send = JavaMethod("(Landroid/os/Message;)V")
    getBinder = JavaMethod("()Landroid/os/IBinder;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    writeMessengerOrNullToParcel = JavaStaticMethod("(Landroid/os/Messenger;Landroid/os/Parcel;)V")
    readMessengerOrNullFromParcel = JavaStaticMethod("(Landroid/os/Parcel;)Landroid/os/Messenger;")