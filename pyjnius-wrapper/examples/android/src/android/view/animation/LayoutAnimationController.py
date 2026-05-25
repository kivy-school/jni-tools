from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LayoutAnimationController"]

class LayoutAnimationController(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/animation/LayoutAnimationController"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/view/animation/Animation;)V", False), ("(Landroid/view/animation/Animation;F)V", False)]
    ORDER_NORMAL = JavaStaticField("I")
    ORDER_RANDOM = JavaStaticField("I")
    ORDER_REVERSE = JavaStaticField("I")
    mAnimation = JavaField("Landroid/view/animation/Animation;")
    mInterpolator = JavaField("Landroid/view/animation/Interpolator;")
    mRandomizer = JavaField("Ljava/util/Random;")
    getOrder = JavaMethod("()I")
    setOrder = JavaMethod("(I)V")
    setAnimation = JavaMultipleMethod([("(Landroid/content/Context;I)V", False, False), ("(Landroid/view/animation/Animation;)V", False, False)])
    getAnimation = JavaMethod("()Landroid/view/animation/Animation;")
    setInterpolator = JavaMultipleMethod([("(Landroid/content/Context;I)V", False, False), ("(Landroid/view/animation/Interpolator;)V", False, False)])
    getInterpolator = JavaMethod("()Landroid/view/animation/Interpolator;")
    getDelay = JavaMethod("()F")
    setDelay = JavaMethod("(F)V")
    willOverlap = JavaMethod("()Z")
    start = JavaMethod("()V")
    getAnimationForView = JavaMethod("(Landroid/view/View;)Landroid/view/animation/Animation;")
    isDone = JavaMethod("()Z")
    getDelayForView = JavaMethod("(Landroid/view/View;)J")
    getTransformedIndex = JavaMethod("(Landroid/view/animation/LayoutAnimationController$AnimationParameters;)I")

    class AnimationParameters(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/animation/LayoutAnimationController/AnimationParameters"
        __javaconstructor__ = [("()V", False)]
        count = JavaField("I")
        index = JavaField("I")