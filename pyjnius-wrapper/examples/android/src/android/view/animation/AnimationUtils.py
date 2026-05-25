from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AnimationUtils"]

class AnimationUtils(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/animation/AnimationUtils"
    __javaconstructor__ = [("()V", False)]
    currentAnimationTimeMillis = JavaStaticMethod("()J")
    loadAnimation = JavaStaticMethod("(Landroid/content/Context;I)Landroid/view/animation/Animation;")
    loadLayoutAnimation = JavaStaticMethod("(Landroid/content/Context;I)Landroid/view/animation/LayoutAnimationController;")
    makeInAnimation = JavaStaticMethod("(Landroid/content/Context;Z)Landroid/view/animation/Animation;")
    makeOutAnimation = JavaStaticMethod("(Landroid/content/Context;Z)Landroid/view/animation/Animation;")
    makeInChildBottomAnimation = JavaStaticMethod("(Landroid/content/Context;)Landroid/view/animation/Animation;")
    loadInterpolator = JavaStaticMethod("(Landroid/content/Context;I)Landroid/view/animation/Interpolator;")