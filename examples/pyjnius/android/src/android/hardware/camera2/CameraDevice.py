from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CameraDevice"]

class CameraDevice(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/camera2/CameraDevice"
    AUDIO_RESTRICTION_NONE = JavaStaticField("I")
    AUDIO_RESTRICTION_VIBRATION = JavaStaticField("I")
    AUDIO_RESTRICTION_VIBRATION_SOUND = JavaStaticField("I")
    TEMPLATE_MANUAL = JavaStaticField("I")
    TEMPLATE_PREVIEW = JavaStaticField("I")
    TEMPLATE_RECORD = JavaStaticField("I")
    TEMPLATE_STILL_CAPTURE = JavaStaticField("I")
    TEMPLATE_VIDEO_SNAPSHOT = JavaStaticField("I")
    TEMPLATE_ZERO_SHUTTER_LAG = JavaStaticField("I")
    createCaptureRequest = JavaMultipleMethod([("(I)Landroid/hardware/camera2/CaptureRequest$Builder;", False, False), ("(ILjava/util/Set;)Landroid/hardware/camera2/CaptureRequest$Builder;", False, False)])
    createCaptureSession = JavaMultipleMethod([("(Ljava/util/List;Landroid/hardware/camera2/CameraCaptureSession$StateCallback;Landroid/os/Handler;)V", False, False), ("(Landroid/hardware/camera2/params/SessionConfiguration;)V", False, False)])
    createCaptureSessionByOutputConfigurations = JavaMethod("(Ljava/util/List;Landroid/hardware/camera2/CameraCaptureSession$StateCallback;Landroid/os/Handler;)V")
    createConstrainedHighSpeedCaptureSession = JavaMethod("(Ljava/util/List;Landroid/hardware/camera2/CameraCaptureSession$StateCallback;Landroid/os/Handler;)V")
    createExtensionSession = JavaMethod("(Landroid/hardware/camera2/params/ExtensionSessionConfiguration;)V")
    createReprocessCaptureRequest = JavaMethod("(Landroid/hardware/camera2/TotalCaptureResult;)Landroid/hardware/camera2/CaptureRequest$Builder;")
    createReprocessableCaptureSession = JavaMethod("(Landroid/hardware/camera2/params/InputConfiguration;Ljava/util/List;Landroid/hardware/camera2/CameraCaptureSession$StateCallback;Landroid/os/Handler;)V")
    createReprocessableCaptureSessionByConfigurations = JavaMethod("(Landroid/hardware/camera2/params/InputConfiguration;Ljava/util/List;Landroid/hardware/camera2/CameraCaptureSession$StateCallback;Landroid/os/Handler;)V")
    getCameraAudioRestriction = JavaMethod("()I")
    isSessionConfigurationSupported = JavaMethod("(Landroid/hardware/camera2/params/SessionConfiguration;)Z")
    setCameraAudioRestriction = JavaMethod("(I)V")
    close = JavaMethod("()V")
    getId = JavaMethod("()Ljava/lang/String;")

    class StateCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/camera2/CameraDevice$StateCallback"
        __javaconstructor__ = [("()V", False)]
        ERROR_CAMERA_DEVICE = JavaStaticField("I")
        ERROR_CAMERA_DISABLED = JavaStaticField("I")
        ERROR_CAMERA_IN_USE = JavaStaticField("I")
        ERROR_CAMERA_SERVICE = JavaStaticField("I")
        ERROR_MAX_CAMERAS_IN_USE = JavaStaticField("I")
        onDisconnected = JavaMethod("(Landroid/hardware/camera2/CameraDevice;)V")
        onError = JavaMethod("(Landroid/hardware/camera2/CameraDevice;I)V")
        onClosed = JavaMethod("(Landroid/hardware/camera2/CameraDevice;)V")
        onOpened = JavaMethod("(Landroid/hardware/camera2/CameraDevice;)V")

    class CameraDeviceSetup(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/camera2/CameraDevice$CameraDeviceSetup"
        openCamera = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/hardware/camera2/CameraDevice$StateCallback;)V")
        getSessionCharacteristics = JavaMethod("(Landroid/hardware/camera2/params/SessionConfiguration;)Landroid/hardware/camera2/CameraCharacteristics;")
        createCaptureRequest = JavaMethod("(I)Landroid/hardware/camera2/CaptureRequest$Builder;")
        isSessionConfigurationSupported = JavaMethod("(Landroid/hardware/camera2/params/SessionConfiguration;)Z")
        getId = JavaMethod("()Ljava/lang/String;")