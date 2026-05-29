from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ListPreference"]

class ListPreference(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/preference/ListPreference"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;)V", False)]
    DEFAULT_ORDER = JavaStaticField("I")
    getSummary = JavaMethod("()Ljava/lang/CharSequence;")
    setSummary = JavaMethod("(Ljava/lang/CharSequence;)V")
    setEntryValues = JavaMultipleMethod([("([Ljava/lang/CharSequence;)V", False, False), ("(I)V", False, False)])
    setEntries = JavaMultipleMethod([("([Ljava/lang/CharSequence;)V", False, False), ("(I)V", False, False)])
    findIndexOfValue = JavaMethod("(Ljava/lang/String;)I")
    getEntryValues = JavaMethod("()[Ljava/lang/CharSequence;")
    setValueIndex = JavaMethod("(I)V")
    getValue = JavaMethod("()Ljava/lang/String;")
    setValue = JavaMethod("(Ljava/lang/String;)V")
    getEntries = JavaMethod("()[Ljava/lang/CharSequence;")
    getEntry = JavaMethod("()Ljava/lang/CharSequence;")