from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InputMethodSession"]

class InputMethodSession(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inputmethod/InputMethodSession"
    finishInput = JavaMethod("()V")
    updateSelection = JavaMethod("(IIIIII)V")
    viewClicked = JavaMethod("(Z)V")
    updateCursor = JavaMethod("(Landroid/graphics/Rect;)V")
    displayCompletions = JavaMethod("([Landroid/view/inputmethod/CompletionInfo;)V")
    updateExtractedText = JavaMethod("(ILandroid/view/inputmethod/ExtractedText;)V")
    dispatchKeyEvent = JavaMethod("(ILandroid/view/KeyEvent;Landroid/view/inputmethod/InputMethodSession$EventCallback;)V")
    dispatchTrackballEvent = JavaMethod("(ILandroid/view/MotionEvent;Landroid/view/inputmethod/InputMethodSession$EventCallback;)V")
    dispatchGenericMotionEvent = JavaMethod("(ILandroid/view/MotionEvent;Landroid/view/inputmethod/InputMethodSession$EventCallback;)V")
    appPrivateCommand = JavaMethod("(Ljava/lang/String;Landroid/os/Bundle;)V")
    toggleSoftInput = JavaMethod("(II)V")
    updateCursorAnchorInfo = JavaMethod("(Landroid/view/inputmethod/CursorAnchorInfo;)V")

    class EventCallback(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/inputmethod/InputMethodSession/EventCallback"
        finishedEvent = JavaMethod("(IZ)V")