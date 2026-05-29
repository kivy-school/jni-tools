from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FloatEvaluator"]

class FloatEvaluator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/FloatEvaluator"
    __javaconstructor__ = [("()V", False)]
    evaluate = JavaMultipleMethod([("(FLjava/lang/Number;Ljava/lang/Number;)Ljava/lang/Float;", False, False), ("(FLjava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;", False, False)])