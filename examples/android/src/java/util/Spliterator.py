from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Spliterator"]

class Spliterator(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/Spliterator"
    CONCURRENT = JavaStaticField("I")
    DISTINCT = JavaStaticField("I")
    IMMUTABLE = JavaStaticField("I")
    NONNULL = JavaStaticField("I")
    ORDERED = JavaStaticField("I")
    SIZED = JavaStaticField("I")
    SORTED = JavaStaticField("I")
    SUBSIZED = JavaStaticField("I")
    tryAdvance = JavaMethod("(Ljava/util/function/Consumer;)Z")
    forEachRemaining = JavaMethod("(Ljava/util/function/Consumer;)V")
    trySplit = JavaMethod("()Ljava/util/Spliterator;")
    estimateSize = JavaMethod("()J")
    getExactSizeIfKnown = JavaMethod("()J")
    characteristics = JavaMethod("()I")
    hasCharacteristics = JavaMethod("(I)Z")
    getComparator = JavaMethod("()Ljava/util/Comparator;")

    class OfDouble(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/Spliterator/OfDouble"
        trySplit = JavaMethod("()Ljava/util/Spliterator$OfDouble;")
        tryAdvance = JavaMultipleMethod([("(Ljava/util/function/DoubleConsumer;)Z", False, False), ("(Ljava/util/function/Consumer;)Z", False, False)])
        forEachRemaining = JavaMultipleMethod([("(Ljava/util/function/DoubleConsumer;)V", False, False), ("(Ljava/util/function/Consumer;)V", False, False)])

    class OfInt(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/Spliterator/OfInt"
        trySplit = JavaMethod("()Ljava/util/Spliterator$OfInt;")
        tryAdvance = JavaMultipleMethod([("(Ljava/util/function/IntConsumer;)Z", False, False), ("(Ljava/util/function/Consumer;)Z", False, False)])
        forEachRemaining = JavaMultipleMethod([("(Ljava/util/function/IntConsumer;)V", False, False), ("(Ljava/util/function/Consumer;)V", False, False)])

    class OfLong(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/Spliterator/OfLong"
        trySplit = JavaMethod("()Ljava/util/Spliterator$OfLong;")
        tryAdvance = JavaMultipleMethod([("(Ljava/util/function/LongConsumer;)Z", False, False), ("(Ljava/util/function/Consumer;)Z", False, False)])
        forEachRemaining = JavaMultipleMethod([("(Ljava/util/function/LongConsumer;)V", False, False), ("(Ljava/util/function/Consumer;)V", False, False)])

    class OfPrimitive(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/Spliterator/OfPrimitive"
        trySplit = JavaMethod("()Ljava/util/Spliterator$OfPrimitive;")
        tryAdvance = JavaMethod("(Ljava/lang/Object;)Z")
        forEachRemaining = JavaMethod("(Ljava/lang/Object;)V")