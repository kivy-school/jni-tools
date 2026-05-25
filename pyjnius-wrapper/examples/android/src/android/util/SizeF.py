from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SizeF"]

class SizeF(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/SizeF"
    __javaconstructor__ = [("(FF)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getWidth = JavaMethod("()F")
    getHeight = JavaMethod("()F")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    parseSizeF = JavaStaticMethod("(Ljava/lang/String;)Landroid/util/SizeF;")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")