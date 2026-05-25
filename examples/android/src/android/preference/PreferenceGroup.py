from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PreferenceGroup"]

class PreferenceGroup(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/preference/PreferenceGroup"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False)]
    setOrderingAsAdded = JavaMethod("(Z)V")
    isOrderingAsAdded = JavaMethod("()Z")
    addItemFromInflater = JavaMethod("(Landroid/preference/Preference;)V")
    getPreferenceCount = JavaMethod("()I")
    getPreference = JavaMethod("(I)Landroid/preference/Preference;")
    addPreference = JavaMethod("(Landroid/preference/Preference;)Z")
    removePreference = JavaMethod("(Landroid/preference/Preference;)Z")
    removeAll = JavaMethod("()V")
    onPrepareAddPreference = JavaMethod("(Landroid/preference/Preference;)Z")
    findPreference = JavaMethod("(Ljava/lang/CharSequence;)Landroid/preference/Preference;")
    isOnSameScreenAsChildren = JavaMethod("()Z")
    onAttachedToActivity = JavaMethod("()V")
    onPrepareForRemoval = JavaMethod("()V")
    notifyDependencyChange = JavaMethod("(Z)V")
    dispatchSaveInstanceState = JavaMethod("(Landroid/os/Bundle;)V")
    dispatchRestoreInstanceState = JavaMethod("(Landroid/os/Bundle;)V")