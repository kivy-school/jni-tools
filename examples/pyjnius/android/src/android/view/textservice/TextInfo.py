from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TextInfo"]

class TextInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/textservice/TextInfo"
    __javaconstructor__ = [("(Ljava/lang/String;II)V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/lang/CharSequence;IIII)V", False), ("(Landroid/os/Parcel;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getSequence = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getCharSequence = JavaMethod("()Ljava/lang/CharSequence;")
    describeContents = JavaMethod("()I")
    getCookie = JavaMethod("()I")
    getText = JavaMethod("()Ljava/lang/String;")