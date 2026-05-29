from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WifiP2pUsdBasedServiceConfig"]

class WifiP2pUsdBasedServiceConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/p2p/nsd/WifiP2pUsdBasedServiceConfig"
    __javaconstructor__ = [("()V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    SERVICE_PROTOCOL_TYPE_BONJOUR = JavaStaticField("I")
    SERVICE_PROTOCOL_TYPE_GENERIC = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getServiceSpecificInfo = JavaMethod("()[B")
    toString = JavaMethod("()Ljava/lang/String;")
    getServiceName = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getMaxAllowedServiceSpecificInfoLength = JavaStaticMethod("()I")
    getServiceProtocolType = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/wifi/p2p/nsd/WifiP2pUsdBasedServiceConfig$Builder"
        __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
        setServiceSpecificInfo = JavaMethod("([B)Landroid/net/wifi/p2p/nsd/WifiP2pUsdBasedServiceConfig$Builder;")
        build = JavaMethod("()Landroid/net/wifi/p2p/nsd/WifiP2pUsdBasedServiceConfig;")
        setServiceProtocolType = JavaMethod("(I)Landroid/net/wifi/p2p/nsd/WifiP2pUsdBasedServiceConfig$Builder;")