from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ShortBuffer"]

class ShortBuffer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/ShortBuffer"
    allocate = JavaStaticMethod("(I)Ljava/nio/ShortBuffer;")
    wrap = JavaMultipleMethod([("([SII)Ljava/nio/ShortBuffer;", True, False), ("([S)Ljava/nio/ShortBuffer;", True, False)])
    slice = JavaMultipleMethod([("()Ljava/nio/ShortBuffer;", False, False), ("(II)Ljava/nio/ShortBuffer;", False, False)])
    duplicate = JavaMethod("()Ljava/nio/ShortBuffer;")
    asReadOnlyBuffer = JavaMethod("()Ljava/nio/ShortBuffer;")
    get = JavaMultipleMethod([("()S", False, False), ("(I)S", False, False), ("([SII)Ljava/nio/ShortBuffer;", False, False), ("([S)Ljava/nio/ShortBuffer;", False, False), ("(I[SII)Ljava/nio/ShortBuffer;", False, False), ("(I[S)Ljava/nio/ShortBuffer;", False, False)])
    put = JavaMultipleMethod([("(S)Ljava/nio/ShortBuffer;", False, False), ("(IS)Ljava/nio/ShortBuffer;", False, False), ("(Ljava/nio/ShortBuffer;)Ljava/nio/ShortBuffer;", False, False), ("(ILjava/nio/ShortBuffer;II)Ljava/nio/ShortBuffer;", False, False), ("([SII)Ljava/nio/ShortBuffer;", False, False), ("([S)Ljava/nio/ShortBuffer;", False, False), ("(I[SII)Ljava/nio/ShortBuffer;", False, False), ("(I[S)Ljava/nio/ShortBuffer;", False, False)])
    hasArray = JavaMethod("()Z")
    array = JavaMethod("()[S")
    arrayOffset = JavaMethod("()I")
    position = JavaMethod("(I)Ljava/nio/Buffer;")
    limit = JavaMethod("(I)Ljava/nio/Buffer;")
    mark = JavaMethod("()Ljava/nio/Buffer;")
    reset = JavaMethod("()Ljava/nio/Buffer;")
    clear = JavaMethod("()Ljava/nio/Buffer;")
    flip = JavaMethod("()Ljava/nio/Buffer;")
    rewind = JavaMethod("()Ljava/nio/Buffer;")
    compact = JavaMethod("()Ljava/nio/ShortBuffer;")
    isDirect = JavaMethod("()Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    compareTo = JavaMethod("(Ljava/nio/ShortBuffer;)I")
    mismatch = JavaMethod("(Ljava/nio/ShortBuffer;)I")
    order = JavaMethod("()Ljava/nio/ByteOrder;")