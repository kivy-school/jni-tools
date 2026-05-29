from typing import Any, ClassVar, overload
from android.telephony.BarringInfo import BarringInfo
from android.telephony.CellIdentity import CellIdentity
from android.telephony.CellLocation import CellLocation
from android.telephony.PreciseDataConnectionState import PreciseDataConnectionState
from android.telephony.ServiceState import ServiceState
from android.telephony.SignalStrength import SignalStrength
from android.telephony.TelephonyDisplayInfo import TelephonyDisplayInfo
from android.telephony.ims.ImsReasonInfo import ImsReasonInfo

class TelephonyCallback:
    def __init__(self) -> None: ...

    class UserMobileDataStateListener:
        def onUserMobileDataStateChanged(self, p0: bool) -> None: ...

    class SignalStrengthsListener:
        def onSignalStrengthsChanged(self, p0: SignalStrength) -> None: ...

    class ServiceStateListener:
        def onServiceStateChanged(self, p0: ServiceState) -> None: ...

    class RegistrationFailedListener:
        def onRegistrationFailed(self, p0: CellIdentity, p1: str, p2: int, p3: int, p4: int) -> None: ...

    class PreciseDataConnectionStateListener:
        def onPreciseDataConnectionStateChanged(self, p0: PreciseDataConnectionState) -> None: ...

    class PhysicalChannelConfigListener:
        def onPhysicalChannelConfigChanged(self, p0: list) -> None: ...

    class MessageWaitingIndicatorListener:
        def onMessageWaitingIndicatorChanged(self, p0: bool) -> None: ...

    class ImsCallDisconnectCauseListener:
        def onImsCallDisconnectCauseChanged(self, p0: ImsReasonInfo) -> None: ...

    class EmergencyNumberListListener:
        def onEmergencyNumberListChanged(self, p0: dict) -> None: ...

    class DisplayInfoListener:
        def onDisplayInfoChanged(self, p0: TelephonyDisplayInfo) -> None: ...

    class DataConnectionStateListener:
        def onDataConnectionStateChanged(self, p0: int, p1: int) -> None: ...

    class DataActivityListener:
        def onDataActivity(self, p0: int) -> None: ...

    class DataActivationStateListener:
        def onDataActivationStateChanged(self, p0: int) -> None: ...

    class CellLocationListener:
        def onCellLocationChanged(self, p0: CellLocation) -> None: ...

    class CellInfoListener:
        def onCellInfoChanged(self, p0: list) -> None: ...

    class CarrierNetworkListener:
        def onCarrierNetworkChange(self, p0: bool) -> None: ...

    class CallStateListener:
        def onCallStateChanged(self, p0: int) -> None: ...

    class CallForwardingIndicatorListener:
        def onCallForwardingIndicatorChanged(self, p0: bool) -> None: ...

    class CallDisconnectCauseListener:
        def onCallDisconnectCauseChanged(self, p0: int, p1: int) -> None: ...

    class BarringInfoListener:
        def onBarringInfoChanged(self, p0: BarringInfo) -> None: ...

    class ActiveDataSubscriptionIdListener:
        def onActiveDataSubscriptionIdChanged(self, p0: int) -> None: ...
