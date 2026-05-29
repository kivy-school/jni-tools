from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SoftApConfiguration"]

class SoftApConfiguration(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/SoftApConfiguration"
    BAND_2GHZ = JavaStaticField("I")
    BAND_5GHZ = JavaStaticField("I")
    BAND_60GHZ = JavaStaticField("I")
    BAND_6GHZ = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    SECURITY_TYPE_OPEN = JavaStaticField("I")
    SECURITY_TYPE_WPA2_PSK = JavaStaticField("I")
    SECURITY_TYPE_WPA3_OWE = JavaStaticField("I")
    SECURITY_TYPE_WPA3_OWE_TRANSITION = JavaStaticField("I")
    SECURITY_TYPE_WPA3_SAE = JavaStaticField("I")
    SECURITY_TYPE_WPA3_SAE_TRANSITION = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getChannels = JavaMethod("()Landroid/util/SparseIntArray;")
    getWifiSsid = JavaMethod("()Landroid/net/wifi/WifiSsid;")
    getBssid = JavaMethod("()Landroid/net/MacAddress;")
    getPassphrase = JavaMethod("()Ljava/lang/String;")
    getSecurityType = JavaMethod("()I")
    getSsid = JavaMethod("()Ljava/lang/String;")
    isHiddenSsid = JavaMethod("()Z")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/wifi/SoftApConfiguration$Builder"
        __javaconstructor__ = [("()V", False)]
        setChannels = JavaMethod("(Landroid/util/SparseIntArray;)Landroid/net/wifi/SoftApConfiguration$Builder;")
        build = JavaMethod("()Landroid/net/wifi/SoftApConfiguration;")