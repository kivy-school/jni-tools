from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SplittableRandom"]

class SplittableRandom(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/SplittableRandom"
    __javaconstructor__ = [("(J)V", False), ("()V", False)]
    split = JavaMultipleMethod([("()Ljava/util/SplittableRandom;", False, False), ("(Ljava/util/random/RandomGenerator$SplittableGenerator;)Ljava/util/SplittableRandom;", False, False)])
    nextInt = JavaMethod("()I")
    nextLong = JavaMethod("()J")
    nextBytes = JavaMethod("([B)V")
    splits = JavaMultipleMethod([("()Ljava/util/stream/Stream;", False, False), ("(J)Ljava/util/stream/Stream;", False, False), ("(Ljava/util/random/RandomGenerator$SplittableGenerator;)Ljava/util/stream/Stream;", False, False), ("(JLjava/util/random/RandomGenerator$SplittableGenerator;)Ljava/util/stream/Stream;", False, False)])
    ints = JavaMultipleMethod([("(J)Ljava/util/stream/IntStream;", False, False), ("()Ljava/util/stream/IntStream;", False, False), ("(JII)Ljava/util/stream/IntStream;", False, False), ("(II)Ljava/util/stream/IntStream;", False, False)])
    longs = JavaMultipleMethod([("(J)Ljava/util/stream/LongStream;", False, False), ("()Ljava/util/stream/LongStream;", False, False), ("(JJJ)Ljava/util/stream/LongStream;", False, False), ("(JJ)Ljava/util/stream/LongStream;", False, False)])
    doubles = JavaMultipleMethod([("(J)Ljava/util/stream/DoubleStream;", False, False), ("()Ljava/util/stream/DoubleStream;", False, False), ("(JDD)Ljava/util/stream/DoubleStream;", False, False), ("(DD)Ljava/util/stream/DoubleStream;", False, False)])