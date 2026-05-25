from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MultiResolutionStreamConfigurationMap"]

class MultiResolutionStreamConfigurationMap(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/camera2/params/MultiResolutionStreamConfigurationMap"
    getOutputFormats = JavaMethod("()[I")
    getInputFormats = JavaMethod("()[I")
    getOutputInfo = JavaMethod("(I)Ljava/util/Collection;")
    getInputInfo = JavaMethod("(I)Ljava/util/Collection;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")