from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ExtractedText"]

class ExtractedText(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inputmethod/ExtractedText"
    __javaconstructor__ = [("()V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    FLAG_SELECTING = JavaStaticField("I")
    FLAG_SINGLE_LINE = JavaStaticField("I")
    flags = JavaField("I")
    hint = JavaField("Ljava/lang/CharSequence;")
    partialEndOffset = JavaField("I")
    partialStartOffset = JavaField("I")
    selectionEnd = JavaField("I")
    selectionStart = JavaField("I")
    startOffset = JavaField("I")
    text = JavaField("Ljava/lang/CharSequence;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")