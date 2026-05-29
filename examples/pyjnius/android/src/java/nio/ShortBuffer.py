from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ShortBuffer"]

class ShortBuffer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/ShortBuffer"
    reset = JavaMultipleMethod([("()Ljava/nio/Buffer;", False, False), ("()Ljava/nio/ShortBuffer;", False, False)])
    put = JavaMultipleMethod([("(Ljava/nio/ShortBuffer;)Ljava/nio/ShortBuffer;", False, False), ("(ILjava/nio/ShortBuffer;II)Ljava/nio/ShortBuffer;", False, False), ("(S)Ljava/nio/ShortBuffer;", False, False), ("(IS)Ljava/nio/ShortBuffer;", False, False), ("(I[S)Ljava/nio/ShortBuffer;", False, False), ("(I[SII)Ljava/nio/ShortBuffer;", False, False), ("([S)Ljava/nio/ShortBuffer;", False, False), ("([SII)Ljava/nio/ShortBuffer;", False, False)])
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    compareTo = JavaMultipleMethod([("(Ljava/lang/Object;)I", False, False), ("(Ljava/nio/ShortBuffer;)I", False, False)])
    clear = JavaMultipleMethod([("()Ljava/nio/ShortBuffer;", False, False), ("()Ljava/nio/Buffer;", False, False)])
    wrap = JavaMultipleMethod([("([S)Ljava/nio/ShortBuffer;", True, False), ("([SII)Ljava/nio/ShortBuffer;", True, False)])
    position = JavaMultipleMethod([("(I)Ljava/nio/Buffer;", False, False), ("(I)Ljava/nio/ShortBuffer;", False, False)])
    mismatch = JavaMethod("(Ljava/nio/ShortBuffer;)I")
    get = JavaMultipleMethod([("(I[S)Ljava/nio/ShortBuffer;", False, False), ("(I[SII)Ljava/nio/ShortBuffer;", False, False), ("([S)Ljava/nio/ShortBuffer;", False, False), ("([SII)Ljava/nio/ShortBuffer;", False, False), ("(I)S", False, False), ("()S", False, False)])
    limit = JavaMultipleMethod([("(I)Ljava/nio/Buffer;", False, False), ("(I)Ljava/nio/ShortBuffer;", False, False)])
    isDirect = JavaMethod("()Z")
    hasArray = JavaMethod("()Z")
    array = JavaMultipleMethod([("()[S", False, False), ("()Ljava/lang/Object;", False, False)])
    arrayOffset = JavaMethod("()I")
    allocate = JavaStaticMethod("(I)Ljava/nio/ShortBuffer;")
    mark = JavaMultipleMethod([("()Ljava/nio/Buffer;", False, False), ("()Ljava/nio/ShortBuffer;", False, False)])
    asReadOnlyBuffer = JavaMethod("()Ljava/nio/ShortBuffer;")
    compact = JavaMethod("()Ljava/nio/ShortBuffer;")
    order = JavaMethod("()Ljava/nio/ByteOrder;")
    flip = JavaMultipleMethod([("()Ljava/nio/ShortBuffer;", False, False), ("()Ljava/nio/Buffer;", False, False)])
    rewind = JavaMultipleMethod([("()Ljava/nio/ShortBuffer;", False, False), ("()Ljava/nio/Buffer;", False, False)])
    slice = JavaMultipleMethod([("(II)Ljava/nio/Buffer;", False, False), ("()Ljava/nio/Buffer;", False, False), ("(II)Ljava/nio/ShortBuffer;", False, False), ("()Ljava/nio/ShortBuffer;", False, False)])
    duplicate = JavaMultipleMethod([("()Ljava/nio/ShortBuffer;", False, False), ("()Ljava/nio/Buffer;", False, False)])