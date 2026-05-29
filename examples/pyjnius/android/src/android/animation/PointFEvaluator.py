from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PointFEvaluator"]

class PointFEvaluator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/PointFEvaluator"
    __javaconstructor__ = [("()V", False), ("(Landroid/graphics/PointF;)V", False)]
    evaluate = JavaMethod("(FLandroid/graphics/PointF;Landroid/graphics/PointF;)Landroid/graphics/PointF;")