from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StateListAnimator"]

class StateListAnimator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/StateListAnimator"
    __javaconstructor__ = [("()V", False)]
    addState = JavaMethod("([ILandroid/animation/Animator;)V")
    clone = JavaMethod("()Landroid/animation/StateListAnimator;")
    jumpToCurrentState = JavaMethod("()V")