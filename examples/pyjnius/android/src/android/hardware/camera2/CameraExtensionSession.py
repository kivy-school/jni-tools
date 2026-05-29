from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CameraExtensionSession"]

class CameraExtensionSession(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/camera2/CameraExtensionSession"
    stopRepeating = JavaMethod("()V")
    capture = JavaMethod("(Landroid/hardware/camera2/CaptureRequest;Ljava/util/concurrent/Executor;Landroid/hardware/camera2/CameraExtensionSession$ExtensionCaptureCallback;)I")
    getRealtimeStillCaptureLatency = JavaMethod("()Landroid/hardware/camera2/CameraExtensionSession$StillCaptureLatency;")
    setRepeatingRequest = JavaMethod("(Landroid/hardware/camera2/CaptureRequest;Ljava/util/concurrent/Executor;Landroid/hardware/camera2/CameraExtensionSession$ExtensionCaptureCallback;)I")
    close = JavaMethod("()V")
    getDevice = JavaMethod("()Landroid/hardware/camera2/CameraDevice;")

    class StillCaptureLatency(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/camera2/CameraExtensionSession$StillCaptureLatency"
        __javaconstructor__ = [("(JJ)V", False)]
        getCaptureLatency = JavaMethod("()J")
        getProcessingLatency = JavaMethod("()J")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        toString = JavaMethod("()Ljava/lang/String;")
        hashCode = JavaMethod("()I")

    class StateCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/camera2/CameraExtensionSession$StateCallback"
        __javaconstructor__ = [("()V", False)]
        onClosed = JavaMethod("(Landroid/hardware/camera2/CameraExtensionSession;)V")
        onConfigured = JavaMethod("(Landroid/hardware/camera2/CameraExtensionSession;)V")
        onConfigureFailed = JavaMethod("(Landroid/hardware/camera2/CameraExtensionSession;)V")

    class ExtensionCaptureCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/camera2/CameraExtensionSession$ExtensionCaptureCallback"
        __javaconstructor__ = [("()V", False)]
        onCaptureFailed = JavaMultipleMethod([("(Landroid/hardware/camera2/CameraExtensionSession;Landroid/hardware/camera2/CaptureRequest;I)V", False, False), ("(Landroid/hardware/camera2/CameraExtensionSession;Landroid/hardware/camera2/CaptureRequest;)V", False, False)])
        onCaptureProcessProgressed = JavaMethod("(Landroid/hardware/camera2/CameraExtensionSession;Landroid/hardware/camera2/CaptureRequest;I)V")
        onCaptureProcessStarted = JavaMethod("(Landroid/hardware/camera2/CameraExtensionSession;Landroid/hardware/camera2/CaptureRequest;)V")
        onCaptureResultAvailable = JavaMethod("(Landroid/hardware/camera2/CameraExtensionSession;Landroid/hardware/camera2/CaptureRequest;Landroid/hardware/camera2/TotalCaptureResult;)V")
        onCaptureSequenceAborted = JavaMethod("(Landroid/hardware/camera2/CameraExtensionSession;I)V")
        onCaptureSequenceCompleted = JavaMethod("(Landroid/hardware/camera2/CameraExtensionSession;I)V")
        onCaptureStarted = JavaMethod("(Landroid/hardware/camera2/CameraExtensionSession;Landroid/hardware/camera2/CaptureRequest;J)V")