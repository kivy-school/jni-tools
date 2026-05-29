from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ConsumerIrManager"]

class ConsumerIrManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/ConsumerIrManager"
    transmit = JavaMethod("(I[I)V")
    hasIrEmitter = JavaMethod("()Z")
    getCarrierFrequencies = JavaMethod("()[Landroid/hardware/ConsumerIrManager$CarrierFrequencyRange;")

    class CarrierFrequencyRange(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/ConsumerIrManager$CarrierFrequencyRange"
        __javaconstructor__ = [("(Landroid/hardware/ConsumerIrManager;II)V", False)]
        getMaxFrequency = JavaMethod("()I")
        getMinFrequency = JavaMethod("()I")