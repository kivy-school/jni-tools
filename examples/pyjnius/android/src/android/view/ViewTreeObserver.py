from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ViewTreeObserver"]

class ViewTreeObserver(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/ViewTreeObserver"
    addOnGlobalFocusChangeListener = JavaMethod("(Landroid/view/ViewTreeObserver$OnGlobalFocusChangeListener;)V")
    addOnGlobalLayoutListener = JavaMethod("(Landroid/view/ViewTreeObserver$OnGlobalLayoutListener;)V")
    addOnPreDrawListener = JavaMethod("(Landroid/view/ViewTreeObserver$OnPreDrawListener;)V")
    addOnScrollChangedListener = JavaMethod("(Landroid/view/ViewTreeObserver$OnScrollChangedListener;)V")
    addOnSystemGestureExclusionRectsChangedListener = JavaMethod("(Ljava/util/function/Consumer;)V")
    addOnDrawListener = JavaMethod("(Landroid/view/ViewTreeObserver$OnDrawListener;)V")
    addOnTouchModeChangeListener = JavaMethod("(Landroid/view/ViewTreeObserver$OnTouchModeChangeListener;)V")
    addOnWindowAttachListener = JavaMethod("(Landroid/view/ViewTreeObserver$OnWindowAttachListener;)V")
    addOnWindowFocusChangeListener = JavaMethod("(Landroid/view/ViewTreeObserver$OnWindowFocusChangeListener;)V")
    addOnWindowVisibilityChangeListener = JavaMethod("(Landroid/view/ViewTreeObserver$OnWindowVisibilityChangeListener;)V")
    dispatchOnDraw = JavaMethod("()V")
    dispatchOnGlobalLayout = JavaMethod("()V")
    dispatchOnPreDraw = JavaMethod("()Z")
    registerFrameCommitCallback = JavaMethod("(Ljava/lang/Runnable;)V")
    removeGlobalOnLayoutListener = JavaMethod("(Landroid/view/ViewTreeObserver$OnGlobalLayoutListener;)V")
    removeOnDrawListener = JavaMethod("(Landroid/view/ViewTreeObserver$OnDrawListener;)V")
    removeOnGlobalFocusChangeListener = JavaMethod("(Landroid/view/ViewTreeObserver$OnGlobalFocusChangeListener;)V")
    removeOnGlobalLayoutListener = JavaMethod("(Landroid/view/ViewTreeObserver$OnGlobalLayoutListener;)V")
    removeOnPreDrawListener = JavaMethod("(Landroid/view/ViewTreeObserver$OnPreDrawListener;)V")
    removeOnScrollChangedListener = JavaMethod("(Landroid/view/ViewTreeObserver$OnScrollChangedListener;)V")
    removeOnSystemGestureExclusionRectsChangedListener = JavaMethod("(Ljava/util/function/Consumer;)V")
    removeOnTouchModeChangeListener = JavaMethod("(Landroid/view/ViewTreeObserver$OnTouchModeChangeListener;)V")
    removeOnWindowAttachListener = JavaMethod("(Landroid/view/ViewTreeObserver$OnWindowAttachListener;)V")
    removeOnWindowFocusChangeListener = JavaMethod("(Landroid/view/ViewTreeObserver$OnWindowFocusChangeListener;)V")
    removeOnWindowVisibilityChangeListener = JavaMethod("(Landroid/view/ViewTreeObserver$OnWindowVisibilityChangeListener;)V")
    unregisterFrameCommitCallback = JavaMethod("(Ljava/lang/Runnable;)Z")
    isAlive = JavaMethod("()Z")

    class OnWindowVisibilityChangeListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/ViewTreeObserver$OnWindowVisibilityChangeListener"
        onWindowVisibilityChanged = JavaMethod("(I)V")

    class OnWindowFocusChangeListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/ViewTreeObserver$OnWindowFocusChangeListener"
        onWindowFocusChanged = JavaMethod("(Z)V")

    class OnWindowAttachListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/ViewTreeObserver$OnWindowAttachListener"
        onWindowDetached = JavaMethod("()V")
        onWindowAttached = JavaMethod("()V")

    class OnTouchModeChangeListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/ViewTreeObserver$OnTouchModeChangeListener"
        onTouchModeChanged = JavaMethod("(Z)V")

    class OnScrollChangedListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/ViewTreeObserver$OnScrollChangedListener"
        onScrollChanged = JavaMethod("()V")

    class OnPreDrawListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/ViewTreeObserver$OnPreDrawListener"
        onPreDraw = JavaMethod("()Z")

    class OnGlobalLayoutListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/ViewTreeObserver$OnGlobalLayoutListener"
        onGlobalLayout = JavaMethod("()V")

    class OnGlobalFocusChangeListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/ViewTreeObserver$OnGlobalFocusChangeListener"
        onGlobalFocusChanged = JavaMethod("(Landroid/view/View;Landroid/view/View;)V")

    class OnDrawListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/ViewTreeObserver$OnDrawListener"
        onDraw = JavaMethod("()V")