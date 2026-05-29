from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MultiResolutionStreamConfigurationMap"]

class MultiResolutionStreamConfigurationMap(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/camera2/params/MultiResolutionStreamConfigurationMap"
    getInputInfo = JavaMethod("(I)Ljava/util/Collection;")
    getOutputInfo = JavaMethod("(I)Ljava/util/Collection;")
    getInputFormats = JavaMethod("()[I")
    getOutputFormats = JavaMethod("()[I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")