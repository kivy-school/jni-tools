from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VelocityTracker"]

class VelocityTracker(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/VelocityTracker"
    getAxisVelocity = JavaMultipleMethod([("(I)F", False, False), ("(II)F", False, False)])
    getXVelocity = JavaMultipleMethod([("()F", False, False), ("(I)F", False, False)])
    isAxisSupported = JavaMethod("(I)Z")
    getYVelocity = JavaMultipleMethod([("(I)F", False, False), ("()F", False, False)])
    addMovement = JavaMethod("(Landroid/view/MotionEvent;)V")
    computeCurrentVelocity = JavaMultipleMethod([("(IF)V", False, False), ("(I)V", False, False)])
    clear = JavaMethod("()V")
    recycle = JavaMethod("()V")
    obtain = JavaStaticMethod("()Landroid/view/VelocityTracker;")