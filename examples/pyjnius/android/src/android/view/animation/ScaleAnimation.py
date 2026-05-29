from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ScaleAnimation"]

class ScaleAnimation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/animation/ScaleAnimation"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(FFFF)V", False), ("(FFFFFF)V", False), ("(FFFFIFIF)V", False)]
    applyTransformation = JavaMethod("(FLandroid/view/animation/Transformation;)V")
    initialize = JavaMethod("(IIII)V")