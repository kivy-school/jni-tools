from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FloatBuffer"]

class FloatBuffer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/FloatBuffer"
    allocate = JavaStaticMethod("(I)Ljava/nio/FloatBuffer;")
    wrap = JavaMultipleMethod([("([FII)Ljava/nio/FloatBuffer;", True, False), ("([F)Ljava/nio/FloatBuffer;", True, False)])
    slice = JavaMultipleMethod([("()Ljava/nio/FloatBuffer;", False, False), ("(II)Ljava/nio/FloatBuffer;", False, False)])
    duplicate = JavaMethod("()Ljava/nio/FloatBuffer;")
    asReadOnlyBuffer = JavaMethod("()Ljava/nio/FloatBuffer;")
    get = JavaMultipleMethod([("()F", False, False), ("(I)F", False, False), ("([FII)Ljava/nio/FloatBuffer;", False, False), ("([F)Ljava/nio/FloatBuffer;", False, False), ("(I[FII)Ljava/nio/FloatBuffer;", False, False), ("(I[F)Ljava/nio/FloatBuffer;", False, False)])
    put = JavaMultipleMethod([("(F)Ljava/nio/FloatBuffer;", False, False), ("(IF)Ljava/nio/FloatBuffer;", False, False), ("(Ljava/nio/FloatBuffer;)Ljava/nio/FloatBuffer;", False, False), ("(ILjava/nio/FloatBuffer;II)Ljava/nio/FloatBuffer;", False, False), ("([FII)Ljava/nio/FloatBuffer;", False, False), ("([F)Ljava/nio/FloatBuffer;", False, False), ("(I[FII)Ljava/nio/FloatBuffer;", False, False), ("(I[F)Ljava/nio/FloatBuffer;", False, False)])
    hasArray = JavaMethod("()Z")
    array = JavaMethod("()[F")
    arrayOffset = JavaMethod("()I")
    position = JavaMethod("(I)Ljava/nio/Buffer;")
    limit = JavaMethod("(I)Ljava/nio/Buffer;")
    mark = JavaMethod("()Ljava/nio/Buffer;")
    reset = JavaMethod("()Ljava/nio/Buffer;")
    clear = JavaMethod("()Ljava/nio/Buffer;")
    flip = JavaMethod("()Ljava/nio/Buffer;")
    rewind = JavaMethod("()Ljava/nio/Buffer;")
    compact = JavaMethod("()Ljava/nio/FloatBuffer;")
    isDirect = JavaMethod("()Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    compareTo = JavaMethod("(Ljava/nio/FloatBuffer;)I")
    mismatch = JavaMethod("(Ljava/nio/FloatBuffer;)I")
    order = JavaMethod("()Ljava/nio/ByteOrder;")