from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FloatBuffer"]

class FloatBuffer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/FloatBuffer"
    reset = JavaMultipleMethod([("()Ljava/nio/Buffer;", False, False), ("()Ljava/nio/FloatBuffer;", False, False)])
    put = JavaMultipleMethod([("(Ljava/nio/FloatBuffer;)Ljava/nio/FloatBuffer;", False, False), ("(ILjava/nio/FloatBuffer;II)Ljava/nio/FloatBuffer;", False, False), ("(F)Ljava/nio/FloatBuffer;", False, False), ("(IF)Ljava/nio/FloatBuffer;", False, False), ("(I[F)Ljava/nio/FloatBuffer;", False, False), ("(I[FII)Ljava/nio/FloatBuffer;", False, False), ("([F)Ljava/nio/FloatBuffer;", False, False), ("([FII)Ljava/nio/FloatBuffer;", False, False)])
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    compareTo = JavaMultipleMethod([("(Ljava/lang/Object;)I", False, False), ("(Ljava/nio/FloatBuffer;)I", False, False)])
    clear = JavaMultipleMethod([("()Ljava/nio/FloatBuffer;", False, False), ("()Ljava/nio/Buffer;", False, False)])
    wrap = JavaMultipleMethod([("([F)Ljava/nio/FloatBuffer;", True, False), ("([FII)Ljava/nio/FloatBuffer;", True, False)])
    position = JavaMultipleMethod([("(I)Ljava/nio/Buffer;", False, False), ("(I)Ljava/nio/FloatBuffer;", False, False)])
    mismatch = JavaMethod("(Ljava/nio/FloatBuffer;)I")
    get = JavaMultipleMethod([("(I[F)Ljava/nio/FloatBuffer;", False, False), ("(I[FII)Ljava/nio/FloatBuffer;", False, False), ("([F)Ljava/nio/FloatBuffer;", False, False), ("([FII)Ljava/nio/FloatBuffer;", False, False), ("(I)F", False, False), ("()F", False, False)])
    limit = JavaMultipleMethod([("(I)Ljava/nio/Buffer;", False, False), ("(I)Ljava/nio/FloatBuffer;", False, False)])
    isDirect = JavaMethod("()Z")
    hasArray = JavaMethod("()Z")
    array = JavaMultipleMethod([("()[F", False, False), ("()Ljava/lang/Object;", False, False)])
    arrayOffset = JavaMethod("()I")
    allocate = JavaStaticMethod("(I)Ljava/nio/FloatBuffer;")
    mark = JavaMultipleMethod([("()Ljava/nio/Buffer;", False, False), ("()Ljava/nio/FloatBuffer;", False, False)])
    asReadOnlyBuffer = JavaMethod("()Ljava/nio/FloatBuffer;")
    compact = JavaMethod("()Ljava/nio/FloatBuffer;")
    order = JavaMethod("()Ljava/nio/ByteOrder;")
    flip = JavaMultipleMethod([("()Ljava/nio/FloatBuffer;", False, False), ("()Ljava/nio/Buffer;", False, False)])
    rewind = JavaMultipleMethod([("()Ljava/nio/FloatBuffer;", False, False), ("()Ljava/nio/Buffer;", False, False)])
    slice = JavaMultipleMethod([("(II)Ljava/nio/Buffer;", False, False), ("()Ljava/nio/Buffer;", False, False), ("(II)Ljava/nio/FloatBuffer;", False, False), ("()Ljava/nio/FloatBuffer;", False, False)])
    duplicate = JavaMultipleMethod([("()Ljava/nio/FloatBuffer;", False, False), ("()Ljava/nio/Buffer;", False, False)])