from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PrimitiveIterator"]

class PrimitiveIterator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/PrimitiveIterator"
    forEachRemaining = JavaMethod("(Ljava/lang/Object;)V")

    class OfDouble(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/PrimitiveIterator$OfDouble"
        forEachRemaining = JavaMultipleMethod([("(Ljava/lang/Object;)V", False, False), ("(Ljava/util/function/DoubleConsumer;)V", False, False), ("(Ljava/util/function/Consumer;)V", False, False)])
        next = JavaMultipleMethod([("()Ljava/lang/Object;", False, False), ("()Ljava/lang/Double;", False, False)])
        nextDouble = JavaMethod("()D")

    class OfLong(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/PrimitiveIterator$OfLong"
        nextLong = JavaMethod("()J")
        forEachRemaining = JavaMultipleMethod([("(Ljava/lang/Object;)V", False, False), ("(Ljava/util/function/Consumer;)V", False, False), ("(Ljava/util/function/LongConsumer;)V", False, False)])
        next = JavaMultipleMethod([("()Ljava/lang/Long;", False, False), ("()Ljava/lang/Object;", False, False)])

    class OfInt(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/PrimitiveIterator$OfInt"
        forEachRemaining = JavaMultipleMethod([("(Ljava/lang/Object;)V", False, False), ("(Ljava/util/function/IntConsumer;)V", False, False), ("(Ljava/util/function/Consumer;)V", False, False)])
        next = JavaMultipleMethod([("()Ljava/lang/Object;", False, False), ("()Ljava/lang/Integer;", False, False)])
        nextInt = JavaMethod("()I")