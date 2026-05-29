from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Image"]

class Image(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/Image"
    getFormat = JavaMethod("()I")
    getWidth = JavaMethod("()I")
    getHeight = JavaMethod("()I")
    getTimestamp = JavaMethod("()J")
    getFence = JavaMethod("()Landroid/hardware/SyncFence;")
    getHardwareBuffer = JavaMethod("()Landroid/hardware/HardwareBuffer;")
    setTimestamp = JavaMethod("(J)V")
    setFence = JavaMethod("(Landroid/hardware/SyncFence;)V")
    getDataSpace = JavaMethod("()I")
    setDataSpace = JavaMethod("(I)V")
    getCropRect = JavaMethod("()Landroid/graphics/Rect;")
    setCropRect = JavaMethod("(Landroid/graphics/Rect;)V")
    getPlanes = JavaMethod("()[Landroid/media/Image$Plane;")
    close = JavaMethod("()V")

    class Plane(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/Image/Plane"
        getRowStride = JavaMethod("()I")
        getPixelStride = JavaMethod("()I")
        getBuffer = JavaMethod("()Ljava/nio/ByteBuffer;")