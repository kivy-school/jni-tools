from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Characteristics"]

class Characteristics(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/aware/Characteristics"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    WIFI_AWARE_CIPHER_SUITE_NCS_PK_128 = JavaStaticField("I")
    WIFI_AWARE_CIPHER_SUITE_NCS_PK_256 = JavaStaticField("I")
    WIFI_AWARE_CIPHER_SUITE_NCS_PK_PASN_128 = JavaStaticField("I")
    WIFI_AWARE_CIPHER_SUITE_NCS_PK_PASN_256 = JavaStaticField("I")
    WIFI_AWARE_CIPHER_SUITE_NCS_SK_128 = JavaStaticField("I")
    WIFI_AWARE_CIPHER_SUITE_NCS_SK_256 = JavaStaticField("I")
    WIFI_AWARE_CIPHER_SUITE_NONE = JavaStaticField("I")
    getMaxServiceNameLength = JavaMethod("()I")
    getMaxServiceSpecificInfoLength = JavaMethod("()I")
    getMaxMatchFilterLength = JavaMethod("()I")
    getNumberOfSupportedDataInterfaces = JavaMethod("()I")
    getNumberOfSupportedPublishSessions = JavaMethod("()I")
    getNumberOfSupportedSubscribeSessions = JavaMethod("()I")
    getNumberOfSupportedDataPaths = JavaMethod("()I")
    isInstantCommunicationModeSupported = JavaMethod("()Z")
    isAwarePairingSupported = JavaMethod("()Z")
    isSuspensionSupported = JavaMethod("()Z")
    getSupportedCipherSuites = JavaMethod("()I")
    getSupportedPairingCipherSuites = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")