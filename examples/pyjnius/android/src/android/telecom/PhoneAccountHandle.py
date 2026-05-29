from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PhoneAccountHandle"]

class PhoneAccountHandle(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telecom/PhoneAccountHandle"
    __javaconstructor__ = [("(Landroid/content/ComponentName;Ljava/lang/String;)V", False), ("(Landroid/content/ComponentName;Ljava/lang/String;Landroid/os/UserHandle;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getId = JavaMethod("()Ljava/lang/String;")
    getUserHandle = JavaMethod("()Landroid/os/UserHandle;")
    getComponentName = JavaMethod("()Landroid/content/ComponentName;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")