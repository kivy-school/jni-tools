from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CameraCaptureSession"]

class CameraCaptureSession(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/camera2/CameraCaptureSession"
    __javaconstructor__ = [("()V", False)]
    getDevice = JavaMethod("()Landroid/hardware/camera2/CameraDevice;")
    prepare = JavaMethod("(Landroid/view/Surface;)V")
    finalizeOutputConfigurations = JavaMethod("(Ljava/util/List;)V")
    capture = JavaMethod("(Landroid/hardware/camera2/CaptureRequest;Landroid/hardware/camera2/CameraCaptureSession$CaptureCallback;Landroid/os/Handler;)I")
    captureSingleRequest = JavaMethod("(Landroid/hardware/camera2/CaptureRequest;Ljava/util/concurrent/Executor;Landroid/hardware/camera2/CameraCaptureSession$CaptureCallback;)I")
    captureBurst = JavaMethod("(Ljava/util/List;Landroid/hardware/camera2/CameraCaptureSession$CaptureCallback;Landroid/os/Handler;)I")
    captureBurstRequests = JavaMethod("(Ljava/util/List;Ljava/util/concurrent/Executor;Landroid/hardware/camera2/CameraCaptureSession$CaptureCallback;)I")
    setRepeatingRequest = JavaMethod("(Landroid/hardware/camera2/CaptureRequest;Landroid/hardware/camera2/CameraCaptureSession$CaptureCallback;Landroid/os/Handler;)I")
    setSingleRepeatingRequest = JavaMethod("(Landroid/hardware/camera2/CaptureRequest;Ljava/util/concurrent/Executor;Landroid/hardware/camera2/CameraCaptureSession$CaptureCallback;)I")
    setRepeatingBurst = JavaMethod("(Ljava/util/List;Landroid/hardware/camera2/CameraCaptureSession$CaptureCallback;Landroid/os/Handler;)I")
    setRepeatingBurstRequests = JavaMethod("(Ljava/util/List;Ljava/util/concurrent/Executor;Landroid/hardware/camera2/CameraCaptureSession$CaptureCallback;)I")
    stopRepeating = JavaMethod("()V")
    abortCaptures = JavaMethod("()V")
    isReprocessable = JavaMethod("()Z")
    getInputSurface = JavaMethod("()Landroid/view/Surface;")
    updateOutputConfiguration = JavaMethod("(Landroid/hardware/camera2/params/OutputConfiguration;)V")
    switchToOffline = JavaMethod("(Ljava/util/Collection;Ljava/util/concurrent/Executor;Landroid/hardware/camera2/CameraOfflineSession$CameraOfflineSessionCallback;)Landroid/hardware/camera2/CameraOfflineSession;")
    supportsOfflineProcessing = JavaMethod("(Landroid/view/Surface;)Z")
    close = JavaMethod("()V")

    class CaptureCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/camera2/CameraCaptureSession/CaptureCallback"
        __javaconstructor__ = [("()V", False)]
        onCaptureStarted = JavaMethod("(Landroid/hardware/camera2/CameraCaptureSession;Landroid/hardware/camera2/CaptureRequest;JJ)V")
        onReadoutStarted = JavaMethod("(Landroid/hardware/camera2/CameraCaptureSession;Landroid/hardware/camera2/CaptureRequest;JJ)V")
        onCaptureProgressed = JavaMethod("(Landroid/hardware/camera2/CameraCaptureSession;Landroid/hardware/camera2/CaptureRequest;Landroid/hardware/camera2/CaptureResult;)V")
        onCaptureCompleted = JavaMethod("(Landroid/hardware/camera2/CameraCaptureSession;Landroid/hardware/camera2/CaptureRequest;Landroid/hardware/camera2/TotalCaptureResult;)V")
        onCaptureFailed = JavaMethod("(Landroid/hardware/camera2/CameraCaptureSession;Landroid/hardware/camera2/CaptureRequest;Landroid/hardware/camera2/CaptureFailure;)V")
        onCaptureSequenceCompleted = JavaMethod("(Landroid/hardware/camera2/CameraCaptureSession;IJ)V")
        onCaptureSequenceAborted = JavaMethod("(Landroid/hardware/camera2/CameraCaptureSession;I)V")
        onCaptureBufferLost = JavaMethod("(Landroid/hardware/camera2/CameraCaptureSession;Landroid/hardware/camera2/CaptureRequest;Landroid/view/Surface;J)V")

    class StateCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/camera2/CameraCaptureSession/StateCallback"
        __javaconstructor__ = [("()V", False)]
        onConfigured = JavaMethod("(Landroid/hardware/camera2/CameraCaptureSession;)V")
        onConfigureFailed = JavaMethod("(Landroid/hardware/camera2/CameraCaptureSession;)V")
        onReady = JavaMethod("(Landroid/hardware/camera2/CameraCaptureSession;)V")
        onActive = JavaMethod("(Landroid/hardware/camera2/CameraCaptureSession;)V")
        onCaptureQueueEmpty = JavaMethod("(Landroid/hardware/camera2/CameraCaptureSession;)V")
        onClosed = JavaMethod("(Landroid/hardware/camera2/CameraCaptureSession;)V")
        onSurfacePrepared = JavaMethod("(Landroid/hardware/camera2/CameraCaptureSession;Landroid/view/Surface;)V")