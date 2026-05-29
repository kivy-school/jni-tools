from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

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
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getTimeout = JavaMethod("()I")
    isConnectable = JavaMethod("()Z")
    getTxPowerLevel = JavaMethod("()I")
    isDiscoverable = JavaMethod("()Z")
    toString = JavaMethod("()Ljava/lang/String;")
    getMode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/bluetooth/le/AdvertiseSettings$Builder"
        __javaconstructor__ = [("()V", False)]
        setTimeout = JavaMethod("(I)Landroid/bluetooth/le/AdvertiseSettings$Builder;")
        setAdvertiseMode = JavaMethod("(I)Landroid/bluetooth/le/AdvertiseSettings$Builder;")
        setConnectable = JavaMethod("(Z)Landroid/bluetooth/le/AdvertiseSettings$Builder;")
        setDiscoverable = JavaMethod("(Z)Landroid/bluetooth/le/AdvertiseSettings$Builder;")
        setTxPowerLevel = JavaMethod("(I)Landroid/bluetooth/le/AdvertiseSettings$Builder;")
        build = JavaMethod("()Landroid/bluetooth/le/AdvertiseSettings;")