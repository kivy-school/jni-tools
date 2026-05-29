from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

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
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getSupportedCipherSuites = JavaMethod("()I")
    getMaxMatchFilterLength = JavaMethod("()I")
    getMaxServiceNameLength = JavaMethod("()I")
    getMaxServiceSpecificInfoLength = JavaMethod("()I")
    getNumberOfSupportedDataInterfaces = JavaMethod("()I")
    getNumberOfSupportedDataPaths = JavaMethod("()I")
    getNumberOfSupportedPublishSessions = JavaMethod("()I")
    getNumberOfSupportedSubscribeSessions = JavaMethod("()I")
    getSupportedPairingCipherSuites = JavaMethod("()I")
    isAwarePairingSupported = JavaMethod("()Z")
    isInstantCommunicationModeSupported = JavaMethod("()Z")
    isSuspensionSupported = JavaMethod("()Z")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")