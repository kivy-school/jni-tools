from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CameraManager"]

class CameraManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/camera2/CameraManager"
    openCamera = JavaMultipleMethod([("(Ljava/lang/String;Landroid/hardware/camera2/CameraDevice$StateCallback;Landroid/os/Handler;)V", False, False), ("(Ljava/lang/String;Ljava/util/concurrent/Executor;Landroid/hardware/camera2/CameraDevice$StateCallback;)V", False, False)])
    setTorchMode = JavaMethod("(Ljava/lang/String;Z)V")
    getCameraCharacteristics = JavaMethod("(Ljava/lang/String;)Landroid/hardware/camera2/CameraCharacteristics;")
    getCameraIdList = JavaMethod("()[Ljava/lang/String;")
    getCameraDeviceSetup = JavaMethod("(Ljava/lang/String;)Landroid/hardware/camera2/CameraDevice$CameraDeviceSetup;")
    getCameraExtensionCharacteristics = JavaMethod("(Ljava/lang/String;)Landroid/hardware/camera2/CameraExtensionCharacteristics;")
    getConcurrentCameraIds = JavaMethod("()Ljava/util/Set;")
    getTorchStrengthLevel = JavaMethod("(Ljava/lang/String;)I")
    isCameraDeviceSetupSupported = JavaMethod("(Ljava/lang/String;)Z")
    isConcurrentSessionConfigurationSupported = JavaMethod("(Ljava/util/Map;)Z")
    registerAvailabilityCallback = JavaMultipleMethod([("(Ljava/util/concurrent/Executor;Landroid/hardware/camera2/CameraManager$AvailabilityCallback;)V", False, False), ("(Landroid/hardware/camera2/CameraManager$AvailabilityCallback;Landroid/os/Handler;)V", False, False)])
    registerTorchCallback = JavaMultipleMethod([("(Landroid/hardware/camera2/CameraManager$TorchCallback;Landroid/os/Handler;)V", False, False), ("(Ljava/util/concurrent/Executor;Landroid/hardware/camera2/CameraManager$TorchCallback;)V", False, False)])
    turnOnTorchWithStrengthLevel = JavaMethod("(Ljava/lang/String;I)V")
    unregisterAvailabilityCallback = JavaMethod("(Landroid/hardware/camera2/CameraManager$AvailabilityCallback;)V")
    unregisterTorchCallback = JavaMethod("(Landroid/hardware/camera2/CameraManager$TorchCallback;)V")

    class TorchCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/camera2/CameraManager$TorchCallback"
        __javaconstructor__ = [("()V", False)]
        onTorchModeChanged = JavaMethod("(Ljava/lang/String;Z)V")
        onTorchModeUnavailable = JavaMethod("(Ljava/lang/String;)V")
        onTorchStrengthLevelChanged = JavaMethod("(Ljava/lang/String;I)V")

    class AvailabilityCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/camera2/CameraManager$AvailabilityCallback"
        __javaconstructor__ = [("()V", False)]
        onCameraAvailable = JavaMethod("(Ljava/lang/String;)V")
        onCameraAccessPrioritiesChanged = JavaMethod("()V")
        onCameraUnavailable = JavaMethod("(Ljava/lang/String;)V")
        onPhysicalCameraAvailable = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
        onPhysicalCameraUnavailable = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")