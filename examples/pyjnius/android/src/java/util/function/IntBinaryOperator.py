from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IntBinaryOperator"]

class IntBinaryOperator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/IntBinaryOperator"
    applyAsInt = JavaMethod("(II)I")