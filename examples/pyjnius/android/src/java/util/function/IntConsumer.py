from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IntConsumer"]

class IntConsumer(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/IntConsumer"
    accept = JavaMethod("(I)V")
    andThen = JavaMethod("(Ljava/util/function/IntConsumer;)Ljava/util/function/IntConsumer;")