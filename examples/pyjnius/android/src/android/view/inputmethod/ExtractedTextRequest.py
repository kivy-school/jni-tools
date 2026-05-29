from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ExtractedTextRequest"]

class ExtractedTextRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inputmethod/ExtractedTextRequest"
    __javaconstructor__ = [("()V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    flags = JavaField("I")
    hintMaxChars = JavaField("I")
    hintMaxLines = JavaField("I")
    token = JavaField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")