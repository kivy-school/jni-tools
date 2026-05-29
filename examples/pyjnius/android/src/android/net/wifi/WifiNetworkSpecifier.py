from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WifiNetworkSpecifier"]

class WifiNetworkSpecifier(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/WifiNetworkSpecifier"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    canBeSatisfiedBy = JavaMethod("(Landroid/net/NetworkSpecifier;)Z")
    redact = JavaMethod("()Landroid/net/NetworkSpecifier;")
    getPreferredChannelFrequenciesMhz = JavaMethod("()[I")
    getBand = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/wifi/WifiNetworkSpecifier$Builder"
        __javaconstructor__ = [("()V", False)]
        setBssid = JavaMethod("(Landroid/net/MacAddress;)Landroid/net/wifi/WifiNetworkSpecifier$Builder;")
        setBand = JavaMethod("(I)Landroid/net/wifi/WifiNetworkSpecifier$Builder;")
        setBssidPattern = JavaMethod("(Landroid/net/MacAddress;Landroid/net/MacAddress;)Landroid/net/wifi/WifiNetworkSpecifier$Builder;")
        setPreferredChannelsFrequenciesMhz = JavaMethod("([I)Landroid/net/wifi/WifiNetworkSpecifier$Builder;")
        setSsidPattern = JavaMethod("(Landroid/os/PatternMatcher;)Landroid/net/wifi/WifiNetworkSpecifier$Builder;")
        build = JavaMethod("()Landroid/net/wifi/WifiNetworkSpecifier;")
        setWpa3Passphrase = JavaMethod("(Ljava/lang/String;)Landroid/net/wifi/WifiNetworkSpecifier$Builder;")
        setIsEnhancedOpen = JavaMethod("(Z)Landroid/net/wifi/WifiNetworkSpecifier$Builder;")
        setSsid = JavaMethod("(Ljava/lang/String;)Landroid/net/wifi/WifiNetworkSpecifier$Builder;")
        setIsHiddenSsid = JavaMethod("(Z)Landroid/net/wifi/WifiNetworkSpecifier$Builder;")
        setWpa2EnterpriseConfig = JavaMethod("(Landroid/net/wifi/WifiEnterpriseConfig;)Landroid/net/wifi/WifiNetworkSpecifier$Builder;")
        setWpa2Passphrase = JavaMethod("(Ljava/lang/String;)Landroid/net/wifi/WifiNetworkSpecifier$Builder;")
        setWpa3Enterprise192BitModeConfig = JavaMethod("(Landroid/net/wifi/WifiEnterpriseConfig;)Landroid/net/wifi/WifiNetworkSpecifier$Builder;")
        setWpa3EnterpriseConfig = JavaMethod("(Landroid/net/wifi/WifiEnterpriseConfig;)Landroid/net/wifi/WifiNetworkSpecifier$Builder;")
        setWpa3EnterpriseStandardModeConfig = JavaMethod("(Landroid/net/wifi/WifiEnterpriseConfig;)Landroid/net/wifi/WifiNetworkSpecifier$Builder;")