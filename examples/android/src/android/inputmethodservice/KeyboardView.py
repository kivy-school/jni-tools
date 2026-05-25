from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["KeyboardView"]

class KeyboardView(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/inputmethodservice/KeyboardView"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False)]
    onAttachedToWindow = JavaMethod("()V")
    setOnKeyboardActionListener = JavaMethod("(Landroid/inputmethodservice/KeyboardView$OnKeyboardActionListener;)V")
    getOnKeyboardActionListener = JavaMethod("()Landroid/inputmethodservice/KeyboardView$OnKeyboardActionListener;")
    setKeyboard = JavaMethod("(Landroid/inputmethodservice/Keyboard;)V")
    getKeyboard = JavaMethod("()Landroid/inputmethodservice/Keyboard;")
    setShifted = JavaMethod("(Z)Z")
    isShifted = JavaMethod("()Z")
    setPreviewEnabled = JavaMethod("(Z)V")
    isPreviewEnabled = JavaMethod("()Z")
    setVerticalCorrection = JavaMethod("(I)V")
    setPopupParent = JavaMethod("(Landroid/view/View;)V")
    setPopupOffset = JavaMethod("(II)V")
    setProximityCorrectionEnabled = JavaMethod("(Z)V")
    isProximityCorrectionEnabled = JavaMethod("()Z")
    onClick = JavaMethod("(Landroid/view/View;)V")
    onMeasure = JavaMethod("(II)V")
    onSizeChanged = JavaMethod("(IIII)V")
    onDraw = JavaMethod("(Landroid/graphics/Canvas;)V")
    invalidateAllKeys = JavaMethod("()V")
    invalidateKey = JavaMethod("(I)V")
    onLongPress = JavaMethod("(Landroid/inputmethodservice/Keyboard$Key;)Z")
    onHoverEvent = JavaMethod("(Landroid/view/MotionEvent;)Z")
    onTouchEvent = JavaMethod("(Landroid/view/MotionEvent;)Z")
    swipeRight = JavaMethod("()V")
    swipeLeft = JavaMethod("()V")
    swipeUp = JavaMethod("()V")
    swipeDown = JavaMethod("()V")
    closing = JavaMethod("()V")
    onDetachedFromWindow = JavaMethod("()V")
    handleBack = JavaMethod("()Z")

    class OnKeyboardActionListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/inputmethodservice/KeyboardView/OnKeyboardActionListener"
        onPress = JavaMethod("(I)V")
        onRelease = JavaMethod("(I)V")
        onKey = JavaMethod("(I[I)V")
        onText = JavaMethod("(Ljava/lang/CharSequence;)V")
        swipeLeft = JavaMethod("()V")
        swipeRight = JavaMethod("()V")
        swipeDown = JavaMethod("()V")
        swipeUp = JavaMethod("()V")