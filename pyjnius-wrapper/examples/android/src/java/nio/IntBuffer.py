from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IntBuffer"]

class IntBuffer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/IntBuffer"
    allocate = JavaStaticMethod("(I)Ljava/nio/IntBuffer;")
    wrap = JavaMultipleMethod([("([III)Ljava/nio/IntBuffer;", True, False), ("([I)Ljava/nio/IntBuffer;", True, False)])
    slice = JavaMultipleMethod([("()Ljava/nio/IntBuffer;", False, False), ("(II)Ljava/nio/IntBuffer;", False, False)])
    duplicate = JavaMethod("()Ljava/nio/IntBuffer;")
    asReadOnlyBuffer = JavaMethod("()Ljava/nio/IntBuffer;")
    get = JavaMultipleMethod([("()I", False, False), ("(I)I", False, False), ("([III)Ljava/nio/IntBuffer;", False, False), ("([I)Ljava/nio/IntBuffer;", False, False), ("(I[III)Ljava/nio/IntBuffer;", False, False), ("(I[I)Ljava/nio/IntBuffer;", False, False)])
    put = JavaMultipleMethod([("(I)Ljava/nio/IntBuffer;", False, False), ("(II)Ljava/nio/IntBuffer;", False, False), ("(Ljava/nio/IntBuffer;)Ljava/nio/IntBuffer;", False, False), ("(ILjava/nio/IntBuffer;II)Ljava/nio/IntBuffer;", False, False), ("([III)Ljava/nio/IntBuffer;", False, False), ("([I)Ljava/nio/IntBuffer;", False, False), ("(I[III)Ljava/nio/IntBuffer;", False, False), ("(I[I)Ljava/nio/IntBuffer;", False, False)])
    hasArray = JavaMethod("()Z")
    array = JavaMethod("()[I")
    arrayOffset = JavaMethod("()I")
    position = JavaMethod("(I)Ljava/nio/Buffer;")
    limit = JavaMethod("(I)Ljava/nio/Buffer;")
    mark = JavaMethod("()Ljava/nio/Buffer;")
    reset = JavaMethod("()Ljava/nio/Buffer;")
    clear = JavaMethod("()Ljava/nio/Buffer;")
    flip = JavaMethod("()Ljava/nio/Buffer;")
    rewind = JavaMethod("()Ljava/nio/Buffer;")
    compact = JavaMethod("()Ljava/nio/IntBuffer;")
    isDirect = JavaMethod("()Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    compareTo = JavaMethod("(Ljava/nio/IntBuffer;)I")
    mismatch = JavaMethod("(Ljava/nio/IntBuffer;)I")
    order = JavaMethod("()Ljava/nio/ByteOrder;")