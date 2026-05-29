from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DoubleStream"]

class DoubleStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/stream/DoubleStream"
    min = JavaMethod("()Ljava/util/OptionalDouble;")
    max = JavaMethod("()Ljava/util/OptionalDouble;")
    of = JavaMultipleMethod([("(D)Ljava/util/stream/DoubleStream;", True, False), ("([D)Ljava/util/stream/DoubleStream;", True, True)])
    toArray = JavaMethod("()[D")
    iterator = JavaMultipleMethod([("()Ljava/util/Iterator;", False, False), ("()Ljava/util/PrimitiveIterator$OfDouble;", False, False)])
    map = JavaMethod("(Ljava/util/function/DoubleUnaryOperator;)Ljava/util/stream/DoubleStream;")
    collect = JavaMethod("(Ljava/util/function/Supplier;Ljava/util/function/ObjDoubleConsumer;Ljava/util/function/BiConsumer;)Ljava/lang/Object;")
    count = JavaMethod("()J")
    builder = JavaStaticMethod("()Ljava/util/stream/DoubleStream$Builder;")
    concat = JavaStaticMethod("(Ljava/util/stream/DoubleStream;Ljava/util/stream/DoubleStream;)Ljava/util/stream/DoubleStream;")
    limit = JavaMethod("(J)Ljava/util/stream/DoubleStream;")
    spliterator = JavaMultipleMethod([("()Ljava/util/Spliterator;", False, False), ("()Ljava/util/Spliterator$OfDouble;", False, False)])
    filter = JavaMethod("(Ljava/util/function/DoublePredicate;)Ljava/util/stream/DoubleStream;")
    empty = JavaStaticMethod("()Ljava/util/stream/DoubleStream;")
    anyMatch = JavaMethod("(Ljava/util/function/DoublePredicate;)Z")
    forEach = JavaMethod("(Ljava/util/function/DoubleConsumer;)V")
    findAny = JavaMethod("()Ljava/util/OptionalDouble;")
    skip = JavaMethod("(J)Ljava/util/stream/DoubleStream;")
    peek = JavaMethod("(Ljava/util/function/DoubleConsumer;)Ljava/util/stream/DoubleStream;")
    iterate = JavaMultipleMethod([("(DLjava/util/function/DoubleUnaryOperator;)Ljava/util/stream/DoubleStream;", True, False), ("(DLjava/util/function/DoublePredicate;Ljava/util/function/DoubleUnaryOperator;)Ljava/util/stream/DoubleStream;", True, False)])
    flatMap = JavaMethod("(Ljava/util/function/DoubleFunction;)Ljava/util/stream/DoubleStream;")
    allMatch = JavaMethod("(Ljava/util/function/DoublePredicate;)Z")
    dropWhile = JavaMethod("(Ljava/util/function/DoublePredicate;)Ljava/util/stream/DoubleStream;")
    parallel = JavaMultipleMethod([("()Ljava/util/stream/BaseStream;", False, False), ("()Ljava/util/stream/DoubleStream;", False, False)])
    mapToInt = JavaMethod("(Ljava/util/function/DoubleToIntFunction;)Ljava/util/stream/IntStream;")
    mapToLong = JavaMethod("(Ljava/util/function/DoubleToLongFunction;)Ljava/util/stream/LongStream;")
    mapMulti = JavaMethod("(Ljava/util/stream/DoubleStream$DoubleMapMultiConsumer;)Ljava/util/stream/DoubleStream;")
    takeWhile = JavaMethod("(Ljava/util/function/DoublePredicate;)Ljava/util/stream/DoubleStream;")
    forEachOrdered = JavaMethod("(Ljava/util/function/DoubleConsumer;)V")
    sequential = JavaMultipleMethod([("()Ljava/util/stream/DoubleStream;", False, False), ("()Ljava/util/stream/BaseStream;", False, False)])
    average = JavaMethod("()Ljava/util/OptionalDouble;")
    summaryStatistics = JavaMethod("()Ljava/util/DoubleSummaryStatistics;")
    boxed = JavaMethod("()Ljava/util/stream/Stream;")
    distinct = JavaMethod("()Ljava/util/stream/DoubleStream;")
    findFirst = JavaMethod("()Ljava/util/OptionalDouble;")
    noneMatch = JavaMethod("(Ljava/util/function/DoublePredicate;)Z")
    sum = JavaMethod("()D")
    reduce = JavaMultipleMethod([("(Ljava/util/function/DoubleBinaryOperator;)Ljava/util/OptionalDouble;", False, False), ("(DLjava/util/function/DoubleBinaryOperator;)D", False, False)])
    mapToObj = JavaMethod("(Ljava/util/function/DoubleFunction;)Ljava/util/stream/Stream;")
    sorted = JavaMethod("()Ljava/util/stream/DoubleStream;")
    generate = JavaStaticMethod("(Ljava/util/function/DoubleSupplier;)Ljava/util/stream/DoubleStream;")

    class DoubleMapMultiConsumer(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/stream/DoubleStream$DoubleMapMultiConsumer"
        accept = JavaMethod("(DLjava/util/function/DoubleConsumer;)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/stream/DoubleStream$Builder"
        add = JavaMethod("(D)Ljava/util/stream/DoubleStream$Builder;")
        accept = JavaMethod("(D)V")
        build = JavaMethod("()Ljava/util/stream/DoubleStream;")