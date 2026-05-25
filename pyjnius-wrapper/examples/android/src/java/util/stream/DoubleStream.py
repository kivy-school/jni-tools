from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DoubleStream"]

class DoubleStream(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/stream/DoubleStream"
    filter = JavaMethod("(Ljava/util/function/DoublePredicate;)Ljava/util/stream/DoubleStream;")
    map = JavaMethod("(Ljava/util/function/DoubleUnaryOperator;)Ljava/util/stream/DoubleStream;")
    mapToObj = JavaMethod("(Ljava/util/function/DoubleFunction;)Ljava/util/stream/Stream;")
    mapToInt = JavaMethod("(Ljava/util/function/DoubleToIntFunction;)Ljava/util/stream/IntStream;")
    mapToLong = JavaMethod("(Ljava/util/function/DoubleToLongFunction;)Ljava/util/stream/LongStream;")
    flatMap = JavaMethod("(Ljava/util/function/DoubleFunction;)Ljava/util/stream/DoubleStream;")
    mapMulti = JavaMethod("(Ljava/util/stream/DoubleStream$DoubleMapMultiConsumer;)Ljava/util/stream/DoubleStream;")
    distinct = JavaMethod("()Ljava/util/stream/DoubleStream;")
    sorted = JavaMethod("()Ljava/util/stream/DoubleStream;")
    peek = JavaMethod("(Ljava/util/function/DoubleConsumer;)Ljava/util/stream/DoubleStream;")
    limit = JavaMethod("(J)Ljava/util/stream/DoubleStream;")
    skip = JavaMethod("(J)Ljava/util/stream/DoubleStream;")
    takeWhile = JavaMethod("(Ljava/util/function/DoublePredicate;)Ljava/util/stream/DoubleStream;")
    dropWhile = JavaMethod("(Ljava/util/function/DoublePredicate;)Ljava/util/stream/DoubleStream;")
    forEach = JavaMethod("(Ljava/util/function/DoubleConsumer;)V")
    forEachOrdered = JavaMethod("(Ljava/util/function/DoubleConsumer;)V")
    toArray = JavaMethod("()[D")
    reduce = JavaMultipleMethod([("(DLjava/util/function/DoubleBinaryOperator;)D", False, False), ("(Ljava/util/function/DoubleBinaryOperator;)Ljava/util/OptionalDouble;", False, False)])
    collect = JavaMethod("(Ljava/util/function/Supplier;Ljava/util/function/ObjDoubleConsumer;Ljava/util/function/BiConsumer;)Ljava/lang/Object;")
    sum = JavaMethod("()D")
    min = JavaMethod("()Ljava/util/OptionalDouble;")
    max = JavaMethod("()Ljava/util/OptionalDouble;")
    count = JavaMethod("()J")
    average = JavaMethod("()Ljava/util/OptionalDouble;")
    summaryStatistics = JavaMethod("()Ljava/util/DoubleSummaryStatistics;")
    anyMatch = JavaMethod("(Ljava/util/function/DoublePredicate;)Z")
    allMatch = JavaMethod("(Ljava/util/function/DoublePredicate;)Z")
    noneMatch = JavaMethod("(Ljava/util/function/DoublePredicate;)Z")
    findFirst = JavaMethod("()Ljava/util/OptionalDouble;")
    findAny = JavaMethod("()Ljava/util/OptionalDouble;")
    boxed = JavaMethod("()Ljava/util/stream/Stream;")
    sequential = JavaMethod("()Ljava/util/stream/DoubleStream;")
    parallel = JavaMethod("()Ljava/util/stream/DoubleStream;")
    iterator = JavaMethod("()Ljava/util/PrimitiveIterator$OfDouble;")
    spliterator = JavaMethod("()Ljava/util/Spliterator$OfDouble;")
    builder = JavaStaticMethod("()Ljava/util/stream/DoubleStream$Builder;")
    empty = JavaStaticMethod("()Ljava/util/stream/DoubleStream;")
    of = JavaMultipleMethod([("(D)Ljava/util/stream/DoubleStream;", True, False), ("([D)Ljava/util/stream/DoubleStream;", True, True)])
    iterate = JavaMultipleMethod([("(DLjava/util/function/DoubleUnaryOperator;)Ljava/util/stream/DoubleStream;", True, False), ("(DLjava/util/function/DoublePredicate;Ljava/util/function/DoubleUnaryOperator;)Ljava/util/stream/DoubleStream;", True, False)])
    generate = JavaStaticMethod("(Ljava/util/function/DoubleSupplier;)Ljava/util/stream/DoubleStream;")
    concat = JavaStaticMethod("(Ljava/util/stream/DoubleStream;Ljava/util/stream/DoubleStream;)Ljava/util/stream/DoubleStream;")

    class Builder(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/stream/DoubleStream/Builder"
        accept = JavaMethod("(D)V")
        add = JavaMethod("(D)Ljava/util/stream/DoubleStream$Builder;")
        build = JavaMethod("()Ljava/util/stream/DoubleStream;")

    class DoubleMapMultiConsumer(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/stream/DoubleStream/DoubleMapMultiConsumer"
        accept = JavaMethod("(DLjava/util/function/DoubleConsumer;)V")