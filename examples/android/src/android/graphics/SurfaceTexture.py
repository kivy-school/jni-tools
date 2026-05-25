from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SurfaceTexture"]

class SurfaceTexture(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/SurfaceTexture"
    __javaconstructor__ = [("(I)V", False), ("(IZ)V", False), ("(Z)V", False)]
    setOnFrameAvailableListener = JavaMultipleMethod([("(Landroid/graphics/SurfaceTexture$OnFrameAvailableListener;)V", False, False), ("(Landroid/graphics/SurfaceTexture$OnFrameAvailableListener;Landroid/os/Handler;)V", False, False)])
    setDefaultBufferSize = JavaMethod("(II)V")
    updateTexImage = JavaMethod("()V")
    releaseTexImage = JavaMethod("()V")
    detachFromGLContext = JavaMethod("()V")
    attachToGLContext = JavaMethod("(I)V")
    getTransformMatrix = JavaMethod("([F)V")
    getTimestamp = JavaMethod("()J")
    getDataSpace = JavaMethod("()I")
    release = JavaMethod("()V")
    isReleased = JavaMethod("()Z")
    finalize = JavaMethod("()V")

    class OnFrameAvailableListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/SurfaceTexture/OnFrameAvailableListener"
        onFrameAvailable = JavaMethod("(Landroid/graphics/SurfaceTexture;)V")

    class OutOfResourcesException(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/SurfaceTexture/OutOfResourcesException"
        __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]