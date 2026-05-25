from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CameraManager"]

class CameraManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/camera2/CameraManager"
    getCameraIdList = JavaMethod("()[Ljava/lang/String;")
    getConcurrentCameraIds = JavaMethod("()Ljava/util/Set;")
    isConcurrentSessionConfigurationSupported = JavaMethod("(Ljava/util/Map;)Z")
    registerAvailabilityCallback = JavaMultipleMethod([("(Landroid/hardware/camera2/CameraManager$AvailabilityCallback;Landroid/os/Handler;)V", False, False), ("(Ljava/util/concurrent/Executor;Landroid/hardware/camera2/CameraManager$AvailabilityCallback;)V", False, False)])
    unregisterAvailabilityCallback = JavaMethod("(Landroid/hardware/camera2/CameraManager$AvailabilityCallback;)V")
    registerTorchCallback = JavaMultipleMethod([("(Landroid/hardware/camera2/CameraManager$TorchCallback;Landroid/os/Handler;)V", False, False), ("(Ljava/util/concurrent/Executor;Landroid/hardware/camera2/CameraManager$TorchCallback;)V", False, False)])
    unregisterTorchCallback = JavaMethod("(Landroid/hardware/camera2/CameraManager$TorchCallback;)V")
    getCameraCharacteristics = JavaMethod("(Ljava/lang/String;)Landroid/hardware/camera2/CameraCharacteristics;")
    getCameraExtensionCharacteristics = JavaMethod("(Ljava/lang/String;)Landroid/hardware/camera2/CameraExtensionCharacteristics;")
    getCameraDeviceSetup = JavaMethod("(Ljava/lang/String;)Landroid/hardware/camera2/CameraDevice$CameraDeviceSetup;")
    isCameraDeviceSetupSupported = JavaMethod("(Ljava/lang/String;)Z")
    openCamera = JavaMultipleMethod([("(Ljava/lang/String;Landroid/hardware/camera2/CameraDevice$StateCallback;Landroid/os/Handler;)V", False, False), ("(Ljava/lang/String;Ljava/util/concurrent/Executor;Landroid/hardware/camera2/CameraDevice$StateCallback;)V", False, False)])
    setTorchMode = JavaMethod("(Ljava/lang/String;Z)V")
    turnOnTorchWithStrengthLevel = JavaMethod("(Ljava/lang/String;I)V")
    getTorchStrengthLevel = JavaMethod("(Ljava/lang/String;)I")

    class AvailabilityCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/camera2/CameraManager/AvailabilityCallback"
        __javaconstructor__ = [("()V", False)]
        onCameraAvailable = JavaMethod("(Ljava/lang/String;)V")
        onCameraUnavailable = JavaMethod("(Ljava/lang/String;)V")
        onCameraAccessPrioritiesChanged = JavaMethod("()V")
        onPhysicalCameraAvailable = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
        onPhysicalCameraUnavailable = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")

    class TorchCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/camera2/CameraManager/TorchCallback"
        __javaconstructor__ = [("()V", False)]
        onTorchModeUnavailable = JavaMethod("(Ljava/lang/String;)V")
        onTorchModeChanged = JavaMethod("(Ljava/lang/String;Z)V")
        onTorchStrengthLevelChanged = JavaMethod("(Ljava/lang/String;I)V")