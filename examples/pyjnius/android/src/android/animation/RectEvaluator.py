from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RectEvaluator"]

class RectEvaluator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/RectEvaluator"
    __javaconstructor__ = [("()V", False), ("(Landroid/graphics/Rect;)V", False)]
    evaluate = JavaMultipleMethod([("(FLjava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;", False, False), ("(FLandroid/graphics/Rect;Landroid/graphics/Rect;)Landroid/graphics/Rect;", False, False)])