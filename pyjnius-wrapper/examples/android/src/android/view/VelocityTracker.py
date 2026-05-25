from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VelocityTracker"]

class VelocityTracker(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/VelocityTracker"
    obtain = JavaStaticMethod("()Landroid/view/VelocityTracker;")
    recycle = JavaMethod("()V")
    finalize = JavaMethod("()V")
    isAxisSupported = JavaMethod("(I)Z")
    clear = JavaMethod("()V")
    addMovement = JavaMethod("(Landroid/view/MotionEvent;)V")
    computeCurrentVelocity = JavaMultipleMethod([("(I)V", False, False), ("(IF)V", False, False)])
    getXVelocity = JavaMultipleMethod([("()F", False, False), ("(I)F", False, False)])
    getYVelocity = JavaMultipleMethod([("()F", False, False), ("(I)F", False, False)])
    getAxisVelocity = JavaMultipleMethod([("(II)F", False, False), ("(I)F", False, False)])