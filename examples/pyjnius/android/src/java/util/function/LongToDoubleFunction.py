from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LongToDoubleFunction"]

class LongToDoubleFunction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/LongToDoubleFunction"
    applyAsDouble = JavaMethod("(J)D")