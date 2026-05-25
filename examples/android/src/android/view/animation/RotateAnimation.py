from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RotateAnimation"]

class RotateAnimation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/animation/RotateAnimation"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(FF)V", False), ("(FFFF)V", False), ("(FFIFIF)V", False)]
    applyTransformation = JavaMethod("(FLandroid/view/animation/Transformation;)V")
    initialize = JavaMethod("(IIII)V")