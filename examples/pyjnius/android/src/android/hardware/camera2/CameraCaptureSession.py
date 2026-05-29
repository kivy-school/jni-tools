from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CameraCaptureSession"]

class CameraCaptureSession(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/camera2/CameraCaptureSession"
    __javaconstructor__ = [("()V", False)]
    stopRepeating = JavaMethod("()V")
    capture = JavaMethod("(Landroid/hardware/camera2/CaptureRequest;Landroid/hardware/camera2/CameraCaptureSession$CaptureCallback;Landroid/os/Handler;)I")
    setRepeatingRequest = JavaMethod("(Landroid/hardware/camera2/CaptureRequest;Landroid/hardware/camera2/CameraCaptureSession$CaptureCallback;Landroid/os/Handler;)I")
    close = JavaMethod("()V")
    prepare = JavaMethod("(Landroid/view/Surface;)V")
    abortCaptures = JavaMethod("()V")
    isReprocessable = JavaMethod("()Z")
    getInputSurface = JavaMethod("()Landroid/view/Surface;")
    captureBurst = JavaMethod("(Ljava/util/List;Landroid/hardware/camera2/CameraCaptureSession$CaptureCallback;Landroid/os/Handler;)I")
    switchToOffline = JavaMethod("(Ljava/util/Collection;Ljava/util/concurrent/Executor;Landroid/hardware/camera2/CameraOfflineSession$CameraOfflineSessionCallback;)Landroid/hardware/camera2/CameraOfflineSession;")
    setRepeatingBurst = JavaMethod("(Ljava/util/List;Landroid/hardware/camera2/CameraCaptureSession$CaptureCallback;Landroid/os/Handler;)I")
    captureBurstRequests = JavaMethod("(Ljava/util/List;Ljava/util/concurrent/Executor;Landroid/hardware/camera2/CameraCaptureSession$CaptureCallback;)I")
    captureSingleRequest = JavaMethod("(Landroid/hardware/camera2/CaptureRequest;Ljava/util/concurrent/Executor;Landroid/hardware/camera2/CameraCaptureSession$CaptureCallback;)I")
    finalizeOutputConfigurations = JavaMethod("(Ljava/util/List;)V")
    setRepeatingBurstRequests = JavaMethod("(Ljava/util/List;Ljava/util/concurrent/Executor;Landroid/hardware/camera2/CameraCaptureSession$CaptureCallback;)I")
    setSingleRepeatingRequest = JavaMethod("(Landroid/hardware/camera2/CaptureRequest;Ljava/util/concurrent/Executor;Landroid/hardware/camera2/CameraCaptureSession$CaptureCallback;)I")
    supportsOfflineProcessing = JavaMethod("(Landroid/view/Surface;)Z")
    updateOutputConfiguration = JavaMethod("(Landroid/hardware/camera2/params/OutputConfiguration;)V")
    getDevice = JavaMethod("()Landroid/hardware/camera2/CameraDevice;")

    class StateCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/camera2/CameraCaptureSession$StateCallback"
        __javaconstructor__ = [("()V", False)]
        onActive = JavaMethod("(Landroid/hardware/camera2/CameraCaptureSession;)V")
        onCaptureQueueEmpty = JavaMethod("(Landroid/hardware/camera2/CameraCaptureSession;)V")
        onReady = JavaMethod("(Landroid/hardware/camera2/CameraCaptureSession;)V")
        onSurfacePrepared = JavaMethod("(Landroid/hardware/camera2/CameraCaptureSession;Landroid/view/Surface;)V")
        onClosed = JavaMethod("(Landroid/hardware/camera2/CameraCaptureSession;)V")
        onConfigured = JavaMethod("(Landroid/hardware/camera2/CameraCaptureSession;)V")
        onConfigureFailed = JavaMethod("(Landroid/hardware/camera2/CameraCaptureSession;)V")

    class CaptureCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/camera2/CameraCaptureSession$CaptureCallback"
        __javaconstructor__ = [("()V", False)]
        onCaptureCompleted = JavaMethod("(Landroid/hardware/camera2/CameraCaptureSession;Landroid/hardware/camera2/CaptureRequest;Landroid/hardware/camera2/TotalCaptureResult;)V")
        onReadoutStarted = JavaMethod("(Landroid/hardware/camera2/CameraCaptureSession;Landroid/hardware/camera2/CaptureRequest;JJ)V")
        onCaptureBufferLost = JavaMethod("(Landroid/hardware/camera2/CameraCaptureSession;Landroid/hardware/camera2/CaptureRequest;Landroid/view/Surface;J)V")
        onCaptureProgressed = JavaMethod("(Landroid/hardware/camera2/CameraCaptureSession;Landroid/hardware/camera2/CaptureRequest;Landroid/hardware/camera2/CaptureResult;)V")
        onCaptureFailed = JavaMethod("(Landroid/hardware/camera2/CameraCaptureSession;Landroid/hardware/camera2/CaptureRequest;Landroid/hardware/camera2/CaptureFailure;)V")
        onCaptureSequenceAborted = JavaMethod("(Landroid/hardware/camera2/CameraCaptureSession;I)V")
        onCaptureSequenceCompleted = JavaMethod("(Landroid/hardware/camera2/CameraCaptureSession;IJ)V")
        onCaptureStarted = JavaMethod("(Landroid/hardware/camera2/CameraCaptureSession;Landroid/hardware/camera2/CaptureRequest;JJ)V")