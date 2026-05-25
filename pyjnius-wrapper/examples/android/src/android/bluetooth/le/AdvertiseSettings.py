from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdvertiseSettings"]

class AdvertiseSettings(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/bluetooth/le/AdvertiseSettings"
    ADVERTISE_MODE_BALANCED = JavaStaticField("I")
    ADVERTISE_MODE_LOW_LATENCY = JavaStaticField("I")
    ADVERTISE_MODE_LOW_POWER = JavaStaticField("I")
    ADVERTISE_TX_POWER_HIGH = JavaStaticField("I")
    ADVERTISE_TX_POWER_LOW = JavaStaticField("I")
    ADVERTISE_TX_POWER_MEDIUM = JavaStaticField("I")
    ADVERTISE_TX_POWER_ULTRA_LOW = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getMode = JavaMethod("()I")
    getTxPowerLevel = JavaMethod("()I")
    isConnectable = JavaMethod("()Z")
    isDiscoverable = JavaMethod("()Z")
    getTimeout = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/bluetooth/le/AdvertiseSettings/Builder"
        __javaconstructor__ = [("()V", False)]
        setAdvertiseMode = JavaMethod("(I)Landroid/bluetooth/le/AdvertiseSettings$Builder;")
        setTxPowerLevel = JavaMethod("(I)Landroid/bluetooth/le/AdvertiseSettings$Builder;")
        setConnectable = JavaMethod("(Z)Landroid/bluetooth/le/AdvertiseSettings$Builder;")
        setDiscoverable = JavaMethod("(Z)Landroid/bluetooth/le/AdvertiseSettings$Builder;")
        setTimeout = JavaMethod("(I)Landroid/bluetooth/le/AdvertiseSettings$Builder;")
        build = JavaMethod("()Landroid/bluetooth/le/AdvertiseSettings;")