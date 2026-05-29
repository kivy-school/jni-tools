from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IntArrayEvaluator"]

class IntArrayEvaluator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/IntArrayEvaluator"
    __javaconstructor__ = [("()V", False), ("([I)V", False)]
    evaluate = JavaMethod("(F[I[I)[I")