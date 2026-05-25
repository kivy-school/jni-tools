from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ScaleGestureDetector"]

class ScaleGestureDetector(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/ScaleGestureDetector"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/view/ScaleGestureDetector$OnScaleGestureListener;)V", False), ("(Landroid/content/Context;Landroid/view/ScaleGestureDetector$OnScaleGestureListener;Landroid/os/Handler;)V", False)]
    onTouchEvent = JavaMethod("(Landroid/view/MotionEvent;)Z")
    setQuickScaleEnabled = JavaMethod("(Z)V")
    isQuickScaleEnabled = JavaMethod("()Z")
    setStylusScaleEnabled = JavaMethod("(Z)V")
    isStylusScaleEnabled = JavaMethod("()Z")
    isInProgress = JavaMethod("()Z")
    getFocusX = JavaMethod("()F")
    getFocusY = JavaMethod("()F")
    getCurrentSpan = JavaMethod("()F")
    getCurrentSpanX = JavaMethod("()F")
    getCurrentSpanY = JavaMethod("()F")
    getPreviousSpan = JavaMethod("()F")
    getPreviousSpanX = JavaMethod("()F")
    getPreviousSpanY = JavaMethod("()F")
    getScaleFactor = JavaMethod("()F")
    getTimeDelta = JavaMethod("()J")
    getEventTime = JavaMethod("()J")

    class OnScaleGestureListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/ScaleGestureDetector/OnScaleGestureListener"
        onScale = JavaMethod("(Landroid/view/ScaleGestureDetector;)Z")
        onScaleBegin = JavaMethod("(Landroid/view/ScaleGestureDetector;)Z")
        onScaleEnd = JavaMethod("(Landroid/view/ScaleGestureDetector;)V")

    class SimpleOnScaleGestureListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/ScaleGestureDetector/SimpleOnScaleGestureListener"
        __javaconstructor__ = [("()V", False)]
        onScale = JavaMethod("(Landroid/view/ScaleGestureDetector;)Z")
        onScaleBegin = JavaMethod("(Landroid/view/ScaleGestureDetector;)Z")
        onScaleEnd = JavaMethod("(Landroid/view/ScaleGestureDetector;)V")