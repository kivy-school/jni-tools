from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TouchInteractionController"]

class TouchInteractionController(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/accessibilityservice/TouchInteractionController"
    STATE_CLEAR = JavaStaticField("I")
    STATE_DELEGATING = JavaStaticField("I")
    STATE_DRAGGING = JavaStaticField("I")
    STATE_TOUCH_EXPLORING = JavaStaticField("I")
    STATE_TOUCH_INTERACTING = JavaStaticField("I")
    registerCallback = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/accessibilityservice/TouchInteractionController$Callback;)V")
    unregisterCallback = JavaMethod("(Landroid/accessibilityservice/TouchInteractionController$Callback;)Z")
    unregisterAllCallbacks = JavaMethod("()V")
    requestTouchExploration = JavaMethod("()V")
    requestDragging = JavaMethod("(I)V")
    requestDelegating = JavaMethod("()V")
    performClick = JavaMethod("()V")
    performLongClickAndStartDrag = JavaMethod("()V")
    getMaxPointerCount = JavaMethod("()I")
    getDisplayId = JavaMethod("()I")
    getState = JavaMethod("()I")
    stateToString = JavaStaticMethod("(I)Ljava/lang/String;")

    class Callback(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/accessibilityservice/TouchInteractionController/Callback"
        onMotionEvent = JavaMethod("(Landroid/view/MotionEvent;)V")
        onStateChanged = JavaMethod("(I)V")