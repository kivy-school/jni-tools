from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LayoutAnimationController"]

class LayoutAnimationController(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/animation/LayoutAnimationController"
    __javaconstructor__ = [("(Landroid/view/animation/Animation;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/view/animation/Animation;F)V", False)]
    ORDER_NORMAL = JavaStaticField("I")
    ORDER_RANDOM = JavaStaticField("I")
    ORDER_REVERSE = JavaStaticField("I")
    setDelay = JavaMethod("(F)V")
    setOrder = JavaMethod("(I)V")
    getDelay = JavaMethod("()F")
    willOverlap = JavaMethod("()Z")
    getAnimationForView = JavaMethod("(Landroid/view/View;)Landroid/view/animation/Animation;")
    start = JavaMethod("()V")
    isDone = JavaMethod("()Z")
    getAnimation = JavaMethod("()Landroid/view/animation/Animation;")
    setAnimation = JavaMultipleMethod([("(Landroid/content/Context;I)V", False, False), ("(Landroid/view/animation/Animation;)V", False, False)])
    getOrder = JavaMethod("()I")
    getInterpolator = JavaMethod("()Landroid/view/animation/Interpolator;")
    setInterpolator = JavaMultipleMethod([("(Landroid/view/animation/Interpolator;)V", False, False), ("(Landroid/content/Context;I)V", False, False)])

    class AnimationParameters(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/animation/LayoutAnimationController$AnimationParameters"
        __javaconstructor__ = [("()V", False)]
        count = JavaField("I")
        index = JavaField("I")