from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Random"]

class Random(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/Random"
    __javaconstructor__ = [("()V", False), ("(J)V", False)]
    setSeed = JavaMethod("(J)V")
    next = JavaMethod("(I)I")
    nextBytes = JavaMethod("([B)V")
    nextInt = JavaMultipleMethod([("()I", False, False), ("(I)I", False, False)])
    nextLong = JavaMethod("()J")
    nextBoolean = JavaMethod("()Z")
    nextFloat = JavaMethod("()F")
    nextDouble = JavaMethod("()D")
    nextGaussian = JavaMethod("()D")
    ints = JavaMultipleMethod([("(J)Ljava/util/stream/IntStream;", False, False), ("()Ljava/util/stream/IntStream;", False, False), ("(JII)Ljava/util/stream/IntStream;", False, False), ("(II)Ljava/util/stream/IntStream;", False, False)])
    longs = JavaMultipleMethod([("(J)Ljava/util/stream/LongStream;", False, False), ("()Ljava/util/stream/LongStream;", False, False), ("(JJJ)Ljava/util/stream/LongStream;", False, False), ("(JJ)Ljava/util/stream/LongStream;", False, False)])
    doubles = JavaMultipleMethod([("(J)Ljava/util/stream/DoubleStream;", False, False), ("()Ljava/util/stream/DoubleStream;", False, False), ("(JDD)Ljava/util/stream/DoubleStream;", False, False), ("(DD)Ljava/util/stream/DoubleStream;", False, False)])