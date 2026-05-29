from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AitInfo"]

class AitInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/tv/AitInfo"
    __javaconstructor__ = [("(II)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getType = JavaMethod("()I")
    getVersion = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    toString = JavaMethod("()Ljava/lang/String;")