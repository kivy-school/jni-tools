from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TypeEvaluator"]

class TypeEvaluator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/TypeEvaluator"
    evaluate = JavaMethod("(FLjava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")