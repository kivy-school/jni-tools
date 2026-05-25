from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ConsumerIrManager"]

class ConsumerIrManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/ConsumerIrManager"
    hasIrEmitter = JavaMethod("()Z")
    transmit = JavaMethod("(I[I)V")
    getCarrierFrequencies = JavaMethod("()[Landroid/hardware/ConsumerIrManager$CarrierFrequencyRange;")

    class CarrierFrequencyRange(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/ConsumerIrManager/CarrierFrequencyRange"
        __javaconstructor__ = [("(Landroid/hardware/ConsumerIrManager;II)V", False)]
        getMinFrequency = JavaMethod("()I")
        getMaxFrequency = JavaMethod("()I")