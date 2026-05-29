from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HardwareRenderer"]

class HardwareRenderer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/HardwareRenderer"
    __javaconstructor__ = [("()V", False)]
    SYNC_CONTEXT_IS_STOPPED = JavaStaticField("I")
    SYNC_FRAME_DROPPED = JavaStaticField("I")
    SYNC_LOST_SURFACE_REWARD_IF_FOUND = JavaStaticField("I")
    SYNC_OK = JavaStaticField("I")
    SYNC_REDRAW_REQUESTED = JavaStaticField("I")
    clearContent = JavaMethod("()V")
    notifyFramePending = JavaMethod("()V")
    setDrawingEnabled = JavaStaticMethod("(Z)V")
    isDrawingEnabled = JavaStaticMethod("()Z")
    setContentRoot = JavaMethod("(Landroid/graphics/RenderNode;)V")
    createRenderRequest = JavaMethod("()Landroid/graphics/HardwareRenderer$FrameRenderRequest;")
    setLightSourceAlpha = JavaMethod("(FF)V")
    setLightSourceGeometry = JavaMethod("(FFFF)V")
    start = JavaMethod("()V")
    setName = JavaMethod("(Ljava/lang/String;)V")
    destroy = JavaMethod("()V")
    setOpaque = JavaMethod("(Z)V")
    isOpaque = JavaMethod("()Z")
    setSurface = JavaMethod("(Landroid/view/Surface;)V")
    stop = JavaMethod("()V")

    class FrameRenderRequest(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/HardwareRenderer$FrameRenderRequest"
        setVsyncTime = JavaMethod("(J)Landroid/graphics/HardwareRenderer$FrameRenderRequest;")
        setWaitForPresent = JavaMethod("(Z)Landroid/graphics/HardwareRenderer$FrameRenderRequest;")
        setFrameCommitCallback = JavaMethod("(Ljava/util/concurrent/Executor;Ljava/lang/Runnable;)Landroid/graphics/HardwareRenderer$FrameRenderRequest;")
        syncAndDraw = JavaMethod("()I")