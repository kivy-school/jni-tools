from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InputMethod"]

class InputMethod(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/accessibilityservice/InputMethod"
    __javaconstructor__ = [("(Landroid/accessibilityservice/AccessibilityService;)V", False)]
    onStartInput = JavaMethod("(Landroid/view/inputmethod/EditorInfo;Z)V")
    onFinishInput = JavaMethod("()V")
    getCurrentInputConnection = JavaMethod("()Landroid/accessibilityservice/InputMethod$AccessibilityInputConnection;")
    getCurrentInputEditorInfo = JavaMethod("()Landroid/view/inputmethod/EditorInfo;")
    getCurrentInputStarted = JavaMethod("()Z")
    onUpdateSelection = JavaMethod("(IIIIII)V")

    class AccessibilityInputConnection(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/accessibilityservice/InputMethod$AccessibilityInputConnection"
        setSelection = JavaMethod("(II)V")
        getCursorCapsMode = JavaMethod("(I)I")
        clearMetaKeyStates = JavaMethod("(I)V")
        commitText = JavaMethod("(Ljava/lang/CharSequence;ILandroid/view/inputmethod/TextAttribute;)V")
        getSurroundingText = JavaMethod("(III)Landroid/view/inputmethod/SurroundingText;")
        deleteSurroundingText = JavaMethod("(II)V")
        performContextMenuAction = JavaMethod("(I)V")
        performEditorAction = JavaMethod("(I)V")
        sendKeyEvent = JavaMethod("(Landroid/view/KeyEvent;)V")