from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LongToDoubleFunction"]

class LongToDoubleFunction(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/LongToDoubleFunction"
    applyAsDouble = JavaMethod("(J)D")