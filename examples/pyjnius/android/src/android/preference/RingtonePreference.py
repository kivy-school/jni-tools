from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RingtonePreference"]

class RingtonePreference(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/preference/RingtonePreference"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;)V", False)]
    getRingtoneType = JavaMethod("()I")
    setRingtoneType = JavaMethod("(I)V")
    getShowDefault = JavaMethod("()Z")
    setShowDefault = JavaMethod("(Z)V")
    getShowSilent = JavaMethod("()Z")
    setShowSilent = JavaMethod("(Z)V")
    onClick = JavaMethod("()V")
    onPrepareRingtonePickerIntent = JavaMethod("(Landroid/content/Intent;)V")
    onSaveRingtone = JavaMethod("(Landroid/net/Uri;)V")
    onRestoreRingtone = JavaMethod("()Landroid/net/Uri;")
    onGetDefaultValue = JavaMethod("(Landroid/content/res/TypedArray;I)Ljava/lang/Object;")
    onSetInitialValue = JavaMethod("(ZLjava/lang/Object;)V")
    onAttachedToHierarchy = JavaMethod("(Landroid/preference/PreferenceManager;)V")
    onActivityResult = JavaMethod("(IILandroid/content/Intent;)Z")