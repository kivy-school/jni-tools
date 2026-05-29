from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Spliterators"]

class Spliterators(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/Spliterators"
    iterator = JavaMultipleMethod([("(Ljava/util/Spliterator$OfDouble;)Ljava/util/PrimitiveIterator$OfDouble;", True, False), ("(Ljava/util/Spliterator;)Ljava/util/Iterator;", True, False), ("(Ljava/util/Spliterator$OfInt;)Ljava/util/PrimitiveIterator$OfInt;", True, False), ("(Ljava/util/Spliterator$OfLong;)Ljava/util/PrimitiveIterator$OfLong;", True, False)])
    spliteratorUnknownSize = JavaMultipleMethod([("(Ljava/util/PrimitiveIterator$OfInt;I)Ljava/util/Spliterator$OfInt;", True, False), ("(Ljava/util/PrimitiveIterator$OfLong;I)Ljava/util/Spliterator$OfLong;", True, False), ("(Ljava/util/PrimitiveIterator$OfDouble;I)Ljava/util/Spliterator$OfDouble;", True, False), ("(Ljava/util/Iterator;I)Ljava/util/Spliterator;", True, False)])
    spliterator = JavaMultipleMethod([("([Ljava/lang/Object;I)Ljava/util/Spliterator;", True, False), ("(Ljava/util/Iterator;JI)Ljava/util/Spliterator;", True, False), ("(Ljava/util/Collection;I)Ljava/util/Spliterator;", True, False), ("(Ljava/util/PrimitiveIterator$OfInt;JI)Ljava/util/Spliterator$OfInt;", True, False), ("(Ljava/util/PrimitiveIterator$OfLong;JI)Ljava/util/Spliterator$OfLong;", True, False), ("(Ljava/util/PrimitiveIterator$OfDouble;JI)Ljava/util/Spliterator$OfDouble;", True, False), ("([JIII)Ljava/util/Spliterator$OfLong;", True, False), ("([JI)Ljava/util/Spliterator$OfLong;", True, False), ("([IIII)Ljava/util/Spliterator$OfInt;", True, False), ("([Ljava/lang/Object;III)Ljava/util/Spliterator;", True, False), ("([DI)Ljava/util/Spliterator$OfDouble;", True, False), ("([DIII)Ljava/util/Spliterator$OfDouble;", True, False), ("([II)Ljava/util/Spliterator$OfInt;", True, False)])
    emptySpliterator = JavaStaticMethod("()Ljava/util/Spliterator;")
    emptyIntSpliterator = JavaStaticMethod("()Ljava/util/Spliterator$OfInt;")
    emptyDoubleSpliterator = JavaStaticMethod("()Ljava/util/Spliterator$OfDouble;")
    emptyLongSpliterator = JavaStaticMethod("()Ljava/util/Spliterator$OfLong;")

    class AbstractDoubleSpliterator(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/Spliterators$AbstractDoubleSpliterator"
        ORDERED = JavaStaticField("I")
        DISTINCT = JavaStaticField("I")
        SORTED = JavaStaticField("I")
        SIZED = JavaStaticField("I")
        NONNULL = JavaStaticField("I")
        IMMUTABLE = JavaStaticField("I")
        CONCURRENT = JavaStaticField("I")
        SUBSIZED = JavaStaticField("I")
        characteristics = JavaMethod("()I")
        trySplit = JavaMultipleMethod([("()Ljava/util/Spliterator;", False, False), ("()Ljava/util/Spliterator$OfDouble;", False, False), ("()Ljava/util/Spliterator$OfPrimitive;", False, False)])
        estimateSize = JavaMethod("()J")

    class AbstractLongSpliterator(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/Spliterators$AbstractLongSpliterator"
        ORDERED = JavaStaticField("I")
        DISTINCT = JavaStaticField("I")
        SORTED = JavaStaticField("I")
        SIZED = JavaStaticField("I")
        NONNULL = JavaStaticField("I")
        IMMUTABLE = JavaStaticField("I")
        CONCURRENT = JavaStaticField("I")
        SUBSIZED = JavaStaticField("I")
        characteristics = JavaMethod("()I")
        trySplit = JavaMultipleMethod([("()Ljava/util/Spliterator;", False, False), ("()Ljava/util/Spliterator$OfLong;", False, False), ("()Ljava/util/Spliterator$OfPrimitive;", False, False)])
        estimateSize = JavaMethod("()J")

    class AbstractIntSpliterator(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/Spliterators$AbstractIntSpliterator"
        ORDERED = JavaStaticField("I")
        DISTINCT = JavaStaticField("I")
        SORTED = JavaStaticField("I")
        SIZED = JavaStaticField("I")
        NONNULL = JavaStaticField("I")
        IMMUTABLE = JavaStaticField("I")
        CONCURRENT = JavaStaticField("I")
        SUBSIZED = JavaStaticField("I")
        characteristics = JavaMethod("()I")
        trySplit = JavaMultipleMethod([("()Ljava/util/Spliterator;", False, False), ("()Ljava/util/Spliterator$OfInt;", False, False), ("()Ljava/util/Spliterator$OfPrimitive;", False, False)])
        estimateSize = JavaMethod("()J")

    class AbstractSpliterator(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/Spliterators$AbstractSpliterator"
        ORDERED = JavaStaticField("I")
        DISTINCT = JavaStaticField("I")
        SORTED = JavaStaticField("I")
        SIZED = JavaStaticField("I")
        NONNULL = JavaStaticField("I")
        IMMUTABLE = JavaStaticField("I")
        CONCURRENT = JavaStaticField("I")
        SUBSIZED = JavaStaticField("I")
        characteristics = JavaMethod("()I")
        trySplit = JavaMethod("()Ljava/util/Spliterator;")
        estimateSize = JavaMethod("()J")