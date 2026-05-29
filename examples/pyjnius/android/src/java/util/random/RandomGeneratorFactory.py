from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RandomGeneratorFactory"]

class RandomGeneratorFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/random/RandomGeneratorFactory"
    of = JavaStaticMethod("(Ljava/lang/String;)Ljava/util/random/RandomGeneratorFactory;")
    getDefault = JavaStaticMethod("()Ljava/util/random/RandomGeneratorFactory;")
    all = JavaStaticMethod("()Ljava/util/stream/Stream;")
    name = JavaMethod("()Ljava/lang/String;")
    group = JavaMethod("()Ljava/lang/String;")
    stateBits = JavaMethod("()I")
    equidistribution = JavaMethod("()I")
    period = JavaMethod("()Ljava/math/BigInteger;")
    isStatistical = JavaMethod("()Z")
    isStochastic = JavaMethod("()Z")
    isHardware = JavaMethod("()Z")
    isArbitrarilyJumpable = JavaMethod("()Z")
    isJumpable = JavaMethod("()Z")
    isLeapable = JavaMethod("()Z")
    isSplittable = JavaMethod("()Z")
    isStreamable = JavaMethod("()Z")
    isDeprecated = JavaMethod("()Z")
    create = JavaMultipleMethod([("()Ljava/util/random/RandomGenerator;", False, False), ("(J)Ljava/util/random/RandomGenerator;", False, False), ("([B)Ljava/util/random/RandomGenerator;", False, False)])