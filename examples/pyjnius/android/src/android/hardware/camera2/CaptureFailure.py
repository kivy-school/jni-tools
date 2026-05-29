from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CaptureFailure"]

class CaptureFailure(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/camera2/CaptureFailure"
    REASON_ERROR = JavaStaticField("I")
    REASON_FLUSHED = JavaStaticField("I")
    wasImageCaptured = JavaMethod("()Z")
    getFrameNumber = JavaMethod("()J")
    getRequest = JavaMethod("()Landroid/hardware/camera2/CaptureRequest;")
    getSequenceId = JavaMethod("()I")
    getPhysicalCameraId = JavaMethod("()Ljava/lang/String;")
    getReason = JavaMethod("()I")