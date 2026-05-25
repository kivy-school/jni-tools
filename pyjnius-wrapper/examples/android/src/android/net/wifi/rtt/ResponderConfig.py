from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ResponderConfig"]

class ResponderConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/rtt/ResponderConfig"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    RESPONDER_AP = JavaStaticField("I")
    RESPONDER_STA = JavaStaticField("I")
    fromScanResult = JavaStaticMethod("(Landroid/net/wifi/ScanResult;)Landroid/net/wifi/rtt/ResponderConfig;")
    getMacAddress = JavaMethod("()Landroid/net/MacAddress;")
    is80211mcSupported = JavaMethod("()Z")
    is80211azNtbSupported = JavaMethod("()Z")
    getChannelWidth = JavaMethod("()I")
    getFrequencyMhz = JavaMethod("()I")
    getCenterFreq0Mhz = JavaMethod("()I")
    getCenterFreq1Mhz = JavaMethod("()I")
    getPreamble = JavaMethod("()I")
    getResponderType = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/wifi/rtt/ResponderConfig/Builder"
        __javaconstructor__ = [("()V", False)]
        setMacAddress = JavaMethod("(Landroid/net/MacAddress;)Landroid/net/wifi/rtt/ResponderConfig$Builder;")
        set80211mcSupported = JavaMethod("(Z)Landroid/net/wifi/rtt/ResponderConfig$Builder;")
        set80211azNtbSupported = JavaMethod("(Z)Landroid/net/wifi/rtt/ResponderConfig$Builder;")
        setChannelWidth = JavaMethod("(I)Landroid/net/wifi/rtt/ResponderConfig$Builder;")
        setFrequencyMhz = JavaMethod("(I)Landroid/net/wifi/rtt/ResponderConfig$Builder;")
        setCenterFreq0Mhz = JavaMethod("(I)Landroid/net/wifi/rtt/ResponderConfig$Builder;")
        setCenterFreq1Mhz = JavaMethod("(I)Landroid/net/wifi/rtt/ResponderConfig$Builder;")
        setPreamble = JavaMethod("(I)Landroid/net/wifi/rtt/ResponderConfig$Builder;")
        setResponderType = JavaMethod("(I)Landroid/net/wifi/rtt/ResponderConfig$Builder;")
        build = JavaMethod("()Landroid/net/wifi/rtt/ResponderConfig;")