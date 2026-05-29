from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ThreadLocalRandom"]

class ThreadLocalRandom(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/ThreadLocalRandom"
    current = JavaStaticMethod("()Ljava/util/concurrent/ThreadLocalRandom;")
    setSeed = JavaMethod("(J)V")
    next = JavaMethod("(I)I")
    nextBoolean = JavaMethod("()Z")
    nextInt = JavaMultipleMethod([("()I", False, False), ("(I)I", False, False), ("(II)I", False, False)])
    nextLong = JavaMultipleMethod([("()J", False, False), ("(J)J", False, False), ("(JJ)J", False, False)])
    nextFloat = JavaMultipleMethod([("()F", False, False), ("(F)F", False, False), ("(FF)F", False, False)])
    nextDouble = JavaMultipleMethod([("()D", False, False), ("(D)D", False, False), ("(DD)D", False, False)])
    ints = JavaMultipleMethod([("(J)Ljava/util/stream/IntStream;", False, False), ("()Ljava/util/stream/IntStream;", False, False), ("(JII)Ljava/util/stream/IntStream;", False, False), ("(II)Ljava/util/stream/IntStream;", False, False)])
    longs = JavaMultipleMethod([("(J)Ljava/util/stream/LongStream;", False, False), ("()Ljava/util/stream/LongStream;", False, False), ("(JJJ)Ljava/util/stream/LongStream;", False, False), ("(JJ)Ljava/util/stream/LongStream;", False, False)])
    doubles = JavaMultipleMethod([("(J)Ljava/util/stream/DoubleStream;", False, False), ("()Ljava/util/stream/DoubleStream;", False, False), ("(JDD)Ljava/util/stream/DoubleStream;", False, False), ("(DD)Ljava/util/stream/DoubleStream;", False, False)])