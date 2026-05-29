from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdvertisingSetParameters"]

class AdvertisingSetParameters(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/bluetooth/le/AdvertisingSetParameters"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    INTERVAL_HIGH = JavaStaticField("I")
    INTERVAL_LOW = JavaStaticField("I")
    INTERVAL_MAX = JavaStaticField("I")
    INTERVAL_MEDIUM = JavaStaticField("I")
    INTERVAL_MIN = JavaStaticField("I")
    TX_POWER_HIGH = JavaStaticField("I")
    TX_POWER_LOW = JavaStaticField("I")
    TX_POWER_MAX = JavaStaticField("I")
    TX_POWER_MEDIUM = JavaStaticField("I")
    TX_POWER_MIN = JavaStaticField("I")
    TX_POWER_ULTRA_LOW = JavaStaticField("I")
    isConnectable = JavaMethod("()Z")
    isDiscoverable = JavaMethod("()Z")
    isScannable = JavaMethod("()Z")
    isLegacy = JavaMethod("()Z")
    isAnonymous = JavaMethod("()Z")
    includeTxPower = JavaMethod("()Z")
    getPrimaryPhy = JavaMethod("()I")
    getSecondaryPhy = JavaMethod("()I")
    getInterval = JavaMethod("()I")
    getTxPowerLevel = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/bluetooth/le/AdvertisingSetParameters/Builder"
        __javaconstructor__ = [("()V", False)]
        setConnectable = JavaMethod("(Z)Landroid/bluetooth/le/AdvertisingSetParameters$Builder;")
        setDiscoverable = JavaMethod("(Z)Landroid/bluetooth/le/AdvertisingSetParameters$Builder;")
        setScannable = JavaMethod("(Z)Landroid/bluetooth/le/AdvertisingSetParameters$Builder;")
        setLegacyMode = JavaMethod("(Z)Landroid/bluetooth/le/AdvertisingSetParameters$Builder;")
        setAnonymous = JavaMethod("(Z)Landroid/bluetooth/le/AdvertisingSetParameters$Builder;")
        setIncludeTxPower = JavaMethod("(Z)Landroid/bluetooth/le/AdvertisingSetParameters$Builder;")
        setPrimaryPhy = JavaMethod("(I)Landroid/bluetooth/le/AdvertisingSetParameters$Builder;")
        setSecondaryPhy = JavaMethod("(I)Landroid/bluetooth/le/AdvertisingSetParameters$Builder;")
        setInterval = JavaMethod("(I)Landroid/bluetooth/le/AdvertisingSetParameters$Builder;")
        setTxPowerLevel = JavaMethod("(I)Landroid/bluetooth/le/AdvertisingSetParameters$Builder;")
        build = JavaMethod("()Landroid/bluetooth/le/AdvertisingSetParameters;")