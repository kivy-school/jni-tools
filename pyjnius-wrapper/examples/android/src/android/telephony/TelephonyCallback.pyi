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

    class ActiveDataSubscriptionIdListener:
        def onActiveDataSubscriptionIdChanged(self, arg0: int) -> None: ...

    class BarringInfoListener:
        def onBarringInfoChanged(self, arg0: BarringInfo) -> None: ...

    class CallDisconnectCauseListener:
        def onCallDisconnectCauseChanged(self, arg0: int, arg1: int) -> None: ...

    class CallForwardingIndicatorListener:
        def onCallForwardingIndicatorChanged(self, arg0: bool) -> None: ...

    class CallStateListener:
        def onCallStateChanged(self, arg0: int) -> None: ...

    class CarrierNetworkListener:
        def onCarrierNetworkChange(self, arg0: bool) -> None: ...

    class CellInfoListener:
        def onCellInfoChanged(self, arg0: list) -> None: ...

    class CellLocationListener:
        def onCellLocationChanged(self, arg0: CellLocation) -> None: ...

    class DataActivationStateListener:
        def onDataActivationStateChanged(self, arg0: int) -> None: ...

    class DataActivityListener:
        def onDataActivity(self, arg0: int) -> None: ...

    class DataConnectionStateListener:
        def onDataConnectionStateChanged(self, arg0: int, arg1: int) -> None: ...

    class DisplayInfoListener:
        def onDisplayInfoChanged(self, arg0: TelephonyDisplayInfo) -> None: ...

    class EmergencyNumberListListener:
        def onEmergencyNumberListChanged(self, arg0: dict) -> None: ...

    class ImsCallDisconnectCauseListener:
        def onImsCallDisconnectCauseChanged(self, arg0: ImsReasonInfo) -> None: ...

    class MessageWaitingIndicatorListener:
        def onMessageWaitingIndicatorChanged(self, arg0: bool) -> None: ...

    class PhysicalChannelConfigListener:
        def onPhysicalChannelConfigChanged(self, arg0: list) -> None: ...

    class PreciseDataConnectionStateListener:
        def onPreciseDataConnectionStateChanged(self, arg0: PreciseDataConnectionState) -> None: ...

    class RegistrationFailedListener:
        def onRegistrationFailed(self, arg0: CellIdentity, arg1: str, arg2: int, arg3: int, arg4: int) -> None: ...

    class ServiceStateListener:
        def onServiceStateChanged(self, arg0: ServiceState) -> None: ...

    class SignalStrengthsListener:
        def onSignalStrengthsChanged(self, arg0: SignalStrength) -> None: ...

    class UserMobileDataStateListener:
        def onUserMobileDataStateChanged(self, arg0: bool) -> None: ...
