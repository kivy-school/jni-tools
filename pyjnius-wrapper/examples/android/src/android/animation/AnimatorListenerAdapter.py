from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AnimatorListenerAdapter"]

class AnimatorListenerAdapter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/AnimatorListenerAdapter"
    __javaconstructor__ = [("()V", False)]
    onAnimationCancel = JavaMethod("(Landroid/animation/Animator;)V")
    onAnimationEnd = JavaMethod("(Landroid/animation/Animator;)V")
    onAnimationRepeat = JavaMethod("(Landroid/animation/Animator;)V")
    onAnimationStart = JavaMethod("(Landroid/animation/Animator;)V")
    onAnimationPause = JavaMethod("(Landroid/animation/Animator;)V")
    onAnimationResume = JavaMethod("(Landroid/animation/Animator;)V")