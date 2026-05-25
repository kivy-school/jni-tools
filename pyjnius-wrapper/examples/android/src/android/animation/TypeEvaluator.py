from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TypeEvaluator"]

class TypeEvaluator(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/TypeEvaluator"
    evaluate = JavaMethod("(FLjava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")