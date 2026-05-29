from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LongBinaryOperator"]

class LongBinaryOperator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/LongBinaryOperator"
    applyAsLong = JavaMethod("(JJ)J")