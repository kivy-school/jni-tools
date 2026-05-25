from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CorrectionInfo"]

class CorrectionInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inputmethod/CorrectionInfo"
    __javaconstructor__ = [("(ILjava/lang/CharSequence;Ljava/lang/CharSequence;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getOffset = JavaMethod("()I")
    getOldText = JavaMethod("()Ljava/lang/CharSequence;")
    getNewText = JavaMethod("()Ljava/lang/CharSequence;")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")