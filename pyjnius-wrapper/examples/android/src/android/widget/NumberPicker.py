from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NumberPicker"]

class NumberPicker(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/NumberPicker"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False)]
    onLayout = JavaMethod("(ZIIII)V")
    onMeasure = JavaMethod("(II)V")
    onInterceptTouchEvent = JavaMethod("(Landroid/view/MotionEvent;)Z")
    onTouchEvent = JavaMethod("(Landroid/view/MotionEvent;)Z")
    dispatchTouchEvent = JavaMethod("(Landroid/view/MotionEvent;)Z")
    dispatchKeyEvent = JavaMethod("(Landroid/view/KeyEvent;)Z")
    dispatchTrackballEvent = JavaMethod("(Landroid/view/MotionEvent;)Z")
    dispatchHoverEvent = JavaMethod("(Landroid/view/MotionEvent;)Z")
    computeScroll = JavaMethod("()V")
    setEnabled = JavaMethod("(Z)V")
    scrollBy = JavaMethod("(II)V")
    computeVerticalScrollOffset = JavaMethod("()I")
    computeVerticalScrollRange = JavaMethod("()I")
    computeVerticalScrollExtent = JavaMethod("()I")
    getSolidColor = JavaMethod("()I")
    setOnValueChangedListener = JavaMethod("(Landroid/widget/NumberPicker$OnValueChangeListener;)V")
    setOnScrollListener = JavaMethod("(Landroid/widget/NumberPicker$OnScrollListener;)V")
    setFormatter = JavaMethod("(Landroid/widget/NumberPicker$Formatter;)V")
    setValue = JavaMethod("(I)V")
    performClick = JavaMethod("()Z")
    performLongClick = JavaMethod("()Z")
    getWrapSelectorWheel = JavaMethod("()Z")
    setWrapSelectorWheel = JavaMethod("(Z)V")
    setOnLongPressUpdateInterval = JavaMethod("(J)V")
    getValue = JavaMethod("()I")
    getMinValue = JavaMethod("()I")
    setMinValue = JavaMethod("(I)V")
    getMaxValue = JavaMethod("()I")
    setMaxValue = JavaMethod("(I)V")
    getDisplayedValues = JavaMethod("()[Ljava/lang/String;")
    setDisplayedValues = JavaMethod("([Ljava/lang/String;)V")
    setSelectionDividerHeight = JavaMethod("(I)V")
    getSelectionDividerHeight = JavaMethod("()I")
    getTopFadingEdgeStrength = JavaMethod("()F")
    getBottomFadingEdgeStrength = JavaMethod("()F")
    onDetachedFromWindow = JavaMethod("()V")
    drawableStateChanged = JavaMethod("()V")
    jumpDrawablesToCurrentState = JavaMethod("()V")
    onDraw = JavaMethod("(Landroid/graphics/Canvas;)V")
    getAccessibilityNodeProvider = JavaMethod("()Landroid/view/accessibility/AccessibilityNodeProvider;")
    setTextColor = JavaMethod("(I)V")
    getTextColor = JavaMethod("()I")
    setTextSize = JavaMethod("(F)V")
    getTextSize = JavaMethod("()F")

    class Formatter(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/NumberPicker/Formatter"
        format = JavaMethod("(I)Ljava/lang/String;")

    class OnScrollListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/NumberPicker/OnScrollListener"
        SCROLL_STATE_FLING = JavaStaticField("I")
        SCROLL_STATE_IDLE = JavaStaticField("I")
        SCROLL_STATE_TOUCH_SCROLL = JavaStaticField("I")
        onScrollStateChange = JavaMethod("(Landroid/widget/NumberPicker;I)V")

    class OnValueChangeListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/NumberPicker/OnValueChangeListener"
        onValueChange = JavaMethod("(Landroid/widget/NumberPicker;II)V")