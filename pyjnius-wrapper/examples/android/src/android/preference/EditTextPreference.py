from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EditTextPreference"]

class EditTextPreference(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/preference/EditTextPreference"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;)V", False)]
    setText = JavaMethod("(Ljava/lang/String;)V")
    getText = JavaMethod("()Ljava/lang/String;")
    onBindDialogView = JavaMethod("(Landroid/view/View;)V")
    showDialog = JavaMethod("(Landroid/os/Bundle;)V")
    onAddEditTextToDialogView = JavaMethod("(Landroid/view/View;Landroid/widget/EditText;)V")
    onDialogClosed = JavaMethod("(Z)V")
    onGetDefaultValue = JavaMethod("(Landroid/content/res/TypedArray;I)Ljava/lang/Object;")
    onSetInitialValue = JavaMethod("(ZLjava/lang/Object;)V")
    shouldDisableDependents = JavaMethod("()Z")
    getEditText = JavaMethod("()Landroid/widget/EditText;")
    onSaveInstanceState = JavaMethod("()Landroid/os/Parcelable;")
    onRestoreInstanceState = JavaMethod("(Landroid/os/Parcelable;)V")