from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SessionConfiguration"]

class SessionConfiguration(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/camera2/params/SessionConfiguration"
    __javaconstructor__ = [("(ILjava/util/List;Ljava/util/concurrent/Executor;Landroid/hardware/camera2/CameraCaptureSession$StateCallback;)V", False), ("(ILjava/util/List;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    SESSION_HIGH_SPEED = JavaStaticField("I")
    SESSION_REGULAR = JavaStaticField("I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getSessionType = JavaMethod("()I")
    getOutputConfigurations = JavaMethod("()Ljava/util/List;")
    getStateCallback = JavaMethod("()Landroid/hardware/camera2/CameraCaptureSession$StateCallback;")
    getExecutor = JavaMethod("()Ljava/util/concurrent/Executor;")
    setInputConfiguration = JavaMethod("(Landroid/hardware/camera2/params/InputConfiguration;)V")
    getInputConfiguration = JavaMethod("()Landroid/hardware/camera2/params/InputConfiguration;")
    setSessionParameters = JavaMethod("(Landroid/hardware/camera2/CaptureRequest;)V")
    getSessionParameters = JavaMethod("()Landroid/hardware/camera2/CaptureRequest;")
    setColorSpace = JavaMethod("(Landroid/graphics/ColorSpace$Named;)V")
    clearColorSpace = JavaMethod("()V")
    getColorSpace = JavaMethod("()Landroid/graphics/ColorSpace;")
    setStateCallback = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/hardware/camera2/CameraCaptureSession$StateCallback;)V")