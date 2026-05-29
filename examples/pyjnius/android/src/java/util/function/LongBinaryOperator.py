from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LongBinaryOperator"]

class LongBinaryOperator(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/LongBinaryOperator"
    applyAsLong = JavaMethod("(JJ)J")