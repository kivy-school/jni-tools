from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SoftApConfiguration"]

class SoftApConfiguration(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/SoftApConfiguration"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    SECURITY_TYPE_OPEN = JavaStaticField("I")
    SECURITY_TYPE_WPA2_PSK = JavaStaticField("I")
    SECURITY_TYPE_WPA3_OWE = JavaStaticField("I")
    SECURITY_TYPE_WPA3_OWE_TRANSITION = JavaStaticField("I")
    SECURITY_TYPE_WPA3_SAE = JavaStaticField("I")
    SECURITY_TYPE_WPA3_SAE_TRANSITION = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getSsid = JavaMethod("()Ljava/lang/String;")
    getWifiSsid = JavaMethod("()Landroid/net/wifi/WifiSsid;")
    getBssid = JavaMethod("()Landroid/net/MacAddress;")
    getPassphrase = JavaMethod("()Ljava/lang/String;")
    isHiddenSsid = JavaMethod("()Z")
    getSecurityType = JavaMethod("()I")