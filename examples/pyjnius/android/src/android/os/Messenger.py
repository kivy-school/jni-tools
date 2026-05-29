from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Messenger"]

class Messenger(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/Messenger"
    __javaconstructor__ = [("(Landroid/os/Handler;)V", False), ("(Landroid/os/IBinder;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    writeMessengerOrNullToParcel = JavaStaticMethod("(Landroid/os/Messenger;Landroid/os/Parcel;)V")
    readMessengerOrNullFromParcel = JavaStaticMethod("(Landroid/os/Parcel;)Landroid/os/Messenger;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    send = JavaMethod("(Landroid/os/Message;)V")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getBinder = JavaMethod("()Landroid/os/IBinder;")
    describeContents = JavaMethod("()I")