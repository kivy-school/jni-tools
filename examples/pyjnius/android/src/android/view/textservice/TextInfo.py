from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TextInfo"]

class TextInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/textservice/TextInfo"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;II)V", False), ("(Ljava/lang/CharSequence;IIII)V", False), ("(Landroid/os/Parcel;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getText = JavaMethod("()Ljava/lang/String;")
    getCharSequence = JavaMethod("()Ljava/lang/CharSequence;")
    getCookie = JavaMethod("()I")
    getSequence = JavaMethod("()I")
    describeContents = JavaMethod("()I")