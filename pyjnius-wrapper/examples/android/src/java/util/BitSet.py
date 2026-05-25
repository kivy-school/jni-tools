from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BitSet"]

class BitSet(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/BitSet"
    __javaconstructor__ = [("()V", False), ("(I)V", False)]
    valueOf = JavaMultipleMethod([("([J)Ljava/util/BitSet;", True, False), ("(Ljava/nio/LongBuffer;)Ljava/util/BitSet;", True, False), ("([B)Ljava/util/BitSet;", True, False), ("(Ljava/nio/ByteBuffer;)Ljava/util/BitSet;", True, False)])
    toByteArray = JavaMethod("()[B")
    toLongArray = JavaMethod("()[J")
    flip = JavaMultipleMethod([("(I)V", False, False), ("(II)V", False, False)])
    set = JavaMultipleMethod([("(I)V", False, False), ("(IZ)V", False, False), ("(II)V", False, False), ("(IIZ)V", False, False)])
    clear = JavaMultipleMethod([("(I)V", False, False), ("(II)V", False, False), ("()V", False, False)])
    get = JavaMultipleMethod([("(I)Z", False, False), ("(II)Ljava/util/BitSet;", False, False)])
    nextSetBit = JavaMethod("(I)I")
    nextClearBit = JavaMethod("(I)I")
    previousSetBit = JavaMethod("(I)I")
    previousClearBit = JavaMethod("(I)I")
    length = JavaMethod("()I")
    isEmpty = JavaMethod("()Z")
    intersects = JavaMethod("(Ljava/util/BitSet;)Z")
    cardinality = JavaMethod("()I")
    and = JavaMethod("(Ljava/util/BitSet;)V")
    or = JavaMethod("(Ljava/util/BitSet;)V")
    xor = JavaMethod("(Ljava/util/BitSet;)V")
    andNot = JavaMethod("(Ljava/util/BitSet;)V")
    hashCode = JavaMethod("()I")
    size = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    clone = JavaMethod("()Ljava/lang/Object;")
    toString = JavaMethod("()Ljava/lang/String;")
    stream = JavaMethod("()Ljava/util/stream/IntStream;")