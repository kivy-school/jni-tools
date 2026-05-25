from typing import Any, ClassVar, overload
from android.net.NetworkSpecifier import NetworkSpecifier
from android.net.TransportInfo import TransportInfo
from android.os.Parcel import Parcel

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Creator:
    """Forward declaration for ``android.os.Parcelable.Creator``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.os.Parcelable.Creator')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/os/Parcelable/Creator
    """
    ...

class NetworkCapabilities:
    CREATOR: ClassVar[Creator]
    NET_CAPABILITY_CAPTIVE_PORTAL: ClassVar[int]
    NET_CAPABILITY_CBS: ClassVar[int]
    NET_CAPABILITY_DUN: ClassVar[int]
    NET_CAPABILITY_EIMS: ClassVar[int]
    NET_CAPABILITY_ENTERPRISE: ClassVar[int]
    NET_CAPABILITY_FOREGROUND: ClassVar[int]
    NET_CAPABILITY_FOTA: ClassVar[int]
    NET_CAPABILITY_HEAD_UNIT: ClassVar[int]
    NET_CAPABILITY_IA: ClassVar[int]
    NET_CAPABILITY_IMS: ClassVar[int]
    NET_CAPABILITY_INTERNET: ClassVar[int]
    NET_CAPABILITY_LOCAL_NETWORK: ClassVar[int]
    NET_CAPABILITY_MCX: ClassVar[int]
    NET_CAPABILITY_MMS: ClassVar[int]
    NET_CAPABILITY_MMTEL: ClassVar[int]
    NET_CAPABILITY_NOT_CONGESTED: ClassVar[int]
    NET_CAPABILITY_NOT_METERED: ClassVar[int]
    NET_CAPABILITY_NOT_RESTRICTED: ClassVar[int]
    NET_CAPABILITY_NOT_ROAMING: ClassVar[int]
    NET_CAPABILITY_NOT_SUSPENDED: ClassVar[int]
    NET_CAPABILITY_NOT_VPN: ClassVar[int]
    NET_CAPABILITY_PRIORITIZE_BANDWIDTH: ClassVar[int]
    NET_CAPABILITY_PRIORITIZE_LATENCY: ClassVar[int]
    NET_CAPABILITY_RCS: ClassVar[int]
    NET_CAPABILITY_SUPL: ClassVar[int]
    NET_CAPABILITY_TEMPORARILY_NOT_METERED: ClassVar[int]
    NET_CAPABILITY_TRUSTED: ClassVar[int]
    NET_CAPABILITY_VALIDATED: ClassVar[int]
    NET_CAPABILITY_WIFI_P2P: ClassVar[int]
    NET_CAPABILITY_XCAP: ClassVar[int]
    NET_ENTERPRISE_ID_1: ClassVar[int]
    NET_ENTERPRISE_ID_2: ClassVar[int]
    NET_ENTERPRISE_ID_3: ClassVar[int]
    NET_ENTERPRISE_ID_4: ClassVar[int]
    NET_ENTERPRISE_ID_5: ClassVar[int]
    SIGNAL_STRENGTH_UNSPECIFIED: ClassVar[int]
    TRANSPORT_BLUETOOTH: ClassVar[int]
    TRANSPORT_CELLULAR: ClassVar[int]
    TRANSPORT_ETHERNET: ClassVar[int]
    TRANSPORT_LOWPAN: ClassVar[int]
    TRANSPORT_SATELLITE: ClassVar[int]
    TRANSPORT_THREAD: ClassVar[int]
    TRANSPORT_USB: ClassVar[int]
    TRANSPORT_VPN: ClassVar[int]
    TRANSPORT_WIFI: ClassVar[int]
    TRANSPORT_WIFI_AWARE: ClassVar[int]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: "NetworkCapabilities") -> None: ...
    def getEnterpriseIds(self) -> list[int]: ...
    def hasEnterpriseId(self, arg0: int) -> bool: ...
    def getCapabilities(self) -> list[int]: ...
    def hasCapability(self, arg0: int) -> bool: ...
    def hasTransport(self, arg0: int) -> bool: ...
    def getOwnerUid(self) -> int: ...
    def getLinkUpstreamBandwidthKbps(self) -> int: ...
    def getLinkDownstreamBandwidthKbps(self) -> int: ...
    def getNetworkSpecifier(self) -> NetworkSpecifier: ...
    def getTransportInfo(self) -> TransportInfo: ...
    def getSignalStrength(self) -> int: ...
    def equals(self, arg0: Any) -> bool: ...
    def hashCode(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
    def toString(self) -> str: ...
    def getSubscriptionIds(self) -> set: ...
