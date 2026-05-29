from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

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
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getOperationalModes = JavaMethod("()I")
    getChannelWidth = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getFrequencyMhz = JavaMethod("()I")