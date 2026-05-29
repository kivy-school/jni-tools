from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Spliterator"]

class Spliterator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/Spliterator"
    ORDERED = JavaStaticField("I")
    DISTINCT = JavaStaticField("I")
    SORTED = JavaStaticField("I")
    SIZED = JavaStaticField("I")
    NONNULL = JavaStaticField("I")
    IMMUTABLE = JavaStaticField("I")
    CONCURRENT = JavaStaticField("I")
    SUBSIZED = JavaStaticField("I")
    forEachRemaining = JavaMethod("(Ljava/util/function/Consumer;)V")
    characteristics = JavaMethod("()I")
    getComparator = JavaMethod("()Ljava/util/Comparator;")
    trySplit = JavaMethod("()Ljava/util/Spliterator;")
    tryAdvance = JavaMethod("(Ljava/util/function/Consumer;)Z")
    estimateSize = JavaMethod("()J")
    getExactSizeIfKnown = JavaMethod("()J")
    hasCharacteristics = JavaMethod("(I)Z")

    class OfDouble(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/Spliterator$OfDouble"
        ORDERED = JavaStaticField("I")
        DISTINCT = JavaStaticField("I")
        SORTED = JavaStaticField("I")
        SIZED = JavaStaticField("I")
        NONNULL = JavaStaticField("I")
        IMMUTABLE = JavaStaticField("I")
        CONCURRENT = JavaStaticField("I")
        SUBSIZED = JavaStaticField("I")
        forEachRemaining = JavaMultipleMethod([("(Ljava/lang/Object;)V", False, False), ("(Ljava/util/function/DoubleConsumer;)V", False, False), ("(Ljava/util/function/Consumer;)V", False, False)])
        trySplit = JavaMultipleMethod([("()Ljava/util/Spliterator$OfPrimitive;", False, False), ("()Ljava/util/Spliterator;", False, False), ("()Ljava/util/Spliterator$OfDouble;", False, False)])
        tryAdvance = JavaMultipleMethod([("(Ljava/util/function/DoubleConsumer;)Z", False, False), ("(Ljava/util/function/Consumer;)Z", False, False), ("(Ljava/lang/Object;)Z", False, False)])

    class OfLong(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/Spliterator$OfLong"
        ORDERED = JavaStaticField("I")
        DISTINCT = JavaStaticField("I")
        SORTED = JavaStaticField("I")
        SIZED = JavaStaticField("I")
        NONNULL = JavaStaticField("I")
        IMMUTABLE = JavaStaticField("I")
        CONCURRENT = JavaStaticField("I")
        SUBSIZED = JavaStaticField("I")
        forEachRemaining = JavaMultipleMethod([("(Ljava/lang/Object;)V", False, False), ("(Ljava/util/function/LongConsumer;)V", False, False), ("(Ljava/util/function/Consumer;)V", False, False)])
        trySplit = JavaMultipleMethod([("()Ljava/util/Spliterator$OfPrimitive;", False, False), ("()Ljava/util/Spliterator;", False, False), ("()Ljava/util/Spliterator$OfLong;", False, False)])
        tryAdvance = JavaMultipleMethod([("(Ljava/util/function/LongConsumer;)Z", False, False), ("(Ljava/util/function/Consumer;)Z", False, False), ("(Ljava/lang/Object;)Z", False, False)])

    class OfInt(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/Spliterator$OfInt"
        ORDERED = JavaStaticField("I")
        DISTINCT = JavaStaticField("I")
        SORTED = JavaStaticField("I")
        SIZED = JavaStaticField("I")
        NONNULL = JavaStaticField("I")
        IMMUTABLE = JavaStaticField("I")
        CONCURRENT = JavaStaticField("I")
        SUBSIZED = JavaStaticField("I")
        forEachRemaining = JavaMultipleMethod([("(Ljava/lang/Object;)V", False, False), ("(Ljava/util/function/IntConsumer;)V", False, False), ("(Ljava/util/function/Consumer;)V", False, False)])
        trySplit = JavaMultipleMethod([("()Ljava/util/Spliterator$OfPrimitive;", False, False), ("()Ljava/util/Spliterator;", False, False), ("()Ljava/util/Spliterator$OfInt;", False, False)])
        tryAdvance = JavaMultipleMethod([("(Ljava/util/function/IntConsumer;)Z", False, False), ("(Ljava/util/function/Consumer;)Z", False, False), ("(Ljava/lang/Object;)Z", False, False)])

    class OfPrimitive(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/Spliterator$OfPrimitive"
        ORDERED = JavaStaticField("I")
        DISTINCT = JavaStaticField("I")
        SORTED = JavaStaticField("I")
        SIZED = JavaStaticField("I")
        NONNULL = JavaStaticField("I")
        IMMUTABLE = JavaStaticField("I")
        CONCURRENT = JavaStaticField("I")
        SUBSIZED = JavaStaticField("I")
        forEachRemaining = JavaMethod("(Ljava/lang/Object;)V")
        trySplit = JavaMultipleMethod([("()Ljava/util/Spliterator;", False, False), ("()Ljava/util/Spliterator$OfPrimitive;", False, False)])
        tryAdvance = JavaMethod("(Ljava/lang/Object;)Z")