from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ExtensionSessionConfiguration"]

class ExtensionSessionConfiguration(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/camera2/params/ExtensionSessionConfiguration"
    __javaconstructor__ = [("(ILjava/util/List;Ljava/util/concurrent/Executor;Landroid/hardware/camera2/CameraExtensionSession$StateCallback;)V", False)]
    clearColorSpace = JavaMethod("()V")
    getExecutor = JavaMethod("()Ljava/util/concurrent/Executor;")
    getOutputConfigurations = JavaMethod("()Ljava/util/List;")
    getStateCallback = JavaMethod("()Landroid/hardware/camera2/CameraExtensionSession$StateCallback;")
    getPostviewOutputConfiguration = JavaMethod("()Landroid/hardware/camera2/params/OutputConfiguration;")
    setPostviewOutputConfiguration = JavaMethod("(Landroid/hardware/camera2/params/OutputConfiguration;)V")
    setColorSpace = JavaMethod("(Landroid/graphics/ColorSpace$Named;)V")
    getColorSpace = JavaMethod("()Landroid/graphics/ColorSpace;")
    getExtension = JavaMethod("()I")