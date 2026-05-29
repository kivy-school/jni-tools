from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ThreadLocalRandom"]

class ThreadLocalRandom(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/ThreadLocalRandom"
    nextLong = JavaMultipleMethod([("(JJ)J", False, False), ("()J", False, False), ("(J)J", False, False)])
    nextBoolean = JavaMethod("()Z")
    current = JavaStaticMethod("()Ljava/util/concurrent/ThreadLocalRandom;")
    nextDouble = JavaMultipleMethod([("()D", False, False), ("(DD)D", False, False), ("(D)D", False, False)])
    nextFloat = JavaMultipleMethod([("(FF)F", False, False), ("(F)F", False, False), ("()F", False, False)])
    ints = JavaMultipleMethod([("(J)Ljava/util/stream/IntStream;", False, False), ("()Ljava/util/stream/IntStream;", False, False), ("(II)Ljava/util/stream/IntStream;", False, False), ("(JII)Ljava/util/stream/IntStream;", False, False)])
    doubles = JavaMultipleMethod([("(DD)Ljava/util/stream/DoubleStream;", False, False), ("(J)Ljava/util/stream/DoubleStream;", False, False), ("(JDD)Ljava/util/stream/DoubleStream;", False, False), ("()Ljava/util/stream/DoubleStream;", False, False)])
    setSeed = JavaMethod("(J)V")
    nextGaussian = JavaMethod("()D")
    nextInt = JavaMultipleMethod([("(II)I", False, False), ("()I", False, False), ("(I)I", False, False)])
    longs = JavaMultipleMethod([("()Ljava/util/stream/LongStream;", False, False), ("(JJJ)Ljava/util/stream/LongStream;", False, False), ("(JJ)Ljava/util/stream/LongStream;", False, False), ("(J)Ljava/util/stream/LongStream;", False, False)])