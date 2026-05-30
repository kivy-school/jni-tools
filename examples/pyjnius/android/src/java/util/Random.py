from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class RandomGenerator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/random/RandomGenerator"
    nextBoolean = JavaMethod("()Z")
    nextLong = JavaMultipleMethod([("()J", False, False), ("(J)J", False, False), ("(JJ)J", False, False)])
    nextDouble = JavaMultipleMethod([("()D", False, False), ("(DD)D", False, False), ("(D)D", False, False)])
    getDefault = JavaStaticMethod("()Ljava/util/random/RandomGenerator;")
    of = JavaStaticMethod("(Ljava/lang/String;)Ljava/util/random/RandomGenerator;")
    nextInt = JavaMultipleMethod([("()I", False, False), ("(I)I", False, False), ("(II)I", False, False)])
    nextBytes = JavaMethod("([B)V")
    longs = JavaMultipleMethod([("(JJJ)Ljava/util/stream/LongStream;", False, False), ("()Ljava/util/stream/LongStream;", False, False), ("(JJ)Ljava/util/stream/LongStream;", False, False), ("(J)Ljava/util/stream/LongStream;", False, False)])
    nextFloat = JavaMultipleMethod([("(FF)F", False, False), ("(F)F", False, False), ("()F", False, False)])
    ints = JavaMultipleMethod([("()Ljava/util/stream/IntStream;", False, False), ("(II)Ljava/util/stream/IntStream;", False, False), ("(J)Ljava/util/stream/IntStream;", False, False), ("(JII)Ljava/util/stream/IntStream;", False, False)])
    doubles = JavaMultipleMethod([("(DD)Ljava/util/stream/DoubleStream;", False, False), ("()Ljava/util/stream/DoubleStream;", False, False), ("(J)Ljava/util/stream/DoubleStream;", False, False), ("(JDD)Ljava/util/stream/DoubleStream;", False, False)])
    nextGaussian = JavaMultipleMethod([("()D", False, False), ("(DD)D", False, False)])
    isDeprecated = JavaMethod("()Z")
    nextExponential = JavaMethod("()D")

    class ArbitrarilyJumpableGenerator(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/random/RandomGenerator$ArbitrarilyJumpableGenerator"
        of = JavaStaticMethod("(Ljava/lang/String;)Ljava/util/random/RandomGenerator$ArbitrarilyJumpableGenerator;")
        copy = JavaMultipleMethod([("()Ljava/util/random/RandomGenerator$LeapableGenerator;", False, False), ("()Ljava/util/random/RandomGenerator$JumpableGenerator;", False, False), ("()Ljava/util/random/RandomGenerator$ArbitrarilyJumpableGenerator;", False, False)])
        leap = JavaMethod("()V")
        jump = JavaMultipleMethod([("()V", False, False), ("(D)V", False, False)])
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
        rngs = JavaMultipleMethod([("()Ljava/util/stream/Stream;", False, False), ("(J)Ljava/util/stream/Stream;", False, False)])
        of = JavaStaticMethod("(Ljava/lang/String;)Ljava/util/random/RandomGenerator$JumpableGenerator;")
        copy = JavaMethod("()Ljava/util/random/RandomGenerator$JumpableGenerator;")
        jump = JavaMethod("()V")
        jumpDistance = JavaMethod("()D")
        jumps = JavaMultipleMethod([("(J)Ljava/util/stream/Stream;", False, False), ("()Ljava/util/stream/Stream;", False, False)])
        copyAndJump = JavaMethod("()Ljava/util/random/RandomGenerator;")

    class SplittableGenerator(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/random/RandomGenerator$SplittableGenerator"
        splits = JavaMultipleMethod([("(JLjava/util/random/RandomGenerator$SplittableGenerator;)Ljava/util/stream/Stream;", False, False), ("(J)Ljava/util/stream/Stream;", False, False), ("()Ljava/util/stream/Stream;", False, False), ("(Ljava/util/random/RandomGenerator$SplittableGenerator;)Ljava/util/stream/Stream;", False, False)])
        rngs = JavaMultipleMethod([("(J)Ljava/util/stream/Stream;", False, False), ("()Ljava/util/stream/Stream;", False, False)])
        split = JavaMultipleMethod([("()Ljava/util/random/RandomGenerator$SplittableGenerator;", False, False), ("(Ljava/util/random/RandomGenerator$SplittableGenerator;)Ljava/util/random/RandomGenerator$SplittableGenerator;", False, False)])
        of = JavaStaticMethod("(Ljava/lang/String;)Ljava/util/random/RandomGenerator$SplittableGenerator;")

    class StreamableGenerator(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/random/RandomGenerator$StreamableGenerator"
        rngs = JavaMultipleMethod([("()Ljava/util/stream/Stream;", False, False), ("(J)Ljava/util/stream/Stream;", False, False)])
        of = JavaStaticMethod("(Ljava/lang/String;)Ljava/util/random/RandomGenerator$StreamableGenerator;")

class RandomGeneratorFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/random/RandomGeneratorFactory"
    create = JavaMultipleMethod([("(J)Ljava/util/random/RandomGenerator;", False, False), ("()Ljava/util/random/RandomGenerator;", False, False), ("([B)Ljava/util/random/RandomGenerator;", False, False)])
    name = JavaMethod("()Ljava/lang/String;")
    group = JavaMethod("()Ljava/lang/String;")
    getDefault = JavaStaticMethod("()Ljava/util/random/RandomGeneratorFactory;")
    of = JavaStaticMethod("(Ljava/lang/String;)Ljava/util/random/RandomGeneratorFactory;")
    period = JavaMethod("()Ljava/math/BigInteger;")
    all = JavaStaticMethod("()Ljava/util/stream/Stream;")
    isStochastic = JavaMethod("()Z")
    isHardware = JavaMethod("()Z")
    stateBits = JavaMethod("()I")
    isStatistical = JavaMethod("()Z")
    isArbitrarilyJumpable = JavaMethod("()Z")
    isJumpable = JavaMethod("()Z")
    isLeapable = JavaMethod("()Z")
    isSplittable = JavaMethod("()Z")
    isStreamable = JavaMethod("()Z")
    equidistribution = JavaMethod("()I")
    isDeprecated = JavaMethod("()Z")