from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FloatArrayEvaluator"]

class FloatArrayEvaluator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/FloatArrayEvaluator"
    __javaconstructor__ = [("()V", False), ("([F)V", False)]
    evaluate = JavaMultipleMethod([("(FLjava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;", False, False), ("(F[F[F)[F", False, False)])