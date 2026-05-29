from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DoubleBinaryOperator"]

class DoubleBinaryOperator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/DoubleBinaryOperator"
    applyAsDouble = JavaMethod("(DD)D")