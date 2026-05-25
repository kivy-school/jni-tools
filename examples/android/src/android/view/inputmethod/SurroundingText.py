from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SurroundingText"]

class SurroundingText(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inputmethod/SurroundingText"
    __javaconstructor__ = [("(Ljava/lang/CharSequence;III)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getText = JavaMethod("()Ljava/lang/CharSequence;")
    getSelectionStart = JavaMethod("()I")
    getSelectionEnd = JavaMethod("()I")
    getOffset = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")