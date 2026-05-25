from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CameraConstrainedHighSpeedCaptureSession"]

class CameraConstrainedHighSpeedCaptureSession(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/camera2/CameraConstrainedHighSpeedCaptureSession"
    __javaconstructor__ = [("()V", False)]
    createHighSpeedRequestList = JavaMethod("(Landroid/hardware/camera2/CaptureRequest;)Ljava/util/List;")