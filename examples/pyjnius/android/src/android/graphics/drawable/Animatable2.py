from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Animatable2"]

class Animatable2(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/drawable/Animatable2"
    clearAnimationCallbacks = JavaMethod("()V")
    registerAnimationCallback = JavaMethod("(Landroid/graphics/drawable/Animatable2$AnimationCallback;)V")
    unregisterAnimationCallback = JavaMethod("(Landroid/graphics/drawable/Animatable2$AnimationCallback;)Z")

    class AnimationCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/drawable/Animatable2$AnimationCallback"
        __javaconstructor__ = [("()V", False)]
        onAnimationEnd = JavaMethod("(Landroid/graphics/drawable/Drawable;)V")
        onAnimationStart = JavaMethod("(Landroid/graphics/drawable/Drawable;)V")