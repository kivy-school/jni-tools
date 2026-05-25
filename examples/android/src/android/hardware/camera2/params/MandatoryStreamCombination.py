from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MandatoryStreamCombination"]

class MandatoryStreamCombination(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/camera2/params/MandatoryStreamCombination"
    getDescription = JavaMethod("()Ljava/lang/CharSequence;")
    isReprocessable = JavaMethod("()Z")
    getStreamsInformation = JavaMethod("()Ljava/util/List;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class MandatoryStreamInformation(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/camera2/params/MandatoryStreamCombination/MandatoryStreamInformation"
        isInput = JavaMethod("()Z")
        isUltraHighResolution = JavaMethod("()Z")
        isMaximumSize = JavaMethod("()Z")
        is10BitCapable = JavaMethod("()Z")
        getAvailableSizes = JavaMethod("()Ljava/util/List;")
        getFormat = JavaMethod("()I")
        get10BitFormat = JavaMethod("()I")
        getStreamUseCase = JavaMethod("()J")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")