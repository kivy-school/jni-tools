from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WindowInsetsAnimationController"]

class WindowInsetsAnimationController(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/WindowInsetsAnimationController"
    getHiddenStateInsets = JavaMethod("()Landroid/graphics/Insets;")
    getShownStateInsets = JavaMethod("()Landroid/graphics/Insets;")
    getCurrentInsets = JavaMethod("()Landroid/graphics/Insets;")
    getCurrentFraction = JavaMethod("()F")
    getCurrentAlpha = JavaMethod("()F")
    getTypes = JavaMethod("()I")
    setInsetsAndAlpha = JavaMethod("(Landroid/graphics/Insets;FF)V")
    finish = JavaMethod("(Z)V")
    isReady = JavaMethod("()Z")
    isFinished = JavaMethod("()Z")
    isCancelled = JavaMethod("()Z")