from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ViewTreeObserver"]

class ViewTreeObserver(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/ViewTreeObserver"
    addOnWindowAttachListener = JavaMethod("(Landroid/view/ViewTreeObserver$OnWindowAttachListener;)V")
    removeOnWindowAttachListener = JavaMethod("(Landroid/view/ViewTreeObserver$OnWindowAttachListener;)V")
    addOnWindowFocusChangeListener = JavaMethod("(Landroid/view/ViewTreeObserver$OnWindowFocusChangeListener;)V")
    removeOnWindowFocusChangeListener = JavaMethod("(Landroid/view/ViewTreeObserver$OnWindowFocusChangeListener;)V")
    addOnWindowVisibilityChangeListener = JavaMethod("(Landroid/view/ViewTreeObserver$OnWindowVisibilityChangeListener;)V")
    removeOnWindowVisibilityChangeListener = JavaMethod("(Landroid/view/ViewTreeObserver$OnWindowVisibilityChangeListener;)V")
    addOnGlobalFocusChangeListener = JavaMethod("(Landroid/view/ViewTreeObserver$OnGlobalFocusChangeListener;)V")
    removeOnGlobalFocusChangeListener = JavaMethod("(Landroid/view/ViewTreeObserver$OnGlobalFocusChangeListener;)V")
    addOnGlobalLayoutListener = JavaMethod("(Landroid/view/ViewTreeObserver$OnGlobalLayoutListener;)V")
    removeGlobalOnLayoutListener = JavaMethod("(Landroid/view/ViewTreeObserver$OnGlobalLayoutListener;)V")
    removeOnGlobalLayoutListener = JavaMethod("(Landroid/view/ViewTreeObserver$OnGlobalLayoutListener;)V")
    addOnPreDrawListener = JavaMethod("(Landroid/view/ViewTreeObserver$OnPreDrawListener;)V")
    removeOnPreDrawListener = JavaMethod("(Landroid/view/ViewTreeObserver$OnPreDrawListener;)V")
    addOnDrawListener = JavaMethod("(Landroid/view/ViewTreeObserver$OnDrawListener;)V")
    removeOnDrawListener = JavaMethod("(Landroid/view/ViewTreeObserver$OnDrawListener;)V")
    registerFrameCommitCallback = JavaMethod("(Ljava/lang/Runnable;)V")
    unregisterFrameCommitCallback = JavaMethod("(Ljava/lang/Runnable;)Z")
    addOnScrollChangedListener = JavaMethod("(Landroid/view/ViewTreeObserver$OnScrollChangedListener;)V")
    removeOnScrollChangedListener = JavaMethod("(Landroid/view/ViewTreeObserver$OnScrollChangedListener;)V")
    addOnTouchModeChangeListener = JavaMethod("(Landroid/view/ViewTreeObserver$OnTouchModeChangeListener;)V")
    removeOnTouchModeChangeListener = JavaMethod("(Landroid/view/ViewTreeObserver$OnTouchModeChangeListener;)V")
    addOnSystemGestureExclusionRectsChangedListener = JavaMethod("(Ljava/util/function/Consumer;)V")
    removeOnSystemGestureExclusionRectsChangedListener = JavaMethod("(Ljava/util/function/Consumer;)V")
    isAlive = JavaMethod("()Z")
    dispatchOnGlobalLayout = JavaMethod("()V")
    dispatchOnPreDraw = JavaMethod("()Z")
    dispatchOnDraw = JavaMethod("()V")

    class OnDrawListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/ViewTreeObserver/OnDrawListener"
        onDraw = JavaMethod("()V")

    class OnGlobalFocusChangeListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/ViewTreeObserver/OnGlobalFocusChangeListener"
        onGlobalFocusChanged = JavaMethod("(Landroid/view/View;Landroid/view/View;)V")

    class OnGlobalLayoutListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/ViewTreeObserver/OnGlobalLayoutListener"
        onGlobalLayout = JavaMethod("()V")

    class OnPreDrawListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/ViewTreeObserver/OnPreDrawListener"
        onPreDraw = JavaMethod("()Z")

    class OnScrollChangedListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/ViewTreeObserver/OnScrollChangedListener"
        onScrollChanged = JavaMethod("()V")

    class OnTouchModeChangeListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/ViewTreeObserver/OnTouchModeChangeListener"
        onTouchModeChanged = JavaMethod("(Z)V")

    class OnWindowAttachListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/ViewTreeObserver/OnWindowAttachListener"
        onWindowAttached = JavaMethod("()V")
        onWindowDetached = JavaMethod("()V")

    class OnWindowFocusChangeListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/ViewTreeObserver/OnWindowFocusChangeListener"
        onWindowFocusChanged = JavaMethod("(Z)V")

    class OnWindowVisibilityChangeListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/ViewTreeObserver/OnWindowVisibilityChangeListener"
        onWindowVisibilityChanged = JavaMethod("(I)V")