from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PointFEvaluator"]

class PointFEvaluator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/PointFEvaluator"
    __javaconstructor__ = [("()V", False), ("(Landroid/graphics/PointF;)V", False)]
    evaluate = JavaMultipleMethod([("(FLjava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;", False, False), ("(FLandroid/graphics/PointF;Landroid/graphics/PointF;)Landroid/graphics/PointF;", False, False)])