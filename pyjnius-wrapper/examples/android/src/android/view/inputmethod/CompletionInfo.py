from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CompletionInfo"]

class CompletionInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inputmethod/CompletionInfo"
    __javaconstructor__ = [("(JILjava/lang/CharSequence;)V", False), ("(JILjava/lang/CharSequence;Ljava/lang/CharSequence;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getId = JavaMethod("()J")
    getPosition = JavaMethod("()I")
    getText = JavaMethod("()Ljava/lang/CharSequence;")
    getLabel = JavaMethod("()Ljava/lang/CharSequence;")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")