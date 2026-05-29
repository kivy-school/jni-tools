from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BinaryOperator"]

class BinaryOperator(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/BinaryOperator"
    minBy = JavaStaticMethod("(Ljava/util/Comparator;)Ljava/util/function/BinaryOperator;")
    maxBy = JavaStaticMethod("(Ljava/util/Comparator;)Ljava/util/function/BinaryOperator;")