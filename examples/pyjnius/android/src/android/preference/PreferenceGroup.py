from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PreferenceGroup"]

class PreferenceGroup(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/preference/PreferenceGroup"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False)]
    DEFAULT_ORDER = JavaStaticField("I")
    addPreference = JavaMethod("(Landroid/preference/Preference;)Z")
    addItemFromInflater = JavaMethod("(Landroid/preference/Preference;)V")
    getPreference = JavaMethod("(I)Landroid/preference/Preference;")
    getPreferenceCount = JavaMethod("()I")
    isOrderingAsAdded = JavaMethod("()Z")
    removePreference = JavaMethod("(Landroid/preference/Preference;)Z")
    setOrderingAsAdded = JavaMethod("(Z)V")
    findPreference = JavaMethod("(Ljava/lang/CharSequence;)Landroid/preference/Preference;")
    notifyDependencyChange = JavaMethod("(Z)V")
    removeAll = JavaMethod("()V")