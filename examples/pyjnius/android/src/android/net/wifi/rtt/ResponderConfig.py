from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ResponderConfig"]

class ResponderConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/rtt/ResponderConfig"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    RESPONDER_AP = JavaStaticField("I")
    RESPONDER_STA = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getMacAddress = JavaMethod("()Landroid/net/MacAddress;")
    fromScanResult = JavaStaticMethod("(Landroid/net/wifi/ScanResult;)Landroid/net/wifi/rtt/ResponderConfig;")
    getCenterFreq0Mhz = JavaMethod("()I")
    getCenterFreq1Mhz = JavaMethod("()I")
    getChannelWidth = JavaMethod("()I")
    getPreamble = JavaMethod("()I")
    getResponderType = JavaMethod("()I")
    getSecureRangingConfig = JavaMethod("()Landroid/net/wifi/rtt/SecureRangingConfig;")
    is80211azNtbSupported = JavaMethod("()Z")
    is80211mcSupported = JavaMethod("()Z")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getFrequencyMhz = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/wifi/rtt/ResponderConfig$Builder"
        __javaconstructor__ = [("()V", False)]
        setMacAddress = JavaMethod("(Landroid/net/MacAddress;)Landroid/net/wifi/rtt/ResponderConfig$Builder;")
        setCenterFreq1Mhz = JavaMethod("(I)Landroid/net/wifi/rtt/ResponderConfig$Builder;")
        setResponderType = JavaMethod("(I)Landroid/net/wifi/rtt/ResponderConfig$Builder;")
        setPreamble = JavaMethod("(I)Landroid/net/wifi/rtt/ResponderConfig$Builder;")
        setChannelWidth = JavaMethod("(I)Landroid/net/wifi/rtt/ResponderConfig$Builder;")
        setCenterFreq0Mhz = JavaMethod("(I)Landroid/net/wifi/rtt/ResponderConfig$Builder;")
        set80211azNtbSupported = JavaMethod("(Z)Landroid/net/wifi/rtt/ResponderConfig$Builder;")
        set80211mcSupported = JavaMethod("(Z)Landroid/net/wifi/rtt/ResponderConfig$Builder;")
        setSecureRangingConfig = JavaMethod("(Landroid/net/wifi/rtt/SecureRangingConfig;)Landroid/net/wifi/rtt/ResponderConfig$Builder;")
        setFrequencyMhz = JavaMethod("(I)Landroid/net/wifi/rtt/ResponderConfig$Builder;")
        build = JavaMethod("()Landroid/net/wifi/rtt/ResponderConfig;")