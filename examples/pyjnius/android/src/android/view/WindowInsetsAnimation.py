from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WindowInsetsAnimation"]

class WindowInsetsAnimation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/WindowInsetsAnimation"
    __javaconstructor__ = [("(ILandroid/view/animation/Interpolator;J)V", False)]
    getTypeMask = JavaMethod("()I")
    getFraction = JavaMethod("()F")
    getInterpolatedFraction = JavaMethod("()F")
    getInterpolator = JavaMethod("()Landroid/view/animation/Interpolator;")
    getDurationMillis = JavaMethod("()J")
    setFraction = JavaMethod("(F)V")
    getAlpha = JavaMethod("()F")
    setAlpha = JavaMethod("(F)V")

    class Bounds(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/WindowInsetsAnimation/Bounds"
        __javaconstructor__ = [("(Landroid/graphics/Insets;Landroid/graphics/Insets;)V", False)]
        getLowerBound = JavaMethod("()Landroid/graphics/Insets;")
        getUpperBound = JavaMethod("()Landroid/graphics/Insets;")
        inset = JavaMethod("(Landroid/graphics/Insets;)Landroid/view/WindowInsetsAnimation$Bounds;")
        toString = JavaMethod("()Ljava/lang/String;")

    class Callback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/WindowInsetsAnimation/Callback"
        __javaconstructor__ = [("(I)V", False)]
        DISPATCH_MODE_CONTINUE_ON_SUBTREE = JavaStaticField("I")
        DISPATCH_MODE_STOP = JavaStaticField("I")
        getDispatchMode = JavaMethod("()I")
        onPrepare = JavaMethod("(Landroid/view/WindowInsetsAnimation;)V")
        onStart = JavaMethod("(Landroid/view/WindowInsetsAnimation;Landroid/view/WindowInsetsAnimation$Bounds;)Landroid/view/WindowInsetsAnimation$Bounds;")
        onProgress = JavaMethod("(Landroid/view/WindowInsets;Ljava/util/List;)Landroid/view/WindowInsets;")
        onEnd = JavaMethod("(Landroid/view/WindowInsetsAnimation;)V")