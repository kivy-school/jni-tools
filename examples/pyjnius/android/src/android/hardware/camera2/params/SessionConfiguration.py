from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SessionConfiguration"]

class SessionConfiguration(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/camera2/params/SessionConfiguration"
    __javaconstructor__ = [("(ILjava/util/List;)V", False), ("(ILjava/util/List;Ljava/util/concurrent/Executor;Landroid/hardware/camera2/CameraCaptureSession$StateCallback;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    SESSION_HIGH_SPEED = JavaStaticField("I")
    SESSION_REGULAR = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    clearColorSpace = JavaMethod("()V")
    getExecutor = JavaMethod("()Ljava/util/concurrent/Executor;")
    getInputConfiguration = JavaMethod("()Landroid/hardware/camera2/params/InputConfiguration;")
    getOutputConfigurations = JavaMethod("()Ljava/util/List;")
    getSessionParameters = JavaMethod("()Landroid/hardware/camera2/CaptureRequest;")
    getSessionType = JavaMethod("()I")
    getStateCallback = JavaMethod("()Landroid/hardware/camera2/CameraCaptureSession$StateCallback;")
    setInputConfiguration = JavaMethod("(Landroid/hardware/camera2/params/InputConfiguration;)V")
    setSessionParameters = JavaMethod("(Landroid/hardware/camera2/CaptureRequest;)V")
    setStateCallback = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/hardware/camera2/CameraCaptureSession$StateCallback;)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    setColorSpace = JavaMethod("(Landroid/graphics/ColorSpace$Named;)V")
    getColorSpace = JavaMethod("()Landroid/graphics/ColorSpace;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")