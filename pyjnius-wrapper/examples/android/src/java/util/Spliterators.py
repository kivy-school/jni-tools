from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Spliterators"]

class Spliterators(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/Spliterators"
    emptySpliterator = JavaStaticMethod("()Ljava/util/Spliterator;")
    emptyIntSpliterator = JavaStaticMethod("()Ljava/util/Spliterator$OfInt;")
    emptyLongSpliterator = JavaStaticMethod("()Ljava/util/Spliterator$OfLong;")
    emptyDoubleSpliterator = JavaStaticMethod("()Ljava/util/Spliterator$OfDouble;")
    spliterator = JavaMultipleMethod([("([Ljava/lang/Object;I)Ljava/util/Spliterator;", True, False), ("([Ljava/lang/Object;III)Ljava/util/Spliterator;", True, False), ("([II)Ljava/util/Spliterator$OfInt;", True, False), ("([IIII)Ljava/util/Spliterator$OfInt;", True, False), ("([JI)Ljava/util/Spliterator$OfLong;", True, False), ("([JIII)Ljava/util/Spliterator$OfLong;", True, False), ("([DI)Ljava/util/Spliterator$OfDouble;", True, False), ("([DIII)Ljava/util/Spliterator$OfDouble;", True, False), ("(Ljava/util/Collection;I)Ljava/util/Spliterator;", True, False), ("(Ljava/util/Iterator;JI)Ljava/util/Spliterator;", True, False), ("(Ljava/util/PrimitiveIterator$OfInt;JI)Ljava/util/Spliterator$OfInt;", True, False), ("(Ljava/util/PrimitiveIterator$OfLong;JI)Ljava/util/Spliterator$OfLong;", True, False), ("(Ljava/util/PrimitiveIterator$OfDouble;JI)Ljava/util/Spliterator$OfDouble;", True, False)])
    spliteratorUnknownSize = JavaMultipleMethod([("(Ljava/util/Iterator;I)Ljava/util/Spliterator;", True, False), ("(Ljava/util/PrimitiveIterator$OfInt;I)Ljava/util/Spliterator$OfInt;", True, False), ("(Ljava/util/PrimitiveIterator$OfLong;I)Ljava/util/Spliterator$OfLong;", True, False), ("(Ljava/util/PrimitiveIterator$OfDouble;I)Ljava/util/Spliterator$OfDouble;", True, False)])
    iterator = JavaMultipleMethod([("(Ljava/util/Spliterator;)Ljava/util/Iterator;", True, False), ("(Ljava/util/Spliterator$OfInt;)Ljava/util/PrimitiveIterator$OfInt;", True, False), ("(Ljava/util/Spliterator$OfLong;)Ljava/util/PrimitiveIterator$OfLong;", True, False), ("(Ljava/util/Spliterator$OfDouble;)Ljava/util/PrimitiveIterator$OfDouble;", True, False)])

    class AbstractDoubleSpliterator(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/Spliterators/AbstractDoubleSpliterator"
        __javaconstructor__ = [("(JI)V", False)]
        trySplit = JavaMethod("()Ljava/util/Spliterator$OfDouble;")
        estimateSize = JavaMethod("()J")
        characteristics = JavaMethod("()I")

    class AbstractIntSpliterator(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/Spliterators/AbstractIntSpliterator"
        __javaconstructor__ = [("(JI)V", False)]
        trySplit = JavaMethod("()Ljava/util/Spliterator$OfInt;")
        estimateSize = JavaMethod("()J")
        characteristics = JavaMethod("()I")

    class AbstractLongSpliterator(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/Spliterators/AbstractLongSpliterator"
        __javaconstructor__ = [("(JI)V", False)]
        trySplit = JavaMethod("()Ljava/util/Spliterator$OfLong;")
        estimateSize = JavaMethod("()J")
        characteristics = JavaMethod("()I")

    class AbstractSpliterator(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/Spliterators/AbstractSpliterator"
        __javaconstructor__ = [("(JI)V", False)]
        trySplit = JavaMethod("()Ljava/util/Spliterator;")
        estimateSize = JavaMethod("()J")
        characteristics = JavaMethod("()I")