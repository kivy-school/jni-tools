from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IntEvaluator"]

class IntEvaluator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/IntEvaluator"
    __javaconstructor__ = [("()V", False)]
    evaluate = JavaMethod("(FLjava/lang/Integer;Ljava/lang/Integer;)Ljava/lang/Integer;")