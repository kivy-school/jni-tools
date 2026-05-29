from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TranslateAnimation"]

class TranslateAnimation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/animation/TranslateAnimation"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(FFFF)V", False), ("(IFIFIFIF)V", False)]
    applyTransformation = JavaMethod("(FLandroid/view/animation/Transformation;)V")
    initialize = JavaMethod("(IIII)V")