from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PasnConfig"]

class PasnConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/rtt/PasnConfig"
    AKM_FILS_EAP_SHA256 = JavaStaticField("I")
    AKM_FILS_EAP_SHA384 = JavaStaticField("I")
    AKM_FT_EAP_SHA256 = JavaStaticField("I")
    AKM_FT_EAP_SHA384 = JavaStaticField("I")
    AKM_FT_PSK_SHA256 = JavaStaticField("I")
    AKM_FT_PSK_SHA384 = JavaStaticField("I")
    AKM_NONE = JavaStaticField("I")
    AKM_PASN = JavaStaticField("I")
    AKM_SAE = JavaStaticField("I")
    CIPHER_CCMP_128 = JavaStaticField("I")
    CIPHER_CCMP_256 = JavaStaticField("I")
    CIPHER_GCMP_128 = JavaStaticField("I")
    CIPHER_GCMP_256 = JavaStaticField("I")
    CIPHER_NONE = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getPassword = JavaMethod("()Ljava/lang/String;")
    getWifiSsid = JavaMethod("()Landroid/net/wifi/WifiSsid;")
    getBaseAkms = JavaMethod("()I")
    getCiphers = JavaMethod("()I")
    getPasnComebackCookie = JavaMethod("()[B")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/wifi/rtt/PasnConfig$Builder"
        __javaconstructor__ = [("(II)V", False)]
        setPasnComebackCookie = JavaMethod("([B)Landroid/net/wifi/rtt/PasnConfig$Builder;")
        setPassword = JavaMethod("(Ljava/lang/String;)Landroid/net/wifi/rtt/PasnConfig$Builder;")
        build = JavaMethod("()Landroid/net/wifi/rtt/PasnConfig;")
        setWifiSsid = JavaMethod("(Landroid/net/wifi/WifiSsid;)Landroid/net/wifi/rtt/PasnConfig$Builder;")