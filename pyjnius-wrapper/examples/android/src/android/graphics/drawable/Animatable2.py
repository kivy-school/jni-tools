from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Animatable2"]

class Animatable2(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/drawable/Animatable2"
    registerAnimationCallback = JavaMethod("(Landroid/graphics/drawable/Animatable2$AnimationCallback;)V")
    unregisterAnimationCallback = JavaMethod("(Landroid/graphics/drawable/Animatable2$AnimationCallback;)Z")
    clearAnimationCallbacks = JavaMethod("()V")

    class AnimationCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/drawable/Animatable2/AnimationCallback"
        __javaconstructor__ = [("()V", False)]
        onAnimationStart = JavaMethod("(Landroid/graphics/drawable/Drawable;)V")
        onAnimationEnd = JavaMethod("(Landroid/graphics/drawable/Drawable;)V")