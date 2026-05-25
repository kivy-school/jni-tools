from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TransitionDrawable"]

class TransitionDrawable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/drawable/TransitionDrawable"
    __javaconstructor__ = [("([Landroid/graphics/drawable/Drawable;)V", False)]
    startTransition = JavaMethod("(I)V")
    resetTransition = JavaMethod("()V")
    reverseTransition = JavaMethod("(I)V")
    draw = JavaMethod("(Landroid/graphics/Canvas;)V")
    setCrossFadeEnabled = JavaMethod("(Z)V")
    isCrossFadeEnabled = JavaMethod("()Z")