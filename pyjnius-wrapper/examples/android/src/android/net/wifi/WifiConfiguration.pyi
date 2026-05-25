from typing import Any, ClassVar, overload
from android.net.IpConfiguration import IpConfiguration
from android.net.MacAddress import MacAddress
from android.net.ProxyInfo import ProxyInfo
from android.net.wifi.WifiEnterpriseConfig import WifiEnterpriseConfig
from android.os.Parcel import Parcel
from java.util.BitSet import BitSet

class WifiConfiguration:
    RANDOMIZATION_AUTO: ClassVar[int]
    RANDOMIZATION_NONE: ClassVar[int]
    RANDOMIZATION_NON_PERSISTENT: ClassVar[int]
    RANDOMIZATION_PERSISTENT: ClassVar[int]
    SECURITY_TYPE_DPP: ClassVar[int]
    SECURITY_TYPE_EAP: ClassVar[int]
    SECURITY_TYPE_EAP_SUITE_B: ClassVar[int]
    SECURITY_TYPE_EAP_WPA3_ENTERPRISE: ClassVar[int]
    SECURITY_TYPE_EAP_WPA3_ENTERPRISE_192_BIT: ClassVar[int]
    SECURITY_TYPE_OPEN: ClassVar[int]
    SECURITY_TYPE_OWE: ClassVar[int]
    SECURITY_TYPE_PSK: ClassVar[int]
    SECURITY_TYPE_SAE: ClassVar[int]
    SECURITY_TYPE_WAPI_CERT: ClassVar[int]
    SECURITY_TYPE_WAPI_PSK: ClassVar[int]
    SECURITY_TYPE_WEP: ClassVar[int]
    BSSID: str
    FQDN: str
    SSID: str
    allowedAuthAlgorithms: BitSet
    allowedGroupCiphers: BitSet
    allowedGroupManagementCiphers: BitSet
    allowedKeyManagement: BitSet
    allowedPairwiseCiphers: BitSet
    allowedProtocols: BitSet
    allowedSuiteBCiphers: BitSet
    enterpriseConfig: WifiEnterpriseConfig
    hiddenSSID: bool
    isHomeProviderNetwork: bool
    networkId: int
    preSharedKey: str
    priority: int
    providerFriendlyName: str
    roamingConsortiumIds: list[int]
    status: int
    wepKeys: list[str]
    wepTxKeyIndex: int
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: "WifiConfiguration") -> None: ...
    def setSecurityParams(self, arg0: int) -> None: ...
    def setMacRandomizationSetting(self, arg0: int) -> None: ...
    def getMacRandomizationSetting(self) -> int: ...
    def getRandomizedMacAddress(self) -> MacAddress: ...
    def isDppConfigurator(self) -> bool: ...
    def isPasspoint(self) -> bool: ...
    def toString(self) -> str: ...
    def getKey(self) -> str: ...
    def setIpConfiguration(self, arg0: IpConfiguration) -> None: ...
    def getHttpProxy(self) -> ProxyInfo: ...
    def setHttpProxy(self, arg0: ProxyInfo) -> None: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...

    class AuthAlgorithm:
        LEAP: ClassVar[int]
        OPEN: ClassVar[int]
        SAE: ClassVar[int]
        SHARED: ClassVar[int]
        strings: ClassVar[list[str]]
        varName: ClassVar[str]

    class GroupCipher:
        CCMP: ClassVar[int]
        GCMP_128: ClassVar[int]
        GCMP_256: ClassVar[int]
        SMS4: ClassVar[int]
        TKIP: ClassVar[int]
        WEP104: ClassVar[int]
        WEP40: ClassVar[int]
        strings: ClassVar[list[str]]
        varName: ClassVar[str]

    class GroupMgmtCipher:
        BIP_CMAC_256: ClassVar[int]
        BIP_GMAC_128: ClassVar[int]
        BIP_GMAC_256: ClassVar[int]

    class KeyMgmt:
        DPP: ClassVar[int]
        FILS_SHA256: ClassVar[int]
        FILS_SHA384: ClassVar[int]
        FT_EAP: ClassVar[int]
        FT_PSK: ClassVar[int]
        IEEE8021X: ClassVar[int]
        NONE: ClassVar[int]
        OSEN: ClassVar[int]
        OWE: ClassVar[int]
        SAE: ClassVar[int]
        SUITE_B_192: ClassVar[int]
        WAPI_CERT: ClassVar[int]
        WAPI_PSK: ClassVar[int]
        WPA2_PSK: ClassVar[int]
        WPA_EAP: ClassVar[int]
        WPA_EAP_SHA256: ClassVar[int]
        WPA_PSK: ClassVar[int]
        WPA_PSK_SHA256: ClassVar[int]
        strings: ClassVar[list[str]]
        varName: ClassVar[str]

    class PairwiseCipher:
        CCMP: ClassVar[int]
        GCMP_128: ClassVar[int]
        GCMP_256: ClassVar[int]
        NONE: ClassVar[int]
        SMS4: ClassVar[int]
        TKIP: ClassVar[int]
        strings: ClassVar[list[str]]
        varName: ClassVar[str]

    class Protocol:
        RSN: ClassVar[int]
        WAPI: ClassVar[int]
        WPA: ClassVar[int]
        strings: ClassVar[list[str]]
        varName: ClassVar[str]

    class Status:
        CURRENT: ClassVar[int]
        DISABLED: ClassVar[int]
        ENABLED: ClassVar[int]
        strings: ClassVar[list[str]]
