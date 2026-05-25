from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ToIntFunction"]

class ToIntFunction(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/ToIntFunction"
    applyAsInt = JavaMethod("(Ljava/lang/Object;)I")