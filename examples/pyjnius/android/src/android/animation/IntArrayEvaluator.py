from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IntArrayEvaluator"]

class IntArrayEvaluator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/IntArrayEvaluator"
    __javaconstructor__ = [("()V", False), ("([I)V", False)]
    evaluate = JavaMultipleMethod([("(FLjava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;", False, False), ("(F[I[I)[I", False, False)])