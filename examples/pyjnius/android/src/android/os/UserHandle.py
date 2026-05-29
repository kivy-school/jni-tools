from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UserHandle"]

class UserHandle(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/UserHandle"
    __javaconstructor__ = [("(Landroid/os/Parcel;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMultipleMethod([("(Landroid/os/UserHandle;Landroid/os/Parcel;)V", True, False), ("(Landroid/os/Parcel;I)V", False, False)])
    readFromParcel = JavaStaticMethod("(Landroid/os/Parcel;)Landroid/os/UserHandle;")
    describeContents = JavaMethod("()I")
    getUserHandleForUid = JavaStaticMethod("(I)Landroid/os/UserHandle;")