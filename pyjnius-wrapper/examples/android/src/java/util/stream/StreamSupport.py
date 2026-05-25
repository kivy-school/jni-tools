from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StreamSupport"]

class StreamSupport(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/stream/StreamSupport"
    stream = JavaMultipleMethod([("(Ljava/util/Spliterator;Z)Ljava/util/stream/Stream;", True, False), ("(Ljava/util/function/Supplier;IZ)Ljava/util/stream/Stream;", True, False)])
    intStream = JavaMultipleMethod([("(Ljava/util/Spliterator$OfInt;Z)Ljava/util/stream/IntStream;", True, False), ("(Ljava/util/function/Supplier;IZ)Ljava/util/stream/IntStream;", True, False)])
    longStream = JavaMultipleMethod([("(Ljava/util/Spliterator$OfLong;Z)Ljava/util/stream/LongStream;", True, False), ("(Ljava/util/function/Supplier;IZ)Ljava/util/stream/LongStream;", True, False)])
    doubleStream = JavaMultipleMethod([("(Ljava/util/Spliterator$OfDouble;Z)Ljava/util/stream/DoubleStream;", True, False), ("(Ljava/util/function/Supplier;IZ)Ljava/util/stream/DoubleStream;", True, False)])