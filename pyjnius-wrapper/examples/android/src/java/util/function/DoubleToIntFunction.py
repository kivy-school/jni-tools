from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DoubleToIntFunction"]

class DoubleToIntFunction(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/DoubleToIntFunction"
    applyAsInt = JavaMethod("(D)I")