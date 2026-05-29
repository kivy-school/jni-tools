from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HardwareBufferRenderer"]

class HardwareBufferRenderer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/HardwareBufferRenderer"
    __javaconstructor__ = [("(Landroid/hardware/HardwareBuffer;)V", False)]
    obtainRenderRequest = JavaMethod("()Landroid/graphics/HardwareBufferRenderer$RenderRequest;")
    setContentRoot = JavaMethod("(Landroid/graphics/RenderNode;)V")
    setLightSourceAlpha = JavaMethod("(FF)V")
    setLightSourceGeometry = JavaMethod("(FFFF)V")
    close = JavaMethod("()V")
    isClosed = JavaMethod("()Z")

    class RenderResult(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/HardwareBufferRenderer$RenderResult"
        ERROR_UNKNOWN = JavaStaticField("I")
        SUCCESS = JavaStaticField("I")
        getStatus = JavaMethod("()I")
        getFence = JavaMethod("()Landroid/hardware/SyncFence;")

    class RenderRequest(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/HardwareBufferRenderer$RenderRequest"
        setBufferTransform = JavaMethod("(I)Landroid/graphics/HardwareBufferRenderer$RenderRequest;")
        draw = JavaMethod("(Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")
        setColorSpace = JavaMethod("(Landroid/graphics/ColorSpace;)Landroid/graphics/HardwareBufferRenderer$RenderRequest;")