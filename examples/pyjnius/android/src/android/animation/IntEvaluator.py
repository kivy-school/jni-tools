from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IntEvaluator"]

class IntEvaluator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/IntEvaluator"
    __javaconstructor__ = [("()V", False)]
    evaluate = JavaMultipleMethod([("(FLjava/lang/Integer;Ljava/lang/Integer;)Ljava/lang/Integer;", False, False), ("(FLjava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;", False, False)])