from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LongToIntFunction"]

class LongToIntFunction(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/LongToIntFunction"
    applyAsInt = JavaMethod("(J)I")