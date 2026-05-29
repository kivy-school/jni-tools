from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LongBuffer"]

class LongBuffer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/LongBuffer"
    reset = JavaMultipleMethod([("()Ljava/nio/Buffer;", False, False), ("()Ljava/nio/LongBuffer;", False, False)])
    put = JavaMultipleMethod([("(Ljava/nio/LongBuffer;)Ljava/nio/LongBuffer;", False, False), ("(ILjava/nio/LongBuffer;II)Ljava/nio/LongBuffer;", False, False), ("(J)Ljava/nio/LongBuffer;", False, False), ("(IJ)Ljava/nio/LongBuffer;", False, False), ("(I[J)Ljava/nio/LongBuffer;", False, False), ("(I[JII)Ljava/nio/LongBuffer;", False, False), ("([J)Ljava/nio/LongBuffer;", False, False), ("([JII)Ljava/nio/LongBuffer;", False, False)])
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    compareTo = JavaMultipleMethod([("(Ljava/lang/Object;)I", False, False), ("(Ljava/nio/LongBuffer;)I", False, False)])
    clear = JavaMultipleMethod([("()Ljava/nio/LongBuffer;", False, False), ("()Ljava/nio/Buffer;", False, False)])
    wrap = JavaMultipleMethod([("([J)Ljava/nio/LongBuffer;", True, False), ("([JII)Ljava/nio/LongBuffer;", True, False)])
    position = JavaMultipleMethod([("(I)Ljava/nio/Buffer;", False, False), ("(I)Ljava/nio/LongBuffer;", False, False)])
    mismatch = JavaMethod("(Ljava/nio/LongBuffer;)I")
    get = JavaMultipleMethod([("(I[J)Ljava/nio/LongBuffer;", False, False), ("(I[JII)Ljava/nio/LongBuffer;", False, False), ("([J)Ljava/nio/LongBuffer;", False, False), ("([JII)Ljava/nio/LongBuffer;", False, False), ("(I)J", False, False), ("()J", False, False)])
    limit = JavaMultipleMethod([("(I)Ljava/nio/Buffer;", False, False), ("(I)Ljava/nio/LongBuffer;", False, False)])
    isDirect = JavaMethod("()Z")
    hasArray = JavaMethod("()Z")
    array = JavaMultipleMethod([("()[J", False, False), ("()Ljava/lang/Object;", False, False)])
    arrayOffset = JavaMethod("()I")
    allocate = JavaStaticMethod("(I)Ljava/nio/LongBuffer;")
    mark = JavaMultipleMethod([("()Ljava/nio/Buffer;", False, False), ("()Ljava/nio/LongBuffer;", False, False)])
    asReadOnlyBuffer = JavaMethod("()Ljava/nio/LongBuffer;")
    compact = JavaMethod("()Ljava/nio/LongBuffer;")
    order = JavaMethod("()Ljava/nio/ByteOrder;")
    flip = JavaMultipleMethod([("()Ljava/nio/LongBuffer;", False, False), ("()Ljava/nio/Buffer;", False, False)])
    rewind = JavaMultipleMethod([("()Ljava/nio/LongBuffer;", False, False), ("()Ljava/nio/Buffer;", False, False)])
    slice = JavaMultipleMethod([("(II)Ljava/nio/Buffer;", False, False), ("()Ljava/nio/Buffer;", False, False), ("(II)Ljava/nio/LongBuffer;", False, False), ("()Ljava/nio/LongBuffer;", False, False)])
    duplicate = JavaMultipleMethod([("()Ljava/nio/LongBuffer;", False, False), ("()Ljava/nio/Buffer;", False, False)])