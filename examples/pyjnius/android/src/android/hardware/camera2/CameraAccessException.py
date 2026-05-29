from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CameraAccessException"]

class CameraAccessException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/camera2/CameraAccessException"
    __javaconstructor__ = [("(I)V", False), ("(ILjava/lang/String;)V", False), ("(ILjava/lang/String;Ljava/lang/Throwable;)V", False), ("(ILjava/lang/Throwable;)V", False)]
    CAMERA_DISABLED = JavaStaticField("I")
    CAMERA_DISCONNECTED = JavaStaticField("I")
    CAMERA_ERROR = JavaStaticField("I")
    CAMERA_IN_USE = JavaStaticField("I")
    MAX_CAMERAS_IN_USE = JavaStaticField("I")
    getReason = JavaMethod("()I")