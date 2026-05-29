from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WifiP2pPairingBootstrappingConfig"]

class WifiP2pPairingBootstrappingConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/p2p/WifiP2pPairingBootstrappingConfig"
    __javaconstructor__ = [("(ILjava/lang/String;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    PAIRING_BOOTSTRAPPING_METHOD_DISPLAY_PASSPHRASE = JavaStaticField("I")
    PAIRING_BOOTSTRAPPING_METHOD_DISPLAY_PINCODE = JavaStaticField("I")
    PAIRING_BOOTSTRAPPING_METHOD_KEYPAD_PASSPHRASE = JavaStaticField("I")
    PAIRING_BOOTSTRAPPING_METHOD_KEYPAD_PINCODE = JavaStaticField("I")
    PAIRING_BOOTSTRAPPING_METHOD_OPPORTUNISTIC = JavaStaticField("I")
    PAIRING_BOOTSTRAPPING_METHOD_OUT_OF_BAND = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")