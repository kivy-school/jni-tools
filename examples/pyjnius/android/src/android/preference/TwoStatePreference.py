from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TwoStatePreference"]

class TwoStatePreference(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/preference/TwoStatePreference"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False)]
    DEFAULT_ORDER = JavaStaticField("I")
    shouldDisableDependents = JavaMethod("()Z")
    setDisableDependentsState = JavaMethod("(Z)V")
    getDisableDependentsState = JavaMethod("()Z")
    getSummaryOff = JavaMethod("()Ljava/lang/CharSequence;")
    setSummaryOff = JavaMultipleMethod([("(I)V", False, False), ("(Ljava/lang/CharSequence;)V", False, False)])
    getSummaryOn = JavaMethod("()Ljava/lang/CharSequence;")
    setSummaryOn = JavaMultipleMethod([("(Ljava/lang/CharSequence;)V", False, False), ("(I)V", False, False)])
    isChecked = JavaMethod("()Z")
    setChecked = JavaMethod("(Z)V")