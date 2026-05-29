from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TouchInteractionController"]

class TouchInteractionController(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/accessibilityservice/TouchInteractionController"
    STATE_CLEAR = JavaStaticField("I")
    STATE_DELEGATING = JavaStaticField("I")
    STATE_DRAGGING = JavaStaticField("I")
    STATE_TOUCH_EXPLORING = JavaStaticField("I")
    STATE_TOUCH_INTERACTING = JavaStaticField("I")
    requestDragging = JavaMethod("(I)V")
    unregisterAllCallbacks = JavaMethod("()V")
    getMaxPointerCount = JavaMethod("()I")
    requestDelegating = JavaMethod("()V")
    requestTouchExploration = JavaMethod("()V")
    performLongClickAndStartDrag = JavaMethod("()V")
    getState = JavaMethod("()I")
    performClick = JavaMethod("()V")
    stateToString = JavaStaticMethod("(I)Ljava/lang/String;")
    registerCallback = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/accessibilityservice/TouchInteractionController$Callback;)V")
    unregisterCallback = JavaMethod("(Landroid/accessibilityservice/TouchInteractionController$Callback;)Z")
    getDisplayId = JavaMethod("()I")

    class Callback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/accessibilityservice/TouchInteractionController$Callback"
        onMotionEvent = JavaMethod("(Landroid/view/MotionEvent;)V")
        onStateChanged = JavaMethod("(I)V")