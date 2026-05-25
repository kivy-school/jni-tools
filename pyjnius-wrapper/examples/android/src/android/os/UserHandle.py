from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UserHandle"]

class UserHandle(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/UserHandle"
    __javaconstructor__ = [("(Landroid/os/Parcel;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getUserHandleForUid = JavaStaticMethod("(I)Landroid/os/UserHandle;")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMultipleMethod([("(Landroid/os/Parcel;I)V", False, False), ("(Landroid/os/UserHandle;Landroid/os/Parcel;)V", True, False)])
    readFromParcel = JavaStaticMethod("(Landroid/os/Parcel;)Landroid/os/UserHandle;")