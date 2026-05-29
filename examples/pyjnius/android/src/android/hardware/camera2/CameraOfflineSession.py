from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CameraOfflineSession"]

class CameraOfflineSession(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/camera2/CameraOfflineSession"
    __javaconstructor__ = [("()V", False)]
    close = JavaMethod("()V")

    class CameraOfflineSessionCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/camera2/CameraOfflineSession/CameraOfflineSessionCallback"
        __javaconstructor__ = [("()V", False)]
        STATUS_INTERNAL_ERROR = JavaStaticField("I")
        onReady = JavaMethod("(Landroid/hardware/camera2/CameraOfflineSession;)V")
        onSwitchFailed = JavaMethod("(Landroid/hardware/camera2/CameraOfflineSession;)V")
        onIdle = JavaMethod("(Landroid/hardware/camera2/CameraOfflineSession;)V")
        onError = JavaMethod("(Landroid/hardware/camera2/CameraOfflineSession;I)V")
        onClosed = JavaMethod("(Landroid/hardware/camera2/CameraOfflineSession;)V")