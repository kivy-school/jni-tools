from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ScaleGestureDetector"]

class ScaleGestureDetector(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/ScaleGestureDetector"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/view/ScaleGestureDetector$OnScaleGestureListener;Landroid/os/Handler;)V", False), ("(Landroid/content/Context;Landroid/view/ScaleGestureDetector$OnScaleGestureListener;)V", False)]
    getCurrentSpanX = JavaMethod("()F")
    getFocusY = JavaMethod("()F")
    getTimeDelta = JavaMethod("()J")
    getCurrentSpan = JavaMethod("()F")
    getPreviousSpanY = JavaMethod("()F")
    getPreviousSpanX = JavaMethod("()F")
    getCurrentSpanY = JavaMethod("()F")
    isInProgress = JavaMethod("()Z")
    getFocusX = JavaMethod("()F")
    getPreviousSpan = JavaMethod("()F")
    isQuickScaleEnabled = JavaMethod("()Z")
    isStylusScaleEnabled = JavaMethod("()Z")
    setQuickScaleEnabled = JavaMethod("(Z)V")
    setStylusScaleEnabled = JavaMethod("(Z)V")
    getScaleFactor = JavaMethod("()F")
    onTouchEvent = JavaMethod("(Landroid/view/MotionEvent;)Z")
    getEventTime = JavaMethod("()J")

    class SimpleOnScaleGestureListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/ScaleGestureDetector$SimpleOnScaleGestureListener"
        __javaconstructor__ = [("()V", False)]
        onScaleBegin = JavaMethod("(Landroid/view/ScaleGestureDetector;)Z")
        onScaleEnd = JavaMethod("(Landroid/view/ScaleGestureDetector;)V")
        onScale = JavaMethod("(Landroid/view/ScaleGestureDetector;)Z")

    class OnScaleGestureListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/ScaleGestureDetector$OnScaleGestureListener"
        onScaleBegin = JavaMethod("(Landroid/view/ScaleGestureDetector;)Z")
        onScaleEnd = JavaMethod("(Landroid/view/ScaleGestureDetector;)V")
        onScale = JavaMethod("(Landroid/view/ScaleGestureDetector;)Z")