from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BiFunction"]

class BiFunction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/BiFunction"
    apply = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    andThen = JavaMethod("(Ljava/util/function/Function;)Ljava/util/function/BiFunction;")