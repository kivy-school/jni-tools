from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RandomGenerator"]

class RandomGenerator(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/random/RandomGenerator"
    of = JavaStaticMethod("(Ljava/lang/String;)Ljava/util/random/RandomGenerator;")
    getDefault = JavaStaticMethod("()Ljava/util/random/RandomGenerator;")
    isDeprecated = JavaMethod("()Z")
    doubles = JavaMultipleMethod([("()Ljava/util/stream/DoubleStream;", False, False), ("(DD)Ljava/util/stream/DoubleStream;", False, False), ("(J)Ljava/util/stream/DoubleStream;", False, False), ("(JDD)Ljava/util/stream/DoubleStream;", False, False)])
    ints = JavaMultipleMethod([("()Ljava/util/stream/IntStream;", False, False), ("(II)Ljava/util/stream/IntStream;", False, False), ("(J)Ljava/util/stream/IntStream;", False, False), ("(JII)Ljava/util/stream/IntStream;", False, False)])
    longs = JavaMultipleMethod([("()Ljava/util/stream/LongStream;", False, False), ("(JJ)Ljava/util/stream/LongStream;", False, False), ("(J)Ljava/util/stream/LongStream;", False, False), ("(JJJ)Ljava/util/stream/LongStream;", False, False)])
    nextBoolean = JavaMethod("()Z")
    nextBytes = JavaMethod("([B)V")
    nextFloat = JavaMultipleMethod([("()F", False, False), ("(F)F", False, False), ("(FF)F", False, False)])
    nextDouble = JavaMultipleMethod([("()D", False, False), ("(D)D", False, False), ("(DD)D", False, False)])
    nextInt = JavaMultipleMethod([("()I", False, False), ("(I)I", False, False), ("(II)I", False, False)])
    nextLong = JavaMultipleMethod([("()J", False, False), ("(J)J", False, False), ("(JJ)J", False, False)])
    nextGaussian = JavaMultipleMethod([("()D", False, False), ("(DD)D", False, False)])
    nextExponential = JavaMethod("()D")

    class ArbitrarilyJumpableGenerator(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/random/RandomGenerator/ArbitrarilyJumpableGenerator"
        of = JavaStaticMethod("(Ljava/lang/String;)Ljava/util/random/RandomGenerator$ArbitrarilyJumpableGenerator;")
        copy = JavaMethod("()Ljava/util/random/RandomGenerator$ArbitrarilyJumpableGenerator;")
        jumpPowerOfTwo = JavaMethod("(I)V")
        jump = JavaMultipleMethod([("(D)V", False, False), ("()V", False, False)])
        jumps = JavaMultipleMethod([("(D)Ljava/util/stream/Stream;", False, False), ("(JD)Ljava/util/stream/Stream;", False, False)])
        leap = JavaMethod("()V")
        copyAndJump = JavaMethod("(D)Ljava/util/random/RandomGenerator$ArbitrarilyJumpableGenerator;")

    class JumpableGenerator(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/random/RandomGenerator/JumpableGenerator"
        of = JavaStaticMethod("(Ljava/lang/String;)Ljava/util/random/RandomGenerator$JumpableGenerator;")
        copy = JavaMethod("()Ljava/util/random/RandomGenerator$JumpableGenerator;")
        jump = JavaMethod("()V")
        jumpDistance = JavaMethod("()D")
        jumps = JavaMultipleMethod([("()Ljava/util/stream/Stream;", False, False), ("(J)Ljava/util/stream/Stream;", False, False)])
        rngs = JavaMultipleMethod([("()Ljava/util/stream/Stream;", False, False), ("(J)Ljava/util/stream/Stream;", False, False)])
        copyAndJump = JavaMethod("()Ljava/util/random/RandomGenerator;")

    class LeapableGenerator(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/random/RandomGenerator/LeapableGenerator"
        of = JavaStaticMethod("(Ljava/lang/String;)Ljava/util/random/RandomGenerator$LeapableGenerator;")
        copy = JavaMethod("()Ljava/util/random/RandomGenerator$LeapableGenerator;")
        leap = JavaMethod("()V")
        leapDistance = JavaMethod("()D")
        leaps = JavaMultipleMethod([("()Ljava/util/stream/Stream;", False, False), ("(J)Ljava/util/stream/Stream;", False, False)])
        copyAndLeap = JavaMethod("()Ljava/util/random/RandomGenerator$JumpableGenerator;")

    class SplittableGenerator(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/random/RandomGenerator/SplittableGenerator"
        of = JavaStaticMethod("(Ljava/lang/String;)Ljava/util/random/RandomGenerator$SplittableGenerator;")
        split = JavaMultipleMethod([("()Ljava/util/random/RandomGenerator$SplittableGenerator;", False, False), ("(Ljava/util/random/RandomGenerator$SplittableGenerator;)Ljava/util/random/RandomGenerator$SplittableGenerator;", False, False)])
        splits = JavaMultipleMethod([("()Ljava/util/stream/Stream;", False, False), ("(J)Ljava/util/stream/Stream;", False, False), ("(Ljava/util/random/RandomGenerator$SplittableGenerator;)Ljava/util/stream/Stream;", False, False), ("(JLjava/util/random/RandomGenerator$SplittableGenerator;)Ljava/util/stream/Stream;", False, False)])
        rngs = JavaMultipleMethod([("()Ljava/util/stream/Stream;", False, False), ("(J)Ljava/util/stream/Stream;", False, False)])

    class StreamableGenerator(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/random/RandomGenerator/StreamableGenerator"
        of = JavaStaticMethod("(Ljava/lang/String;)Ljava/util/random/RandomGenerator$StreamableGenerator;")
        rngs = JavaMultipleMethod([("()Ljava/util/stream/Stream;", False, False), ("(J)Ljava/util/stream/Stream;", False, False)])