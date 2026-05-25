from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AwarePairingConfig"]

class AwarePairingConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/aware/AwarePairingConfig"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    PAIRING_BOOTSTRAPPING_NFC_READER = JavaStaticField("I")
    PAIRING_BOOTSTRAPPING_NFC_TAG = JavaStaticField("I")
    PAIRING_BOOTSTRAPPING_OPPORTUNISTIC = JavaStaticField("I")
    PAIRING_BOOTSTRAPPING_PASSPHRASE_DISPLAY = JavaStaticField("I")
    PAIRING_BOOTSTRAPPING_PASSPHRASE_KEYPAD = JavaStaticField("I")
    PAIRING_BOOTSTRAPPING_PIN_CODE_DISPLAY = JavaStaticField("I")
    PAIRING_BOOTSTRAPPING_PIN_CODE_KEYPAD = JavaStaticField("I")
    PAIRING_BOOTSTRAPPING_QR_DISPLAY = JavaStaticField("I")
    PAIRING_BOOTSTRAPPING_QR_SCAN = JavaStaticField("I")
    isPairingCacheEnabled = JavaMethod("()Z")
    isPairingSetupEnabled = JavaMethod("()Z")
    isPairingVerificationEnabled = JavaMethod("()Z")
    getBootstrappingMethods = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/wifi/aware/AwarePairingConfig/Builder"
        __javaconstructor__ = [("()V", False)]
        setPairingSetupEnabled = JavaMethod("(Z)Landroid/net/wifi/aware/AwarePairingConfig$Builder;")
        setPairingVerificationEnabled = JavaMethod("(Z)Landroid/net/wifi/aware/AwarePairingConfig$Builder;")
        setPairingCacheEnabled = JavaMethod("(Z)Landroid/net/wifi/aware/AwarePairingConfig$Builder;")
        setBootstrappingMethods = JavaMethod("(I)Landroid/net/wifi/aware/AwarePairingConfig$Builder;")
        build = JavaMethod("()Landroid/net/wifi/aware/AwarePairingConfig;")