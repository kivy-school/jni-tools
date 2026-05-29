from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LongConsumer"]

class LongConsumer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/LongConsumer"
    accept = JavaMethod("(J)V")
    andThen = JavaMethod("(Ljava/util/function/LongConsumer;)Ljava/util/function/LongConsumer;")