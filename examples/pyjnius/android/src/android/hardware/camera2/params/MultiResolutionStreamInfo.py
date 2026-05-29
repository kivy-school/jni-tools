from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MultiResolutionStreamInfo"]

class MultiResolutionStreamInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/camera2/params/MultiResolutionStreamInfo"
    __javaconstructor__ = [("(IILjava/lang/String;)V", False)]
    getWidth = JavaMethod("()I")
    getHeight = JavaMethod("()I")
    getPhysicalCameraId = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")