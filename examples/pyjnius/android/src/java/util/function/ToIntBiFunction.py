from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ToIntBiFunction"]

class ToIntBiFunction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/ToIntBiFunction"
    applyAsInt = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)I")