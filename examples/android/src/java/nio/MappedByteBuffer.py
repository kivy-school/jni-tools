from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MappedByteBuffer"]

class MappedByteBuffer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/MappedByteBuffer"
    isLoaded = JavaMethod("()Z")
    load = JavaMethod("()Ljava/nio/MappedByteBuffer;")
    force = JavaMultipleMethod([("()Ljava/nio/MappedByteBuffer;", False, False), ("(II)Ljava/nio/MappedByteBuffer;", False, False)])
    position = JavaMethod("(I)Ljava/nio/Buffer;")
    limit = JavaMethod("(I)Ljava/nio/Buffer;")
    mark = JavaMethod("()Ljava/nio/Buffer;")
    reset = JavaMethod("()Ljava/nio/Buffer;")
    clear = JavaMethod("()Ljava/nio/Buffer;")
    flip = JavaMethod("()Ljava/nio/Buffer;")
    rewind = JavaMethod("()Ljava/nio/Buffer;")
    slice = JavaMultipleMethod([("()Ljava/nio/ByteBuffer;", False, False), ("(II)Ljava/nio/MappedByteBuffer;", False, False)])
    duplicate = JavaMethod("()Ljava/nio/ByteBuffer;")
    compact = JavaMethod("()Ljava/nio/ByteBuffer;")