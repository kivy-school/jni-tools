from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Function"]

class Function(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/Function"
    apply = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    compose = JavaMethod("(Ljava/util/function/Function;)Ljava/util/function/Function;")
    andThen = JavaMethod("(Ljava/util/function/Function;)Ljava/util/function/Function;")
    identity = JavaStaticMethod("()Ljava/util/function/Function;")