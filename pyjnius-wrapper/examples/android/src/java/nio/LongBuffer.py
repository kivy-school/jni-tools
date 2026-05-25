from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LongBuffer"]

class LongBuffer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/LongBuffer"
    allocate = JavaStaticMethod("(I)Ljava/nio/LongBuffer;")
    wrap = JavaMultipleMethod([("([JII)Ljava/nio/LongBuffer;", True, False), ("([J)Ljava/nio/LongBuffer;", True, False)])
    slice = JavaMultipleMethod([("()Ljava/nio/LongBuffer;", False, False), ("(II)Ljava/nio/LongBuffer;", False, False)])
    duplicate = JavaMethod("()Ljava/nio/LongBuffer;")
    asReadOnlyBuffer = JavaMethod("()Ljava/nio/LongBuffer;")
    get = JavaMultipleMethod([("()J", False, False), ("(I)J", False, False), ("([JII)Ljava/nio/LongBuffer;", False, False), ("([J)Ljava/nio/LongBuffer;", False, False), ("(I[JII)Ljava/nio/LongBuffer;", False, False), ("(I[J)Ljava/nio/LongBuffer;", False, False)])
    put = JavaMultipleMethod([("(J)Ljava/nio/LongBuffer;", False, False), ("(IJ)Ljava/nio/LongBuffer;", False, False), ("(Ljava/nio/LongBuffer;)Ljava/nio/LongBuffer;", False, False), ("(ILjava/nio/LongBuffer;II)Ljava/nio/LongBuffer;", False, False), ("([JII)Ljava/nio/LongBuffer;", False, False), ("([J)Ljava/nio/LongBuffer;", False, False), ("(I[JII)Ljava/nio/LongBuffer;", False, False), ("(I[J)Ljava/nio/LongBuffer;", False, False)])
    hasArray = JavaMethod("()Z")
    array = JavaMethod("()[J")
    arrayOffset = JavaMethod("()I")
    position = JavaMethod("(I)Ljava/nio/Buffer;")
    limit = JavaMethod("(I)Ljava/nio/Buffer;")
    mark = JavaMethod("()Ljava/nio/Buffer;")
    reset = JavaMethod("()Ljava/nio/Buffer;")
    clear = JavaMethod("()Ljava/nio/Buffer;")
    flip = JavaMethod("()Ljava/nio/Buffer;")
    rewind = JavaMethod("()Ljava/nio/Buffer;")
    compact = JavaMethod("()Ljava/nio/LongBuffer;")
    isDirect = JavaMethod("()Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    compareTo = JavaMethod("(Ljava/nio/LongBuffer;)I")
    mismatch = JavaMethod("(Ljava/nio/LongBuffer;)I")
    order = JavaMethod("()Ljava/nio/ByteOrder;")