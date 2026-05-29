from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InputMethodSession"]

class InputMethodSession(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inputmethod/InputMethodSession"
    displayCompletions = JavaMethod("([Landroid/view/inputmethod/CompletionInfo;)V")
    toggleSoftInput = JavaMethod("(II)V")
    updateCursor = JavaMethod("(Landroid/graphics/Rect;)V")
    updateCursorAnchorInfo = JavaMethod("(Landroid/view/inputmethod/CursorAnchorInfo;)V")
    updateExtractedText = JavaMethod("(ILandroid/view/inputmethod/ExtractedText;)V")
    updateSelection = JavaMethod("(IIIIII)V")
    viewClicked = JavaMethod("(Z)V")
    finishInput = JavaMethod("()V")
    appPrivateCommand = JavaMethod("(Ljava/lang/String;Landroid/os/Bundle;)V")
    dispatchGenericMotionEvent = JavaMethod("(ILandroid/view/MotionEvent;Landroid/view/inputmethod/InputMethodSession$EventCallback;)V")
    dispatchKeyEvent = JavaMethod("(ILandroid/view/KeyEvent;Landroid/view/inputmethod/InputMethodSession$EventCallback;)V")
    dispatchTrackballEvent = JavaMethod("(ILandroid/view/MotionEvent;Landroid/view/inputmethod/InputMethodSession$EventCallback;)V")

    class EventCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/inputmethod/InputMethodSession$EventCallback"
        finishedEvent = JavaMethod("(IZ)V")