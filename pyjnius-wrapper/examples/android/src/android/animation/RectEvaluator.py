from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RectEvaluator"]

class RectEvaluator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/RectEvaluator"
    __javaconstructor__ = [("()V", False), ("(Landroid/graphics/Rect;)V", False)]
    evaluate = JavaMethod("(FLandroid/graphics/Rect;Landroid/graphics/Rect;)Landroid/graphics/Rect;")