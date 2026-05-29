from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RandomGenerator"]

class RandomGenerator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/random/RandomGenerator"
    nextLong = JavaMultipleMethod([("(J)J", False, False), ("()J", False, False), ("(JJ)J", False, False)])
    nextBoolean = JavaMethod("()Z")
    of = JavaStaticMethod("(Ljava/lang/String;)Ljava/util/random/RandomGenerator;")
    getDefault = JavaStaticMethod("()Ljava/util/random/RandomGenerator;")
    nextDouble = JavaMultipleMethod([("(D)D", False, False), ("()D", False, False), ("(DD)D", False, False)])
    nextFloat = JavaMultipleMethod([("(FF)F", False, False), ("()F", False, False), ("(F)F", False, False)])
    ints = JavaMultipleMethod([("(II)Ljava/util/stream/IntStream;", False, False), ("(J)Ljava/util/stream/IntStream;", False, False), ("(JII)Ljava/util/stream/IntStream;", False, False), ("()Ljava/util/stream/IntStream;", False, False)])
    doubles = JavaMultipleMethod([("(JDD)Ljava/util/stream/DoubleStream;", False, False), ("(DD)Ljava/util/stream/DoubleStream;", False, False), ("()Ljava/util/stream/DoubleStream;", False, False), ("(J)Ljava/util/stream/DoubleStream;", False, False)])
    nextGaussian = JavaMultipleMethod([("(DD)D", False, False), ("()D", False, False)])
    isDeprecated = JavaMethod("()Z")
    equiDoubles = JavaMethod("(DDZZ)Ljava/util/stream/DoubleStream;")
    nextExponential = JavaMethod("()D")
    nextInt = JavaMultipleMethod([("()I", False, False), ("(I)I", False, False), ("(II)I", False, False)])
    nextBytes = JavaMethod("([B)V")
    longs = JavaMultipleMethod([("()Ljava/util/stream/LongStream;", False, False), ("(JJ)Ljava/util/stream/LongStream;", False, False), ("(J)Ljava/util/stream/LongStream;", False, False), ("(JJJ)Ljava/util/stream/LongStream;", False, False)])

    class ArbitrarilyJumpableGenerator(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/random/RandomGenerator$ArbitrarilyJumpableGenerator"
        of = JavaStaticMethod("(Ljava/lang/String;)Ljava/util/random/RandomGenerator$ArbitrarilyJumpableGenerator;")
        copy = JavaMultipleMethod([("()Ljava/util/random/RandomGenerator$LeapableGenerator;", False, False), ("()Ljava/util/random/RandomGenerator$JumpableGenerator;", False, False), ("()Ljava/util/random/RandomGenerator$ArbitrarilyJumpableGenerator;", False, False)])
        jump = JavaMultipleMethod([("()V", False, False), ("(D)V", False, False)])
        leap = JavaMethod("()V")
        jumps = JavaMultipleMethod([("(D)Ljava/util/stream/Stream;", False, False), ("(JD)Ljava/util/stream/Stream;", False, False)])
        copyAndJump = JavaMethod("(D)Ljava/util/random/RandomGenerator$ArbitrarilyJumpableGenerator;")
        jumpPowerOfTwo = JavaMethod("(I)V")

    class LeapableGenerator(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/random/RandomGenerator$LeapableGenerator"
        of = JavaStaticMethod("(Ljava/lang/String;)Ljava/util/random/RandomGenerator$LeapableGenerator;")
        copy = JavaMultipleMethod([("()Ljava/util/random/RandomGenerator$JumpableGenerator;", False, False), ("()Ljava/util/random/RandomGenerator$LeapableGenerator;", False, False)])
        leap = JavaMethod("()V")
        leapDistance = JavaMethod("()D")
        leaps = JavaMultipleMethod([("()Ljava/util/stream/Stream;", False, False), ("(J)Ljava/util/stream/Stream;", False, False)])
        copyAndLeap = JavaMethod("()Ljava/util/random/RandomGenerator$JumpableGenerator;")

    class JumpableGenerator(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/random/RandomGenerator$JumpableGenerator"
        of = JavaStaticMethod("(Ljava/lang/String;)Ljava/util/random/RandomGenerator$JumpableGenerator;")
        copy = JavaMethod("()Ljava/util/random/RandomGenerator$JumpableGenerator;")
        rngs = JavaMultipleMethod([("()Ljava/util/stream/Stream;", False, False), ("(J)Ljava/util/stream/Stream;", False, False)])
        jump = JavaMethod("()V")
        jumpDistance = JavaMethod("()D")
        jumps = JavaMultipleMethod([("(J)Ljava/util/stream/Stream;", False, False), ("()Ljava/util/stream/Stream;", False, False)])
        copyAndJump = JavaMethod("()Ljava/util/random/RandomGenerator;")

    class SplittableGenerator(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/random/RandomGenerator$SplittableGenerator"
        of = JavaStaticMethod("(Ljava/lang/String;)Ljava/util/random/RandomGenerator$SplittableGenerator;")
        split = JavaMultipleMethod([("(Ljava/util/random/RandomGenerator$SplittableGenerator;)Ljava/util/random/RandomGenerator$SplittableGenerator;", False, False), ("()Ljava/util/random/RandomGenerator$SplittableGenerator;", False, False)])
        splits = JavaMultipleMethod([("(JLjava/util/random/RandomGenerator$SplittableGenerator;)Ljava/util/stream/Stream;", False, False), ("(Ljava/util/random/RandomGenerator$SplittableGenerator;)Ljava/util/stream/Stream;", False, False), ("(J)Ljava/util/stream/Stream;", False, False), ("()Ljava/util/stream/Stream;", False, False)])
        rngs = JavaMultipleMethod([("(J)Ljava/util/stream/Stream;", False, False), ("()Ljava/util/stream/Stream;", False, False)])

    class StreamableGenerator(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/random/RandomGenerator$StreamableGenerator"
        of = JavaStaticMethod("(Ljava/lang/String;)Ljava/util/random/RandomGenerator$StreamableGenerator;")
        rngs = JavaMultipleMethod([("()Ljava/util/stream/Stream;", False, False), ("(J)Ljava/util/stream/Stream;", False, False)])