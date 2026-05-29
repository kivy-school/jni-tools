from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Signature"]

class Signature(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/pm/Signature"
    __javaconstructor__ = [("([B)V", False), ("(Ljava/lang/String;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toChars = JavaMultipleMethod([("()[C", False, False), ("([C[I)[C", False, False)])
    toCharsString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    toByteArray = JavaMethod("()[B")