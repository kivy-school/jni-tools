from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DoubleBuffer"]

class DoubleBuffer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/DoubleBuffer"
    allocate = JavaStaticMethod("(I)Ljava/nio/DoubleBuffer;")
    wrap = JavaMultipleMethod([("([DII)Ljava/nio/DoubleBuffer;", True, False), ("([D)Ljava/nio/DoubleBuffer;", True, False)])
    slice = JavaMultipleMethod([("()Ljava/nio/DoubleBuffer;", False, False), ("(II)Ljava/nio/DoubleBuffer;", False, False)])
    duplicate = JavaMethod("()Ljava/nio/DoubleBuffer;")
    asReadOnlyBuffer = JavaMethod("()Ljava/nio/DoubleBuffer;")
    get = JavaMultipleMethod([("()D", False, False), ("(I)D", False, False), ("([DII)Ljava/nio/DoubleBuffer;", False, False), ("([D)Ljava/nio/DoubleBuffer;", False, False), ("(I[DII)Ljava/nio/DoubleBuffer;", False, False), ("(I[D)Ljava/nio/DoubleBuffer;", False, False)])
    put = JavaMultipleMethod([("(D)Ljava/nio/DoubleBuffer;", False, False), ("(ID)Ljava/nio/DoubleBuffer;", False, False), ("(Ljava/nio/DoubleBuffer;)Ljava/nio/DoubleBuffer;", False, False), ("(ILjava/nio/DoubleBuffer;II)Ljava/nio/DoubleBuffer;", False, False), ("([DII)Ljava/nio/DoubleBuffer;", False, False), ("([D)Ljava/nio/DoubleBuffer;", False, False), ("(I[DII)Ljava/nio/DoubleBuffer;", False, False), ("(I[D)Ljava/nio/DoubleBuffer;", False, False)])
    hasArray = JavaMethod("()Z")
    array = JavaMethod("()[D")
    arrayOffset = JavaMethod("()I")
    position = JavaMethod("(I)Ljava/nio/Buffer;")
    limit = JavaMethod("(I)Ljava/nio/Buffer;")
    mark = JavaMethod("()Ljava/nio/Buffer;")
    reset = JavaMethod("()Ljava/nio/Buffer;")
    clear = JavaMethod("()Ljava/nio/Buffer;")
    flip = JavaMethod("()Ljava/nio/Buffer;")
    rewind = JavaMethod("()Ljava/nio/Buffer;")
    compact = JavaMethod("()Ljava/nio/DoubleBuffer;")
    isDirect = JavaMethod("()Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    compareTo = JavaMethod("(Ljava/nio/DoubleBuffer;)I")
    mismatch = JavaMethod("(Ljava/nio/DoubleBuffer;)I")
    order = JavaMethod("()Ljava/nio/ByteOrder;")