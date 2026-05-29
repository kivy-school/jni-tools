from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RingtonePreference"]

class RingtonePreference(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/preference/RingtonePreference"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False)]
    DEFAULT_ORDER = JavaStaticField("I")
    getShowSilent = JavaMethod("()Z")
    getShowDefault = JavaMethod("()Z")
    getRingtoneType = JavaMethod("()I")
    setRingtoneType = JavaMethod("(I)V")
    setShowDefault = JavaMethod("(Z)V")
    setShowSilent = JavaMethod("(Z)V")
    onActivityResult = JavaMethod("(IILandroid/content/Intent;)Z")