from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ToIntFunction"]

class ToIntFunction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/ToIntFunction"
    applyAsInt = JavaMethod("(Ljava/lang/Object;)I")