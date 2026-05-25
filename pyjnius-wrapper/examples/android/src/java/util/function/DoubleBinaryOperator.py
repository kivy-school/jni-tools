from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DoubleBinaryOperator"]

class DoubleBinaryOperator(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/DoubleBinaryOperator"
    applyAsDouble = JavaMethod("(DD)D")