from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IntToDoubleFunction"]

class IntToDoubleFunction(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/IntToDoubleFunction"
    applyAsDouble = JavaMethod("(I)D")