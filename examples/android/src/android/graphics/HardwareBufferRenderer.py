from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HardwareBufferRenderer"]

class HardwareBufferRenderer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/HardwareBufferRenderer"
    __javaconstructor__ = [("(Landroid/hardware/HardwareBuffer;)V", False)]
    setContentRoot = JavaMethod("(Landroid/graphics/RenderNode;)V")
    obtainRenderRequest = JavaMethod("()Landroid/graphics/HardwareBufferRenderer$RenderRequest;")
    isClosed = JavaMethod("()Z")
    close = JavaMethod("()V")
    setLightSourceGeometry = JavaMethod("(FFFF)V")
    setLightSourceAlpha = JavaMethod("(FF)V")

    class RenderRequest(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/HardwareBufferRenderer/RenderRequest"
        draw = JavaMethod("(Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")
        setColorSpace = JavaMethod("(Landroid/graphics/ColorSpace;)Landroid/graphics/HardwareBufferRenderer$RenderRequest;")
        setBufferTransform = JavaMethod("(I)Landroid/graphics/HardwareBufferRenderer$RenderRequest;")

    class RenderResult(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/HardwareBufferRenderer/RenderResult"
        ERROR_UNKNOWN = JavaStaticField("I")
        SUCCESS = JavaStaticField("I")
        getFence = JavaMethod("()Landroid/hardware/SyncFence;")
        getStatus = JavaMethod("()I")