from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ToLongBiFunction"]

class ToLongBiFunction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/ToLongBiFunction"
    applyAsLong = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)J")