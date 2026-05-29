from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Function"]

class Function(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/Function"
    apply = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    identity = JavaStaticMethod("()Ljava/util/function/Function;")
    compose = JavaMethod("(Ljava/util/function/Function;)Ljava/util/function/Function;")
    andThen = JavaMethod("(Ljava/util/function/Function;)Ljava/util/function/Function;")