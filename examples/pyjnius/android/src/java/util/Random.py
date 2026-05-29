from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Random"]

class Random(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/Random"
    __javaconstructor__ = [("()V", False), ("(J)V", False)]
    nextLong = JavaMethod("()J")
    nextBoolean = JavaMethod("()Z")
    from = JavaStaticMethod("(Ljava/util/random/RandomGenerator;)Ljava/util/Random;")
    nextDouble = JavaMethod("()D")
    nextFloat = JavaMethod("()F")
    ints = JavaMultipleMethod([("(JII)Ljava/util/stream/IntStream;", False, False), ("(J)Ljava/util/stream/IntStream;", False, False), ("(II)Ljava/util/stream/IntStream;", False, False), ("()Ljava/util/stream/IntStream;", False, False)])
    doubles = JavaMultipleMethod([("()Ljava/util/stream/DoubleStream;", False, False), ("(DD)Ljava/util/stream/DoubleStream;", False, False), ("(J)Ljava/util/stream/DoubleStream;", False, False), ("(JDD)Ljava/util/stream/DoubleStream;", False, False)])
    setSeed = JavaMethod("(J)V")
    nextGaussian = JavaMethod("()D")
    nextInt = JavaMultipleMethod([("(I)I", False, False), ("()I", False, False)])
    nextBytes = JavaMethod("([B)V")
    longs = JavaMultipleMethod([("()Ljava/util/stream/LongStream;", False, False), ("(J)Ljava/util/stream/LongStream;", False, False), ("(JJ)Ljava/util/stream/LongStream;", False, False), ("(JJJ)Ljava/util/stream/LongStream;", False, False)])