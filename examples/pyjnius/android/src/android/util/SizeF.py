from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SizeF"]

class SizeF(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/SizeF"
    __javaconstructor__ = [("(FF)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getHeight = JavaMethod("()F")
    getWidth = JavaMethod("()F")
    parseSizeF = JavaStaticMethod("(Ljava/lang/String;)Landroid/util/SizeF;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")