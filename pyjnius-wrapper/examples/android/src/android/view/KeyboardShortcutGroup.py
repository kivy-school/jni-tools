from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["KeyboardShortcutGroup"]

class KeyboardShortcutGroup(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/KeyboardShortcutGroup"
    __javaconstructor__ = [("(Ljava/lang/CharSequence;Ljava/util/List;)V", False), ("(Ljava/lang/CharSequence;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getLabel = JavaMethod("()Ljava/lang/CharSequence;")
    getItems = JavaMethod("()Ljava/util/List;")
    addItem = JavaMethod("(Landroid/view/KeyboardShortcutInfo;)V")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")