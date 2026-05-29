from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SlidingDrawer"]

class SlidingDrawer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/SlidingDrawer"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False)]
    ORIENTATION_HORIZONTAL = JavaStaticField("I")
    ORIENTATION_VERTICAL = JavaStaticField("I")
    onFinishInflate = JavaMethod("()V")
    onMeasure = JavaMethod("(II)V")
    dispatchDraw = JavaMethod("(Landroid/graphics/Canvas;)V")
    onLayout = JavaMethod("(ZIIII)V")
    onInterceptTouchEvent = JavaMethod("(Landroid/view/MotionEvent;)Z")
    onTouchEvent = JavaMethod("(Landroid/view/MotionEvent;)Z")
    toggle = JavaMethod("()V")
    animateToggle = JavaMethod("()V")
    open = JavaMethod("()V")
    close = JavaMethod("()V")
    animateClose = JavaMethod("()V")
    animateOpen = JavaMethod("()V")
    getAccessibilityClassName = JavaMethod("()Ljava/lang/CharSequence;")
    setOnDrawerOpenListener = JavaMethod("(Landroid/widget/SlidingDrawer$OnDrawerOpenListener;)V")
    setOnDrawerCloseListener = JavaMethod("(Landroid/widget/SlidingDrawer$OnDrawerCloseListener;)V")
    setOnDrawerScrollListener = JavaMethod("(Landroid/widget/SlidingDrawer$OnDrawerScrollListener;)V")
    getHandle = JavaMethod("()Landroid/view/View;")
    getContent = JavaMethod("()Landroid/view/View;")
    unlock = JavaMethod("()V")
    lock = JavaMethod("()V")
    isOpened = JavaMethod("()Z")
    isMoving = JavaMethod("()Z")

    class OnDrawerCloseListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/SlidingDrawer/OnDrawerCloseListener"
        onDrawerClosed = JavaMethod("()V")

    class OnDrawerOpenListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/SlidingDrawer/OnDrawerOpenListener"
        onDrawerOpened = JavaMethod("()V")

    class OnDrawerScrollListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/SlidingDrawer/OnDrawerScrollListener"
        onScrollStarted = JavaMethod("()V")
        onScrollEnded = JavaMethod("()V")