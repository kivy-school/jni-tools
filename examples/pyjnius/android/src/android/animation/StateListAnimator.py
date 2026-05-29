from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StateListAnimator"]

class StateListAnimator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/StateListAnimator"
    __javaconstructor__ = [("()V", False)]
    addState = JavaMethod("([ILandroid/animation/Animator;)V")
    clone = JavaMultipleMethod([("()Ljava/lang/Object;", False, False), ("()Landroid/animation/StateListAnimator;", False, False)])
    jumpToCurrentState = JavaMethod("()V")