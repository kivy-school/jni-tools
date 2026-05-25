from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HardwareRenderer"]

class HardwareRenderer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/HardwareRenderer"
    __javaconstructor__ = [("()V", False)]
    SYNC_CONTEXT_IS_STOPPED = JavaStaticField("I")
    SYNC_FRAME_DROPPED = JavaStaticField("I")
    SYNC_LOST_SURFACE_REWARD_IF_FOUND = JavaStaticField("I")
    SYNC_OK = JavaStaticField("I")
    SYNC_REDRAW_REQUESTED = JavaStaticField("I")
    destroy = JavaMethod("()V")
    setName = JavaMethod("(Ljava/lang/String;)V")
    setLightSourceGeometry = JavaMethod("(FFFF)V")
    setLightSourceAlpha = JavaMethod("(FF)V")
    setContentRoot = JavaMethod("(Landroid/graphics/RenderNode;)V")
    setSurface = JavaMethod("(Landroid/view/Surface;)V")
    createRenderRequest = JavaMethod("()Landroid/graphics/HardwareRenderer$FrameRenderRequest;")
    stop = JavaMethod("()V")
    start = JavaMethod("()V")
    clearContent = JavaMethod("()V")
    notifyFramePending = JavaMethod("()V")
    setOpaque = JavaMethod("(Z)V")
    isOpaque = JavaMethod("()Z")
    isDrawingEnabled = JavaStaticMethod("()Z")
    setDrawingEnabled = JavaStaticMethod("(Z)V")

    class FrameRenderRequest(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/HardwareRenderer/FrameRenderRequest"
        setVsyncTime = JavaMethod("(J)Landroid/graphics/HardwareRenderer$FrameRenderRequest;")
        setFrameCommitCallback = JavaMethod("(Ljava/util/concurrent/Executor;Ljava/lang/Runnable;)Landroid/graphics/HardwareRenderer$FrameRenderRequest;")
        setWaitForPresent = JavaMethod("(Z)Landroid/graphics/HardwareRenderer$FrameRenderRequest;")
        syncAndDraw = JavaMethod("()I")