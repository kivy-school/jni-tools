from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IntBinaryOperator"]

class IntBinaryOperator(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/IntBinaryOperator"
    applyAsInt = JavaMethod("(II)I")