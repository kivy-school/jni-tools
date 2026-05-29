from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MultiSelectListPreference"]

class MultiSelectListPreference(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/preference/MultiSelectListPreference"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False)]
    DEFAULT_ORDER = JavaStaticField("I")
    setEntryValues = JavaMultipleMethod([("([Ljava/lang/CharSequence;)V", False, False), ("(I)V", False, False)])
    setEntries = JavaMultipleMethod([("([Ljava/lang/CharSequence;)V", False, False), ("(I)V", False, False)])
    findIndexOfValue = JavaMethod("(Ljava/lang/String;)I")
    getEntryValues = JavaMethod("()[Ljava/lang/CharSequence;")
    getEntries = JavaMethod("()[Ljava/lang/CharSequence;")
    getValues = JavaMethod("()Ljava/util/Set;")
    setValues = JavaMethod("(Ljava/util/Set;)V")