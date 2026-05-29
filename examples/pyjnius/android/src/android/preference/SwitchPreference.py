from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SwitchPreference"]

class SwitchPreference(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/preference/SwitchPreference"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False)]
    DEFAULT_ORDER = JavaStaticField("I")
    setSwitchTextOff = JavaMultipleMethod([("(Ljava/lang/CharSequence;)V", False, False), ("(I)V", False, False)])
    setSwitchTextOn = JavaMultipleMethod([("(Ljava/lang/CharSequence;)V", False, False), ("(I)V", False, False)])
    getSwitchTextOn = JavaMethod("()Ljava/lang/CharSequence;")
    getSwitchTextOff = JavaMethod("()Ljava/lang/CharSequence;")