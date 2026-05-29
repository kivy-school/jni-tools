from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LongToIntFunction"]

class LongToIntFunction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/LongToIntFunction"
    applyAsInt = JavaMethod("(J)I")