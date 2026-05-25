from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FloatArrayEvaluator"]

class FloatArrayEvaluator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/FloatArrayEvaluator"
    __javaconstructor__ = [("()V", False), ("([F)V", False)]
    evaluate = JavaMethod("(F[F[F)[F")