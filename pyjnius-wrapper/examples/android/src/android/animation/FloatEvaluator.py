from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FloatEvaluator"]

class FloatEvaluator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/FloatEvaluator"
    __javaconstructor__ = [("()V", False)]
    evaluate = JavaMethod("(FLjava/lang/Number;Ljava/lang/Number;)Ljava/lang/Float;")