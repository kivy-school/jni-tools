from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AnimationUtils"]

class AnimationUtils(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/animation/AnimationUtils"
    __javaconstructor__ = [("()V", False)]
    loadAnimation = JavaStaticMethod("(Landroid/content/Context;I)Landroid/view/animation/Animation;")
    loadInterpolator = JavaStaticMethod("(Landroid/content/Context;I)Landroid/view/animation/Interpolator;")
    makeOutAnimation = JavaStaticMethod("(Landroid/content/Context;Z)Landroid/view/animation/Animation;")
    makeInAnimation = JavaStaticMethod("(Landroid/content/Context;Z)Landroid/view/animation/Animation;")
    currentAnimationTimeMillis = JavaStaticMethod("()J")
    loadLayoutAnimation = JavaStaticMethod("(Landroid/content/Context;I)Landroid/view/animation/LayoutAnimationController;")
    makeInChildBottomAnimation = JavaStaticMethod("(Landroid/content/Context;)Landroid/view/animation/Animation;")