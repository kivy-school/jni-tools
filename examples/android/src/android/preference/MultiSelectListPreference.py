from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MultiSelectListPreference"]

class MultiSelectListPreference(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/preference/MultiSelectListPreference"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;)V", False)]
    setEntries = JavaMultipleMethod([("([Ljava/lang/CharSequence;)V", False, False), ("(I)V", False, False)])
    getEntries = JavaMethod("()[Ljava/lang/CharSequence;")
    setEntryValues = JavaMultipleMethod([("([Ljava/lang/CharSequence;)V", False, False), ("(I)V", False, False)])
    getEntryValues = JavaMethod("()[Ljava/lang/CharSequence;")
    setValues = JavaMethod("(Ljava/util/Set;)V")
    getValues = JavaMethod("()Ljava/util/Set;")
    findIndexOfValue = JavaMethod("(Ljava/lang/String;)I")
    onPrepareDialogBuilder = JavaMethod("(Landroid/app/AlertDialog$Builder;)V")
    onDialogClosed = JavaMethod("(Z)V")
    onGetDefaultValue = JavaMethod("(Landroid/content/res/TypedArray;I)Ljava/lang/Object;")
    onSetInitialValue = JavaMethod("(ZLjava/lang/Object;)V")
    onSaveInstanceState = JavaMethod("()Landroid/os/Parcelable;")