from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IntToDoubleFunction"]

class IntToDoubleFunction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/IntToDoubleFunction"
    applyAsDouble = JavaMethod("(I)D")