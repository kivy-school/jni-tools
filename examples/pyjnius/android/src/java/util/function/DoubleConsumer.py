from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DoubleConsumer"]

class DoubleConsumer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/DoubleConsumer"
    accept = JavaMethod("(D)V")
    andThen = JavaMethod("(Ljava/util/function/DoubleConsumer;)Ljava/util/function/DoubleConsumer;")