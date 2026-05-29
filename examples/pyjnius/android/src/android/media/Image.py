from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Image"]

class Image(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/Image"
    close = JavaMethod("()V")
    getFence = JavaMethod("()Landroid/hardware/SyncFence;")
    setCropRect = JavaMethod("(Landroid/graphics/Rect;)V")
    getCropRect = JavaMethod("()Landroid/graphics/Rect;")
    setDataSpace = JavaMethod("(I)V")
    getPlanes = JavaMethod("()[Landroid/media/Image$Plane;")
    setFence = JavaMethod("(Landroid/hardware/SyncFence;)V")
    setTimestamp = JavaMethod("(J)V")
    getHeight = JavaMethod("()I")
    getWidth = JavaMethod("()I")
    getHardwareBuffer = JavaMethod("()Landroid/hardware/HardwareBuffer;")
    getTimestamp = JavaMethod("()J")
    getDataSpace = JavaMethod("()I")
    getFormat = JavaMethod("()I")

    class Plane(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/Image$Plane"
        getBuffer = JavaMethod("()Ljava/nio/ByteBuffer;")
        getPixelStride = JavaMethod("()I")
        getRowStride = JavaMethod("()I")