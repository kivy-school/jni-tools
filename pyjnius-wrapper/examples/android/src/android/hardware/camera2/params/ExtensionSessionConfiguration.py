from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ExtensionSessionConfiguration"]

class ExtensionSessionConfiguration(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/camera2/params/ExtensionSessionConfiguration"
    __javaconstructor__ = [("(ILjava/util/List;Ljava/util/concurrent/Executor;Landroid/hardware/camera2/CameraExtensionSession$StateCallback;)V", False)]
    getExtension = JavaMethod("()I")
    setPostviewOutputConfiguration = JavaMethod("(Landroid/hardware/camera2/params/OutputConfiguration;)V")
    getPostviewOutputConfiguration = JavaMethod("()Landroid/hardware/camera2/params/OutputConfiguration;")
    getOutputConfigurations = JavaMethod("()Ljava/util/List;")
    getStateCallback = JavaMethod("()Landroid/hardware/camera2/CameraExtensionSession$StateCallback;")
    getExecutor = JavaMethod("()Ljava/util/concurrent/Executor;")
    setColorSpace = JavaMethod("(Landroid/graphics/ColorSpace$Named;)V")
    clearColorSpace = JavaMethod("()V")
    getColorSpace = JavaMethod("()Landroid/graphics/ColorSpace;")