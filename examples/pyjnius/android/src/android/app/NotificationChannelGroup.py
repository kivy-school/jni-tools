from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NotificationChannelGroup"]

class NotificationChannelGroup(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/NotificationChannelGroup"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/CharSequence;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    isBlocked = JavaMethod("()Z")
    getChannels = JavaMethod("()Ljava/util/List;")
    getName = JavaMethod("()Ljava/lang/CharSequence;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    clone = JavaMultipleMethod([("()Landroid/app/NotificationChannelGroup;", False, False), ("()Ljava/lang/Object;", False, False)])
    getId = JavaMethod("()Ljava/lang/String;")
    setDescription = JavaMethod("(Ljava/lang/String;)V")
    getDescription = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")