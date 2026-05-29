from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["KeyboardShortcutInfo"]

class KeyboardShortcutInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/KeyboardShortcutInfo"
    __javaconstructor__ = [("(Ljava/lang/CharSequence;CI)V", False), ("(Ljava/lang/CharSequence;II)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getBaseCharacter = JavaMethod("()C")
    getKeycode = JavaMethod("()I")
    getModifiers = JavaMethod("()I")
    getLabel = JavaMethod("()Ljava/lang/CharSequence;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")