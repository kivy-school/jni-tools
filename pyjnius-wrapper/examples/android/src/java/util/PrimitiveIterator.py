from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PrimitiveIterator"]

class PrimitiveIterator(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/PrimitiveIterator"
    forEachRemaining = JavaMethod("(Ljava/lang/Object;)V")

    class OfDouble(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/PrimitiveIterator/OfDouble"
        nextDouble = JavaMethod("()D")
        forEachRemaining = JavaMultipleMethod([("(Ljava/util/function/DoubleConsumer;)V", False, False), ("(Ljava/util/function/Consumer;)V", False, False)])
        next = JavaMethod("()Ljava/lang/Double;")

    class OfInt(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/PrimitiveIterator/OfInt"
        nextInt = JavaMethod("()I")
        forEachRemaining = JavaMultipleMethod([("(Ljava/util/function/IntConsumer;)V", False, False), ("(Ljava/util/function/Consumer;)V", False, False)])
        next = JavaMethod("()Ljava/lang/Integer;")

    class OfLong(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/PrimitiveIterator/OfLong"
        nextLong = JavaMethod("()J")
        forEachRemaining = JavaMultipleMethod([("(Ljava/util/function/LongConsumer;)V", False, False), ("(Ljava/util/function/Consumer;)V", False, False)])
        next = JavaMethod("()Ljava/lang/Long;")