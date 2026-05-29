from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DoubleToIntFunction"]

class DoubleToIntFunction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/DoubleToIntFunction"
    applyAsInt = JavaMethod("(D)I")