from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TransitionDrawable"]

class TransitionDrawable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/drawable/TransitionDrawable"
    __javaconstructor__ = [("([Landroid/graphics/drawable/Drawable;)V", False)]
    INSET_UNDEFINED = JavaStaticField("I")
    PADDING_MODE_NEST = JavaStaticField("I")
    PADDING_MODE_STACK = JavaStaticField("I")
    reverseTransition = JavaMethod("(I)V")
    resetTransition = JavaMethod("()V")
    isCrossFadeEnabled = JavaMethod("()Z")
    setCrossFadeEnabled = JavaMethod("(Z)V")
    startTransition = JavaMethod("(I)V")
    draw = JavaMethod("(Landroid/graphics/Canvas;)V")