from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RandomGeneratorFactory"]

class RandomGeneratorFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/random/RandomGeneratorFactory"
    name = JavaMethod("()Ljava/lang/String;")
    group = JavaMethod("()Ljava/lang/String;")
    of = JavaStaticMethod("(Ljava/lang/String;)Ljava/util/random/RandomGeneratorFactory;")
    getDefault = JavaStaticMethod("()Ljava/util/random/RandomGeneratorFactory;")
    create = JavaMultipleMethod([("()Ljava/util/random/RandomGenerator;", False, False), ("([B)Ljava/util/random/RandomGenerator;", False, False), ("(J)Ljava/util/random/RandomGenerator;", False, False)])
    period = JavaMethod("()Ljava/math/BigInteger;")
    isDeprecated = JavaMethod("()Z")
    all = JavaStaticMethod("()Ljava/util/stream/Stream;")
    stateBits = JavaMethod("()I")
    equidistribution = JavaMethod("()I")
    isStochastic = JavaMethod("()Z")
    isHardware = JavaMethod("()Z")
    isStatistical = JavaMethod("()Z")
    isArbitrarilyJumpable = JavaMethod("()Z")
    isJumpable = JavaMethod("()Z")
    isLeapable = JavaMethod("()Z")
    isSplittable = JavaMethod("()Z")
    isStreamable = JavaMethod("()Z")