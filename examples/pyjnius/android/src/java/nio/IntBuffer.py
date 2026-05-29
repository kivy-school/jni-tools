from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IntBuffer"]

class IntBuffer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/IntBuffer"
    reset = JavaMultipleMethod([("()Ljava/nio/Buffer;", False, False), ("()Ljava/nio/IntBuffer;", False, False)])
    put = JavaMultipleMethod([("(Ljava/nio/IntBuffer;)Ljava/nio/IntBuffer;", False, False), ("(ILjava/nio/IntBuffer;II)Ljava/nio/IntBuffer;", False, False), ("(I)Ljava/nio/IntBuffer;", False, False), ("(II)Ljava/nio/IntBuffer;", False, False), ("(I[I)Ljava/nio/IntBuffer;", False, False), ("(I[III)Ljava/nio/IntBuffer;", False, False), ("([I)Ljava/nio/IntBuffer;", False, False), ("([III)Ljava/nio/IntBuffer;", False, False)])
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    compareTo = JavaMultipleMethod([("(Ljava/lang/Object;)I", False, False), ("(Ljava/nio/IntBuffer;)I", False, False)])
    clear = JavaMultipleMethod([("()Ljava/nio/IntBuffer;", False, False), ("()Ljava/nio/Buffer;", False, False)])
    wrap = JavaMultipleMethod([("([I)Ljava/nio/IntBuffer;", True, False), ("([III)Ljava/nio/IntBuffer;", True, False)])
    position = JavaMultipleMethod([("(I)Ljava/nio/Buffer;", False, False), ("(I)Ljava/nio/IntBuffer;", False, False)])
    mismatch = JavaMethod("(Ljava/nio/IntBuffer;)I")
    get = JavaMultipleMethod([("(I[I)Ljava/nio/IntBuffer;", False, False), ("(I[III)Ljava/nio/IntBuffer;", False, False), ("([I)Ljava/nio/IntBuffer;", False, False), ("([III)Ljava/nio/IntBuffer;", False, False), ("(I)I", False, False), ("()I", False, False)])
    limit = JavaMultipleMethod([("(I)Ljava/nio/Buffer;", False, False), ("(I)Ljava/nio/IntBuffer;", False, False)])
    isDirect = JavaMethod("()Z")
    hasArray = JavaMethod("()Z")
    array = JavaMultipleMethod([("()[I", False, False), ("()Ljava/lang/Object;", False, False)])
    arrayOffset = JavaMethod("()I")
    allocate = JavaStaticMethod("(I)Ljava/nio/IntBuffer;")
    mark = JavaMultipleMethod([("()Ljava/nio/Buffer;", False, False), ("()Ljava/nio/IntBuffer;", False, False)])
    asReadOnlyBuffer = JavaMethod("()Ljava/nio/IntBuffer;")
    compact = JavaMethod("()Ljava/nio/IntBuffer;")
    order = JavaMethod("()Ljava/nio/ByteOrder;")
    flip = JavaMultipleMethod([("()Ljava/nio/IntBuffer;", False, False), ("()Ljava/nio/Buffer;", False, False)])
    rewind = JavaMultipleMethod([("()Ljava/nio/IntBuffer;", False, False), ("()Ljava/nio/Buffer;", False, False)])
    slice = JavaMultipleMethod([("(II)Ljava/nio/Buffer;", False, False), ("()Ljava/nio/Buffer;", False, False), ("(II)Ljava/nio/IntBuffer;", False, False), ("()Ljava/nio/IntBuffer;", False, False)])
    duplicate = JavaMultipleMethod([("()Ljava/nio/IntBuffer;", False, False), ("()Ljava/nio/Buffer;", False, False)])