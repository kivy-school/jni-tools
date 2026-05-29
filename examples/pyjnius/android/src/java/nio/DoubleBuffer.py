from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DoubleBuffer"]

class DoubleBuffer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/DoubleBuffer"
    reset = JavaMultipleMethod([("()Ljava/nio/Buffer;", False, False), ("()Ljava/nio/DoubleBuffer;", False, False)])
    put = JavaMultipleMethod([("(Ljava/nio/DoubleBuffer;)Ljava/nio/DoubleBuffer;", False, False), ("(ILjava/nio/DoubleBuffer;II)Ljava/nio/DoubleBuffer;", False, False), ("(D)Ljava/nio/DoubleBuffer;", False, False), ("(ID)Ljava/nio/DoubleBuffer;", False, False), ("(I[D)Ljava/nio/DoubleBuffer;", False, False), ("(I[DII)Ljava/nio/DoubleBuffer;", False, False), ("([D)Ljava/nio/DoubleBuffer;", False, False), ("([DII)Ljava/nio/DoubleBuffer;", False, False)])
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    compareTo = JavaMultipleMethod([("(Ljava/lang/Object;)I", False, False), ("(Ljava/nio/DoubleBuffer;)I", False, False)])
    clear = JavaMultipleMethod([("()Ljava/nio/DoubleBuffer;", False, False), ("()Ljava/nio/Buffer;", False, False)])
    wrap = JavaMultipleMethod([("([D)Ljava/nio/DoubleBuffer;", True, False), ("([DII)Ljava/nio/DoubleBuffer;", True, False)])
    position = JavaMultipleMethod([("(I)Ljava/nio/Buffer;", False, False), ("(I)Ljava/nio/DoubleBuffer;", False, False)])
    mismatch = JavaMethod("(Ljava/nio/DoubleBuffer;)I")
    get = JavaMultipleMethod([("(I[D)Ljava/nio/DoubleBuffer;", False, False), ("(I[DII)Ljava/nio/DoubleBuffer;", False, False), ("([D)Ljava/nio/DoubleBuffer;", False, False), ("([DII)Ljava/nio/DoubleBuffer;", False, False), ("(I)D", False, False), ("()D", False, False)])
    limit = JavaMultipleMethod([("(I)Ljava/nio/Buffer;", False, False), ("(I)Ljava/nio/DoubleBuffer;", False, False)])
    isDirect = JavaMethod("()Z")
    hasArray = JavaMethod("()Z")
    array = JavaMultipleMethod([("()[D", False, False), ("()Ljava/lang/Object;", False, False)])
    arrayOffset = JavaMethod("()I")
    allocate = JavaStaticMethod("(I)Ljava/nio/DoubleBuffer;")
    mark = JavaMultipleMethod([("()Ljava/nio/Buffer;", False, False), ("()Ljava/nio/DoubleBuffer;", False, False)])
    asReadOnlyBuffer = JavaMethod("()Ljava/nio/DoubleBuffer;")
    compact = JavaMethod("()Ljava/nio/DoubleBuffer;")
    order = JavaMethod("()Ljava/nio/ByteOrder;")
    flip = JavaMultipleMethod([("()Ljava/nio/DoubleBuffer;", False, False), ("()Ljava/nio/Buffer;", False, False)])
    rewind = JavaMultipleMethod([("()Ljava/nio/DoubleBuffer;", False, False), ("()Ljava/nio/Buffer;", False, False)])
    slice = JavaMultipleMethod([("(II)Ljava/nio/Buffer;", False, False), ("()Ljava/nio/Buffer;", False, False), ("(II)Ljava/nio/DoubleBuffer;", False, False), ("()Ljava/nio/DoubleBuffer;", False, False)])
    duplicate = JavaMultipleMethod([("()Ljava/nio/DoubleBuffer;", False, False), ("()Ljava/nio/Buffer;", False, False)])