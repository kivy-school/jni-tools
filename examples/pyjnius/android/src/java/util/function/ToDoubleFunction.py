from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ToDoubleFunction"]

class ToDoubleFunction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/ToDoubleFunction"
    applyAsDouble = JavaMethod("(Ljava/lang/Object;)D")