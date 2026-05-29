from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BiConsumer"]

class BiConsumer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/BiConsumer"
    accept = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)V")
    andThen = JavaMethod("(Ljava/util/function/BiConsumer;)Ljava/util/function/BiConsumer;")