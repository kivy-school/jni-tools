from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AnimatorInflater"]

class AnimatorInflater(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/AnimatorInflater"
    __javaconstructor__ = [("()V", False)]
    loadAnimator = JavaStaticMethod("(Landroid/content/Context;I)Landroid/animation/Animator;")
    loadStateListAnimator = JavaStaticMethod("(Landroid/content/Context;I)Landroid/animation/StateListAnimator;")