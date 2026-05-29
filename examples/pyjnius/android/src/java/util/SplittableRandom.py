from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SplittableRandom"]

class SplittableRandom(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/SplittableRandom"
    __javaconstructor__ = [("(J)V", False), ("()V", False)]
    nextLong = JavaMethod("()J")
    split = JavaMultipleMethod([("()Ljava/util/random/RandomGenerator$SplittableGenerator;", False, False), ("(Ljava/util/random/RandomGenerator$SplittableGenerator;)Ljava/util/SplittableRandom;", False, False), ("()Ljava/util/SplittableRandom;", False, False), ("(Ljava/util/random/RandomGenerator$SplittableGenerator;)Ljava/util/random/RandomGenerator$SplittableGenerator;", False, False)])
    splits = JavaMultipleMethod([("(Ljava/util/random/RandomGenerator$SplittableGenerator;)Ljava/util/stream/Stream;", False, False), ("(J)Ljava/util/stream/Stream;", False, False), ("()Ljava/util/stream/Stream;", False, False), ("(JLjava/util/random/RandomGenerator$SplittableGenerator;)Ljava/util/stream/Stream;", False, False)])
    ints = JavaMultipleMethod([("(JII)Ljava/util/stream/IntStream;", False, False), ("(II)Ljava/util/stream/IntStream;", False, False), ("()Ljava/util/stream/IntStream;", False, False), ("(J)Ljava/util/stream/IntStream;", False, False)])
    doubles = JavaMultipleMethod([("(JDD)Ljava/util/stream/DoubleStream;", False, False), ("()Ljava/util/stream/DoubleStream;", False, False), ("(J)Ljava/util/stream/DoubleStream;", False, False), ("(DD)Ljava/util/stream/DoubleStream;", False, False)])
    nextInt = JavaMethod("()I")
    nextBytes = JavaMethod("([B)V")
    longs = JavaMultipleMethod([("(J)Ljava/util/stream/LongStream;", False, False), ("(JJ)Ljava/util/stream/LongStream;", False, False), ("()Ljava/util/stream/LongStream;", False, False), ("(JJJ)Ljava/util/stream/LongStream;", False, False)])