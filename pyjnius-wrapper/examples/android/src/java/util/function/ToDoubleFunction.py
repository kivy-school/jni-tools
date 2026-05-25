from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ToDoubleFunction"]

class ToDoubleFunction(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/ToDoubleFunction"
    applyAsDouble = JavaMethod("(Ljava/lang/Object;)D")