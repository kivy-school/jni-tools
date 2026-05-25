from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CameraExtensionSession"]

class CameraExtensionSession(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/camera2/CameraExtensionSession"
    getDevice = JavaMethod("()Landroid/hardware/camera2/CameraDevice;")
    capture = JavaMethod("(Landroid/hardware/camera2/CaptureRequest;Ljava/util/concurrent/Executor;Landroid/hardware/camera2/CameraExtensionSession$ExtensionCaptureCallback;)I")
    setRepeatingRequest = JavaMethod("(Landroid/hardware/camera2/CaptureRequest;Ljava/util/concurrent/Executor;Landroid/hardware/camera2/CameraExtensionSession$ExtensionCaptureCallback;)I")
    stopRepeating = JavaMethod("()V")
    getRealtimeStillCaptureLatency = JavaMethod("()Landroid/hardware/camera2/CameraExtensionSession$StillCaptureLatency;")
    close = JavaMethod("()V")

    class ExtensionCaptureCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/camera2/CameraExtensionSession/ExtensionCaptureCallback"
        __javaconstructor__ = [("()V", False)]
        onCaptureStarted = JavaMethod("(Landroid/hardware/camera2/CameraExtensionSession;Landroid/hardware/camera2/CaptureRequest;J)V")
        onCaptureProcessStarted = JavaMethod("(Landroid/hardware/camera2/CameraExtensionSession;Landroid/hardware/camera2/CaptureRequest;)V")
        onCaptureFailed = JavaMultipleMethod([("(Landroid/hardware/camera2/CameraExtensionSession;Landroid/hardware/camera2/CaptureRequest;)V", False, False), ("(Landroid/hardware/camera2/CameraExtensionSession;Landroid/hardware/camera2/CaptureRequest;I)V", False, False)])
        onCaptureSequenceCompleted = JavaMethod("(Landroid/hardware/camera2/CameraExtensionSession;I)V")
        onCaptureSequenceAborted = JavaMethod("(Landroid/hardware/camera2/CameraExtensionSession;I)V")
        onCaptureResultAvailable = JavaMethod("(Landroid/hardware/camera2/CameraExtensionSession;Landroid/hardware/camera2/CaptureRequest;Landroid/hardware/camera2/TotalCaptureResult;)V")
        onCaptureProcessProgressed = JavaMethod("(Landroid/hardware/camera2/CameraExtensionSession;Landroid/hardware/camera2/CaptureRequest;I)V")

    class StateCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/camera2/CameraExtensionSession/StateCallback"
        __javaconstructor__ = [("()V", False)]
        onConfigured = JavaMethod("(Landroid/hardware/camera2/CameraExtensionSession;)V")
        onConfigureFailed = JavaMethod("(Landroid/hardware/camera2/CameraExtensionSession;)V")
        onClosed = JavaMethod("(Landroid/hardware/camera2/CameraExtensionSession;)V")

    class StillCaptureLatency(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/camera2/CameraExtensionSession/StillCaptureLatency"
        __javaconstructor__ = [("(JJ)V", False)]
        getCaptureLatency = JavaMethod("()J")
        getProcessingLatency = JavaMethod("()J")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")
        toString = JavaMethod("()Ljava/lang/String;")