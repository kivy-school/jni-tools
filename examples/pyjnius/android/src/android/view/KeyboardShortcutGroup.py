from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["KeyboardShortcutGroup"]

class KeyboardShortcutGroup(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/KeyboardShortcutGroup"
    __javaconstructor__ = [("(Ljava/lang/CharSequence;)V", False), ("(Ljava/lang/CharSequence;Ljava/util/List;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getItems = JavaMethod("()Ljava/util/List;")
    getLabel = JavaMethod("()Ljava/lang/CharSequence;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    addItem = JavaMethod("(Landroid/view/KeyboardShortcutInfo;)V")