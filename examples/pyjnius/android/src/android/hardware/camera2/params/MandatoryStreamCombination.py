from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MandatoryStreamCombination"]

class MandatoryStreamCombination(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/camera2/params/MandatoryStreamCombination"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    isReprocessable = JavaMethod("()Z")
    getStreamsInformation = JavaMethod("()Ljava/util/List;")
    getDescription = JavaMethod("()Ljava/lang/CharSequence;")

    class MandatoryStreamInformation(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/camera2/params/MandatoryStreamCombination$MandatoryStreamInformation"
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")
        get10BitFormat = JavaMethod("()I")
        getAvailableSizes = JavaMethod("()Ljava/util/List;")
        is10BitCapable = JavaMethod("()Z")
        isInput = JavaMethod("()Z")
        isMaximumSize = JavaMethod("()Z")
        isUltraHighResolution = JavaMethod("()Z")
        getStreamUseCase = JavaMethod("()J")
        getFormat = JavaMethod("()I")