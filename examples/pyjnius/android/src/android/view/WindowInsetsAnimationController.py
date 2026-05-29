from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WindowInsetsAnimationController"]

class WindowInsetsAnimationController(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/WindowInsetsAnimationController"
    isReady = JavaMethod("()Z")
    getCurrentInsets = JavaMethod("()Landroid/graphics/Insets;")
    getTypes = JavaMethod("()I")
    isCancelled = JavaMethod("()Z")
    setInsetsAndAlpha = JavaMethod("(Landroid/graphics/Insets;FF)V")
    getCurrentFraction = JavaMethod("()F")
    getCurrentAlpha = JavaMethod("()F")
    getHiddenStateInsets = JavaMethod("()Landroid/graphics/Insets;")
    getShownStateInsets = JavaMethod("()Landroid/graphics/Insets;")
    finish = JavaMethod("(Z)V")
    isFinished = JavaMethod("()Z")