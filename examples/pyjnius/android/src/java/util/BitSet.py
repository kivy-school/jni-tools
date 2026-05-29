from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BitSet"]

class BitSet(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/BitSet"
    __javaconstructor__ = [("(I)V", False), ("()V", False)]
    size = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    length = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    clone = JavaMethod("()Ljava/lang/Object;")
    valueOf = JavaMultipleMethod([("(Ljava/nio/ByteBuffer;)Ljava/util/BitSet;", True, False), ("([J)Ljava/util/BitSet;", True, False), ("(Ljava/nio/LongBuffer;)Ljava/util/BitSet;", True, False), ("([B)Ljava/util/BitSet;", True, False)])
    clear = JavaMultipleMethod([("()V", False, False), ("(II)V", False, False), ("(I)V", False, False)])
    isEmpty = JavaMethod("()Z")
    get = JavaMultipleMethod([("(II)Ljava/util/BitSet;", False, False), ("(I)Z", False, False)])
    stream = JavaMethod("()Ljava/util/stream/IntStream;")
    set = JavaMultipleMethod([("(II)V", False, False), ("(I)V", False, False), ("(IIZ)V", False, False), ("(IZ)V", False, False)])
    nextClearBit = JavaMethod("(I)I")
    toByteArray = JavaMethod("()[B")
    previousSetBit = JavaMethod("(I)I")
    cardinality = JavaMethod("()I")
    nextSetBit = JavaMethod("(I)I")
    toLongArray = JavaMethod("()[J")
    previousClearBit = JavaMethod("(I)I")
    intersects = JavaMethod("(Ljava/util/BitSet;)Z")
    and = JavaMethod("(Ljava/util/BitSet;)V")
    xor = JavaMethod("(Ljava/util/BitSet;)V")
    andNot = JavaMethod("(Ljava/util/BitSet;)V")
    flip = JavaMultipleMethod([("(II)V", False, False), ("(I)V", False, False)])
    or = JavaMethod("(Ljava/util/BitSet;)V")