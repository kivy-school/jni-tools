from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Buffer"]

class Buffer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/Buffer"
    reset = JavaMethod("()Ljava/nio/Buffer;")
    clear = JavaMethod("()Ljava/nio/Buffer;")
    position = JavaMultipleMethod([("(I)Ljava/nio/Buffer;", False, False), ("()I", False, False)])
    limit = JavaMultipleMethod([("()I", False, False), ("(I)Ljava/nio/Buffer;", False, False)])
    remaining = JavaMethod("()I")
    isDirect = JavaMethod("()Z")
    hasArray = JavaMethod("()Z")
    array = JavaMethod("()Ljava/lang/Object;")
    arrayOffset = JavaMethod("()I")
    capacity = JavaMethod("()I")
    mark = JavaMethod("()Ljava/nio/Buffer;")
    flip = JavaMethod("()Ljava/nio/Buffer;")
    rewind = JavaMethod("()Ljava/nio/Buffer;")
    hasRemaining = JavaMethod("()Z")
    isReadOnly = JavaMethod("()Z")
    slice = JavaMultipleMethod([("()Ljava/nio/Buffer;", False, False), ("(II)Ljava/nio/Buffer;", False, False)])
    duplicate = JavaMethod("()Ljava/nio/Buffer;")