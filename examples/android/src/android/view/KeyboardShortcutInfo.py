from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["KeyboardShortcutInfo"]

class KeyboardShortcutInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/KeyboardShortcutInfo"
    __javaconstructor__ = [("(Ljava/lang/CharSequence;II)V", False), ("(Ljava/lang/CharSequence;CI)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getLabel = JavaMethod("()Ljava/lang/CharSequence;")
    getKeycode = JavaMethod("()I")
    getBaseCharacter = JavaMethod("()C")
    getModifiers = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")