from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PeriodicAdvertisingParameters"]

class PeriodicAdvertisingParameters(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/bluetooth/le/PeriodicAdvertisingParameters"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getIncludeTxPower = JavaMethod("()Z")
    getInterval = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/bluetooth/le/PeriodicAdvertisingParameters/Builder"
        __javaconstructor__ = [("()V", False)]
        setIncludeTxPower = JavaMethod("(Z)Landroid/bluetooth/le/PeriodicAdvertisingParameters$Builder;")
        setInterval = JavaMethod("(I)Landroid/bluetooth/le/PeriodicAdvertisingParameters$Builder;")
        build = JavaMethod("()Landroid/bluetooth/le/PeriodicAdvertisingParameters;")