from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ArgbEvaluator"]

class ArgbEvaluator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/ArgbEvaluator"
    __javaconstructor__ = [("()V", False)]
    evaluate = JavaMethod("(FLjava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")