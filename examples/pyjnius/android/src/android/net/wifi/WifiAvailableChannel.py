from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WifiAvailableChannel"]

class WifiAvailableChannel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/WifiAvailableChannel"
    __javaconstructor__ = [("(II)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    OP_MODE_SAP = JavaStaticField("I")
    OP_MODE_STA = JavaStaticField("I")
    OP_MODE_TDLS = JavaStaticField("I")
    OP_MODE_WIFI_AWARE = JavaStaticField("I")
    OP_MODE_WIFI_DIRECT_CLI = JavaStaticField("I")
    OP_MODE_WIFI_DIRECT_GO = JavaStaticField("I")
    getFrequencyMhz = JavaMethod("()I")
    getOperationalModes = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")