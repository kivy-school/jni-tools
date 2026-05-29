from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Signature"]

class Signature(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/pm/Signature"
    __javaconstructor__ = [("([B)V", False), ("(Ljava/lang/String;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    toChars = JavaMultipleMethod([("()[C", False, False), ("([C[I)[C", False, False)])
    toCharsString = JavaMethod("()Ljava/lang/String;")
    toByteArray = JavaMethod("()[B")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")