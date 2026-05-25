from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NotificationChannelGroup"]

class NotificationChannelGroup(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/NotificationChannelGroup"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/CharSequence;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getId = JavaMethod("()Ljava/lang/String;")
    getName = JavaMethod("()Ljava/lang/CharSequence;")
    getDescription = JavaMethod("()Ljava/lang/String;")
    getChannels = JavaMethod("()Ljava/util/List;")
    isBlocked = JavaMethod("()Z")
    setDescription = JavaMethod("(Ljava/lang/String;)V")
    describeContents = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    clone = JavaMethod("()Landroid/app/NotificationChannelGroup;")
    toString = JavaMethod("()Ljava/lang/String;")