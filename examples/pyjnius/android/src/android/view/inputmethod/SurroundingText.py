from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SurroundingText"]

class SurroundingText(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inputmethod/SurroundingText"
    __javaconstructor__ = [("(Ljava/lang/CharSequence;III)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getSelectionEnd = JavaMethod("()I")
    getSelectionStart = JavaMethod("()I")
    getOffset = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getText = JavaMethod("()Ljava/lang/CharSequence;")