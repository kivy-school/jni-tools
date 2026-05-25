from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Buffer"]

class Buffer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/Buffer"
    capacity = JavaMethod("()I")
    position = JavaMultipleMethod([("()I", False, False), ("(I)Ljava/nio/Buffer;", False, False)])
    limit = JavaMultipleMethod([("()I", False, False), ("(I)Ljava/nio/Buffer;", False, False)])
    mark = JavaMethod("()Ljava/nio/Buffer;")
    reset = JavaMethod("()Ljava/nio/Buffer;")
    clear = JavaMethod("()Ljava/nio/Buffer;")
    flip = JavaMethod("()Ljava/nio/Buffer;")
    rewind = JavaMethod("()Ljava/nio/Buffer;")
    remaining = JavaMethod("()I")
    hasRemaining = JavaMethod("()Z")
    isReadOnly = JavaMethod("()Z")
    hasArray = JavaMethod("()Z")
    array = JavaMethod("()Ljava/lang/Object;")
    arrayOffset = JavaMethod("()I")
    isDirect = JavaMethod("()Z")
    slice = JavaMultipleMethod([("()Ljava/nio/Buffer;", False, False), ("(II)Ljava/nio/Buffer;", False, False)])
    duplicate = JavaMethod("()Ljava/nio/Buffer;")