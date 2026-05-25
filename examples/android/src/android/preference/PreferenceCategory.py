from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PreferenceCategory"]

class PreferenceCategory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/preference/PreferenceCategory"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;)V", False)]
    onPrepareAddPreference = JavaMethod("(Landroid/preference/Preference;)Z")
    isEnabled = JavaMethod("()Z")
    shouldDisableDependents = JavaMethod("()Z")