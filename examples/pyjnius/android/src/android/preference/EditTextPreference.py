from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EditTextPreference"]

class EditTextPreference(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/preference/EditTextPreference"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False)]
    DEFAULT_ORDER = JavaStaticField("I")
    getEditText = JavaMethod("()Landroid/widget/EditText;")
    shouldDisableDependents = JavaMethod("()Z")
    getText = JavaMethod("()Ljava/lang/String;")
    setText = JavaMethod("(Ljava/lang/String;)V")