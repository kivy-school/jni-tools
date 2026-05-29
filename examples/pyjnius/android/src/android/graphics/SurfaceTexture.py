from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SurfaceTexture"]

class SurfaceTexture(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/SurfaceTexture"
    __javaconstructor__ = [("(IZ)V", False), ("(I)V", False), ("(Z)V", False)]
    release = JavaMethod("()V")
    getTimestamp = JavaMethod("()J")
    attachToGLContext = JavaMethod("(I)V")
    detachFromGLContext = JavaMethod("()V")
    getDataSpace = JavaMethod("()I")
    getTransformMatrix = JavaMethod("([F)V")
    isReleased = JavaMethod("()Z")
    releaseTexImage = JavaMethod("()V")
    setDefaultBufferSize = JavaMethod("(II)V")
    setOnFrameAvailableListener = JavaMultipleMethod([("(Landroid/graphics/SurfaceTexture$OnFrameAvailableListener;)V", False, False), ("(Landroid/graphics/SurfaceTexture$OnFrameAvailableListener;Landroid/os/Handler;)V", False, False)])
    updateTexImage = JavaMethod("()V")

    class OutOfResourcesException(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/SurfaceTexture$OutOfResourcesException"
        __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]

    class OnFrameAvailableListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/SurfaceTexture$OnFrameAvailableListener"
        onFrameAvailable = JavaMethod("(Landroid/graphics/SurfaceTexture;)V")