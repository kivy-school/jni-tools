from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InputMethod"]

class InputMethod(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/accessibilityservice/InputMethod"
    __javaconstructor__ = [("(Landroid/accessibilityservice/AccessibilityService;)V", False)]
    getCurrentInputConnection = JavaMethod("()Landroid/accessibilityservice/InputMethod$AccessibilityInputConnection;")
    getCurrentInputStarted = JavaMethod("()Z")
    getCurrentInputEditorInfo = JavaMethod("()Landroid/view/inputmethod/EditorInfo;")
    onStartInput = JavaMethod("(Landroid/view/inputmethod/EditorInfo;Z)V")
    onFinishInput = JavaMethod("()V")
    onUpdateSelection = JavaMethod("(IIIIII)V")

    class AccessibilityInputConnection(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/accessibilityservice/InputMethod/AccessibilityInputConnection"
        commitText = JavaMethod("(Ljava/lang/CharSequence;ILandroid/view/inputmethod/TextAttribute;)V")
        setSelection = JavaMethod("(II)V")
        getSurroundingText = JavaMethod("(III)Landroid/view/inputmethod/SurroundingText;")
        deleteSurroundingText = JavaMethod("(II)V")
        sendKeyEvent = JavaMethod("(Landroid/view/KeyEvent;)V")
        performEditorAction = JavaMethod("(I)V")
        performContextMenuAction = JavaMethod("(I)V")
        getCursorCapsMode = JavaMethod("(I)I")
        clearMetaKeyStates = JavaMethod("(I)V")