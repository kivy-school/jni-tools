from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PhoneAccountHandle"]

class PhoneAccountHandle(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telecom/PhoneAccountHandle"
    __javaconstructor__ = [("(Landroid/content/ComponentName;Ljava/lang/String;)V", False), ("(Landroid/content/ComponentName;Ljava/lang/String;Landroid/os/UserHandle;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getComponentName = JavaMethod("()Landroid/content/ComponentName;")
    getId = JavaMethod("()Ljava/lang/String;")
    getUserHandle = JavaMethod("()Landroid/os/UserHandle;")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")