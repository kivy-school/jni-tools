from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MappedByteBuffer"]

class MappedByteBuffer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/MappedByteBuffer"
    reset = JavaMultipleMethod([("()Ljava/nio/MappedByteBuffer;", False, False), ("()Ljava/nio/Buffer;", False, False), ("()Ljava/nio/ByteBuffer;", False, False)])
    load = JavaMethod("()Ljava/nio/MappedByteBuffer;")
    clear = JavaMultipleMethod([("()Ljava/nio/Buffer;", False, False), ("()Ljava/nio/ByteBuffer;", False, False), ("()Ljava/nio/MappedByteBuffer;", False, False)])
    position = JavaMultipleMethod([("(I)Ljava/nio/MappedByteBuffer;", False, False), ("(I)Ljava/nio/Buffer;", False, False), ("(I)Ljava/nio/ByteBuffer;", False, False)])
    limit = JavaMultipleMethod([("(I)Ljava/nio/ByteBuffer;", False, False), ("(I)Ljava/nio/Buffer;", False, False), ("(I)Ljava/nio/MappedByteBuffer;", False, False)])
    mark = JavaMultipleMethod([("()Ljava/nio/MappedByteBuffer;", False, False), ("()Ljava/nio/ByteBuffer;", False, False), ("()Ljava/nio/Buffer;", False, False)])
    compact = JavaMultipleMethod([("()Ljava/nio/MappedByteBuffer;", False, False), ("()Ljava/nio/ByteBuffer;", False, False)])
    isLoaded = JavaMethod("()Z")
    force = JavaMultipleMethod([("()Ljava/nio/MappedByteBuffer;", False, False), ("(II)Ljava/nio/MappedByteBuffer;", False, False)])
    flip = JavaMultipleMethod([("()Ljava/nio/ByteBuffer;", False, False), ("()Ljava/nio/Buffer;", False, False), ("()Ljava/nio/MappedByteBuffer;", False, False)])
    rewind = JavaMultipleMethod([("()Ljava/nio/Buffer;", False, False), ("()Ljava/nio/ByteBuffer;", False, False), ("()Ljava/nio/MappedByteBuffer;", False, False)])
    slice = JavaMultipleMethod([("(II)Ljava/nio/MappedByteBuffer;", False, False), ("()Ljava/nio/MappedByteBuffer;", False, False), ("()Ljava/nio/Buffer;", False, False), ("(II)Ljava/nio/Buffer;", False, False), ("(II)Ljava/nio/ByteBuffer;", False, False), ("()Ljava/nio/ByteBuffer;", False, False)])
    duplicate = JavaMultipleMethod([("()Ljava/nio/ByteBuffer;", False, False), ("()Ljava/nio/Buffer;", False, False), ("()Ljava/nio/MappedByteBuffer;", False, False)])