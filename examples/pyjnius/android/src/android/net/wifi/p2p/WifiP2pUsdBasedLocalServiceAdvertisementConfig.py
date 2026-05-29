from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WifiP2pUsdBasedLocalServiceAdvertisementConfig"]

class WifiP2pUsdBasedLocalServiceAdvertisementConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/p2p/WifiP2pUsdBasedLocalServiceAdvertisementConfig"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getFrequencyMhz = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/wifi/p2p/WifiP2pUsdBasedLocalServiceAdvertisementConfig$Builder"
        __javaconstructor__ = [("()V", False)]
        setFrequencyMhz = JavaMethod("(I)Landroid/net/wifi/p2p/WifiP2pUsdBasedLocalServiceAdvertisementConfig$Builder;")
        build = JavaMethod("()Landroid/net/wifi/p2p/WifiP2pUsdBasedLocalServiceAdvertisementConfig;")