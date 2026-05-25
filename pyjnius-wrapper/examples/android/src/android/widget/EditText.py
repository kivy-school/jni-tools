from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EditText"]

class EditText(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/EditText"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False)]
    getFreezesText = JavaMethod("()Z")
    getDefaultEditable = JavaMethod("()Z")
    getDefaultMovementMethod = JavaMethod("()Landroid/text/method/MovementMethod;")
    getText = JavaMethod("()Landroid/text/Editable;")
    setText = JavaMethod("(Ljava/lang/CharSequence;Landroid/widget/TextView$BufferType;)V")
    setSelection = JavaMultipleMethod([("(II)V", False, False), ("(I)V", False, False)])
    selectAll = JavaMethod("()V")
    extendSelection = JavaMethod("(I)V")
    setEllipsize = JavaMethod("(Landroid/text/TextUtils$TruncateAt;)V")
    getAccessibilityClassName = JavaMethod("()Ljava/lang/CharSequence;")
    onKeyShortcut = JavaMethod("(ILandroid/view/KeyEvent;)Z")
    onTextContextMenuItem = JavaMethod("(I)Z")
    setStyleShortcutsEnabled = JavaMethod("(Z)V")
    isStyleShortcutEnabled = JavaMethod("()Z")