from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ExtractEditText"]

class ExtractEditText(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/inputmethodservice/ExtractEditText"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False)]
    startInternalChanges = JavaMethod("()V")
    finishInternalChanges = JavaMethod("()V")
    setExtractedText = JavaMethod("(Landroid/view/inputmethod/ExtractedText;)V")
    onSelectionChanged = JavaMethod("(II)V")
    performClick = JavaMethod("()Z")
    onTextContextMenuItem = JavaMethod("(I)Z")
    isInputMethodTarget = JavaMethod("()Z")
    hasVerticalScrollBar = JavaMethod("()Z")
    hasWindowFocus = JavaMethod("()Z")
    isFocused = JavaMethod("()Z")
    hasFocus = JavaMethod("()Z")