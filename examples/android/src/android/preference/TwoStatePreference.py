from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TwoStatePreference"]

class TwoStatePreference(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/preference/TwoStatePreference"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;)V", False)]
    onClick = JavaMethod("()V")
    setChecked = JavaMethod("(Z)V")
    isChecked = JavaMethod("()Z")
    shouldDisableDependents = JavaMethod("()Z")
    setSummaryOn = JavaMultipleMethod([("(Ljava/lang/CharSequence;)V", False, False), ("(I)V", False, False)])
    getSummaryOn = JavaMethod("()Ljava/lang/CharSequence;")
    setSummaryOff = JavaMultipleMethod([("(Ljava/lang/CharSequence;)V", False, False), ("(I)V", False, False)])
    getSummaryOff = JavaMethod("()Ljava/lang/CharSequence;")
    getDisableDependentsState = JavaMethod("()Z")
    setDisableDependentsState = JavaMethod("(Z)V")
    onGetDefaultValue = JavaMethod("(Landroid/content/res/TypedArray;I)Ljava/lang/Object;")
    onSetInitialValue = JavaMethod("(ZLjava/lang/Object;)V")
    onSaveInstanceState = JavaMethod("()Landroid/os/Parcelable;")
    onRestoreInstanceState = JavaMethod("(Landroid/os/Parcelable;)V")