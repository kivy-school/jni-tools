from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel
from android.telephony.CellIdentity import CellIdentity
from android.telephony.CellIdentityWcdma import CellIdentityWcdma
from android.telephony.CellSignalStrength import CellSignalStrength
from android.telephony.CellSignalStrengthWcdma import CellSignalStrengthWcdma

class CellInfoWcdma:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    CONNECTION_NONE: ClassVar[int]
    CONNECTION_PRIMARY_SERVING: ClassVar[int]
    CONNECTION_SECONDARY_SERVING: ClassVar[int]
    CONNECTION_UNKNOWN: ClassVar[int]
    CREATOR: ClassVar[Any]
    UNAVAILABLE: ClassVar[int]
    UNAVAILABLE_LONG: ClassVar[int]
    @overload
    def getCellSignalStrength(self) -> CellSignalStrengthWcdma: ...
    @overload
    def getCellSignalStrength(self) -> CellSignalStrength: ...
    @overload
    def getCellIdentity(self) -> CellIdentity: ...
    @overload
    def getCellIdentity(self) -> CellIdentityWcdma: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload

class DisconnectCause:
    ALREADY_DIALING: ClassVar[int]
    ANSWERED_ELSEWHERE: ClassVar[int]
    BUSY: ClassVar[int]
    CALLING_DISABLED: ClassVar[int]
    CALL_BARRED: ClassVar[int]
    CALL_PULLED: ClassVar[int]
    CANT_CALL_WHILE_RINGING: ClassVar[int]
    CDMA_ACCESS_BLOCKED: ClassVar[int]
    CDMA_ACCESS_FAILURE: ClassVar[int]
    CDMA_ALREADY_ACTIVATED: ClassVar[int]
    CDMA_DROP: ClassVar[int]
    CDMA_INTERCEPT: ClassVar[int]
    CDMA_LOCKED_UNTIL_POWER_CYCLE: ClassVar[int]
    CDMA_NOT_EMERGENCY: ClassVar[int]
    CDMA_PREEMPTED: ClassVar[int]
    CDMA_REORDER: ClassVar[int]
    CDMA_RETRY_ORDER: ClassVar[int]
    CDMA_SO_REJECT: ClassVar[int]
    CONGESTION: ClassVar[int]
    CS_RESTRICTED: ClassVar[int]
    CS_RESTRICTED_EMERGENCY: ClassVar[int]
    CS_RESTRICTED_NORMAL: ClassVar[int]
    DATA_DISABLED: ClassVar[int]
    DATA_LIMIT_REACHED: ClassVar[int]
    DIALED_CALL_FORWARDING_WHILE_ROAMING: ClassVar[int]
    DIALED_MMI: ClassVar[int]
    DIAL_LOW_BATTERY: ClassVar[int]
    DIAL_MODIFIED_TO_DIAL: ClassVar[int]
    DIAL_MODIFIED_TO_DIAL_VIDEO: ClassVar[int]
    DIAL_MODIFIED_TO_SS: ClassVar[int]
    DIAL_MODIFIED_TO_USSD: ClassVar[int]
    DIAL_VIDEO_MODIFIED_TO_DIAL: ClassVar[int]
    DIAL_VIDEO_MODIFIED_TO_DIAL_VIDEO: ClassVar[int]
    DIAL_VIDEO_MODIFIED_TO_SS: ClassVar[int]
    DIAL_VIDEO_MODIFIED_TO_USSD: ClassVar[int]
    EMERGENCY_CALL_OVER_WFC_NOT_AVAILABLE: ClassVar[int]
    EMERGENCY_PERM_FAILURE: ClassVar[int]
    EMERGENCY_TEMP_FAILURE: ClassVar[int]
    ERROR_UNSPECIFIED: ClassVar[int]
    FDN_BLOCKED: ClassVar[int]
    ICC_ERROR: ClassVar[int]
    IMEI_NOT_ACCEPTED: ClassVar[int]
    IMS_ACCESS_BLOCKED: ClassVar[int]
    IMS_MERGED_SUCCESSFULLY: ClassVar[int]
    IMS_SIP_ALTERNATE_EMERGENCY_CALL: ClassVar[int]
    INCOMING_AUTO_REJECTED: ClassVar[int]
    INCOMING_MISSED: ClassVar[int]
    INCOMING_REJECTED: ClassVar[int]
    INVALID_CREDENTIALS: ClassVar[int]
    INVALID_NUMBER: ClassVar[int]
    LIMIT_EXCEEDED: ClassVar[int]
    LOCAL: ClassVar[int]
    LOST_SIGNAL: ClassVar[int]
    LOW_BATTERY: ClassVar[int]
    MAXIMUM_NUMBER_OF_CALLS_REACHED: ClassVar[int]
    MEDIA_TIMEOUT: ClassVar[int]
    MMI: ClassVar[int]
    NORMAL: ClassVar[int]
    NORMAL_UNSPECIFIED: ClassVar[int]
    NOT_DISCONNECTED: ClassVar[int]
    NOT_VALID: ClassVar[int]
    NO_PHONE_NUMBER_SUPPLIED: ClassVar[int]
    NUMBER_UNREACHABLE: ClassVar[int]
    OTASP_PROVISIONING_IN_PROCESS: ClassVar[int]
    OUTGOING_CANCELED: ClassVar[int]
    OUTGOING_EMERGENCY_CALL_PLACED: ClassVar[int]
    OUTGOING_FAILURE: ClassVar[int]
    OUT_OF_NETWORK: ClassVar[int]
    OUT_OF_SERVICE: ClassVar[int]
    POWER_OFF: ClassVar[int]
    SATELLITE_ENABLED: ClassVar[int]
    SERVER_ERROR: ClassVar[int]
    SERVER_UNREACHABLE: ClassVar[int]
    TIMED_OUT: ClassVar[int]
    TOO_MANY_ONGOING_CALLS: ClassVar[int]
    UNOBTAINABLE_NUMBER: ClassVar[int]
    VIDEO_CALL_NOT_ALLOWED_WHILE_TTY_ENABLED: ClassVar[int]
    VOICEMAIL_NUMBER_MISSING: ClassVar[int]
    WFC_SERVICE_NOT_AVAILABLE_IN_THIS_LOCATION: ClassVar[int]
    WIFI_LOST: ClassVar[int]

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

from typing import Any, ClassVar, overload
from android.telephony.BarringInfo import BarringInfo
from android.telephony.CellIdentity import CellIdentity
from android.telephony.CellLocation import CellLocation
from android.telephony.PreciseDataConnectionState import PreciseDataConnectionState
from android.telephony.ServiceState import ServiceState
from android.telephony.SignalStrength import SignalStrength
from android.telephony.TelephonyDisplayInfo import TelephonyDisplayInfo
from android.telephony.ims.ImsReasonInfo import ImsReasonInfo
from java.util.concurrent.Executor import Executor

class PhoneStateListener:
    LISTEN_ACTIVE_DATA_SUBSCRIPTION_ID_CHANGE: ClassVar[int]
    LISTEN_BARRING_INFO: ClassVar[int]
    LISTEN_CALL_DISCONNECT_CAUSES: ClassVar[int]
    LISTEN_CALL_FORWARDING_INDICATOR: ClassVar[int]
    LISTEN_CALL_STATE: ClassVar[int]
    LISTEN_CELL_INFO: ClassVar[int]
    LISTEN_CELL_LOCATION: ClassVar[int]
    LISTEN_DATA_ACTIVITY: ClassVar[int]
    LISTEN_DATA_CONNECTION_STATE: ClassVar[int]
    LISTEN_DISPLAY_INFO_CHANGED: ClassVar[int]
    LISTEN_EMERGENCY_NUMBER_LIST: ClassVar[int]
    LISTEN_IMS_CALL_DISCONNECT_CAUSES: ClassVar[int]
    LISTEN_MESSAGE_WAITING_INDICATOR: ClassVar[int]
    LISTEN_NONE: ClassVar[int]
    LISTEN_PRECISE_DATA_CONNECTION_STATE: ClassVar[int]
    LISTEN_REGISTRATION_FAILURE: ClassVar[int]
    LISTEN_SERVICE_STATE: ClassVar[int]
    LISTEN_SIGNAL_STRENGTH: ClassVar[int]
    LISTEN_SIGNAL_STRENGTHS: ClassVar[int]
    LISTEN_USER_MOBILE_DATA_STATE: ClassVar[int]
    @overload
    def __init__(self, p0: Executor) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def onSignalStrengthsChanged(self, p0: SignalStrength) -> None: ...
    def onImsCallDisconnectCauseChanged(self, p0: ImsReasonInfo) -> None: ...
    def onDisplayInfoChanged(self, p0: TelephonyDisplayInfo) -> None: ...
    def onEmergencyNumberListChanged(self, p0: dict) -> None: ...
    def onServiceStateChanged(self, p0: ServiceState) -> None: ...
    def onActiveDataSubscriptionIdChanged(self, p0: int) -> None: ...
    def onCallDisconnectCauseChanged(self, p0: int, p1: int) -> None: ...
    def onCallForwardingIndicatorChanged(self, p0: bool) -> None: ...
    def onBarringInfoChanged(self, p0: BarringInfo) -> None: ...
    def onCellInfoChanged(self, p0: list) -> None: ...
    def onCallStateChanged(self, p0: int, p1: str) -> None: ...
    def onDataActivity(self, p0: int) -> None: ...
    def onPreciseDataConnectionStateChanged(self, p0: PreciseDataConnectionState) -> None: ...
    def onMessageWaitingIndicatorChanged(self, p0: bool) -> None: ...
    @overload
    def onDataConnectionStateChanged(self, p0: int, p1: int) -> None: ...
    @overload
    def onDataConnectionStateChanged(self, p0: int) -> None: ...
    def onSignalStrengthChanged(self, p0: int) -> None: ...
    def onCellLocationChanged(self, p0: CellLocation) -> None: ...
    def onRegistrationFailed(self, p0: CellIdentity, p1: str, p2: int, p3: int, p4: int) -> None: ...
    def onUserMobileDataStateChanged(self, p0: bool) -> None: ...

from typing import Any, ClassVar, overload
from android.app.PendingIntent import PendingIntent
from android.content.Context import Context
from android.os.ParcelUuid import ParcelUuid
from android.telephony.SubscriptionInfo import SubscriptionInfo
from java.util.concurrent.Executor import Executor

class SubscriptionManager:
    ACTION_DEFAULT_SMS_SUBSCRIPTION_CHANGED: ClassVar[str]
    ACTION_DEFAULT_SUBSCRIPTION_CHANGED: ClassVar[str]
    ACTION_MANAGE_SUBSCRIPTION_PLANS: ClassVar[str]
    ACTION_REFRESH_SUBSCRIPTION_PLANS: ClassVar[str]
    D2D_SHARING_ALL: ClassVar[int]
    D2D_SHARING_ALL_CONTACTS: ClassVar[int]
    D2D_SHARING_DISABLED: ClassVar[int]
    D2D_SHARING_SELECTED_CONTACTS: ClassVar[int]
    D2D_STATUS_SHARING: ClassVar[str]
    D2D_STATUS_SHARING_SELECTED_CONTACTS: ClassVar[str]
    DATA_ROAMING_DISABLE: ClassVar[int]
    DATA_ROAMING_ENABLE: ClassVar[int]
    DEFAULT_SUBSCRIPTION_ID: ClassVar[int]
    EXTRA_SLOT_INDEX: ClassVar[str]
    EXTRA_SUBSCRIPTION_INDEX: ClassVar[str]
    INVALID_SIM_SLOT_INDEX: ClassVar[int]
    INVALID_SUBSCRIPTION_ID: ClassVar[int]
    PHONE_NUMBER_SOURCE_CARRIER: ClassVar[int]
    PHONE_NUMBER_SOURCE_IMS: ClassVar[int]
    PHONE_NUMBER_SOURCE_UICC: ClassVar[int]
    SERVICE_CAPABILITY_DATA: ClassVar[int]
    SERVICE_CAPABILITY_SMS: ClassVar[int]
    SERVICE_CAPABILITY_VOICE: ClassVar[int]
    SUBSCRIPTION_TYPE_LOCAL_SIM: ClassVar[int]
    SUBSCRIPTION_TYPE_REMOTE_SIM: ClassVar[int]
    USAGE_SETTING_DATA_CENTRIC: ClassVar[int]
    USAGE_SETTING_DEFAULT: ClassVar[int]
    USAGE_SETTING_UNKNOWN: ClassVar[int]
    USAGE_SETTING_VOICE_CENTRIC: ClassVar[int]
    @staticmethod
    def getSubscriptionId(p0: int) -> int: ...
    @overload
    def getPhoneNumber(self, p0: int, p1: int) -> str: ...
    @overload
    def getPhoneNumber(self, p0: int) -> str: ...
    def getSubscriptionIds(self, p0: int) -> Any: ...
    def addOnOpportunisticSubscriptionsChangedListener(self, p0: Executor, p1: Any) -> None: ...
    @overload
    def addOnSubscriptionsChangedListener(self, p0: Any) -> None: ...
    @overload
    def addOnSubscriptionsChangedListener(self, p0: Executor, p1: Any) -> None: ...
    def addSubscriptionsIntoGroup(self, p0: list, p1: ParcelUuid) -> None: ...
    def canManageSubscription(self, p0: SubscriptionInfo) -> bool: ...
    def createSubscriptionGroup(self, p0: list) -> ParcelUuid: ...
    def getAccessibleSubscriptionInfoList(self) -> list: ...
    @staticmethod
    def getActiveDataSubscriptionId() -> int: ...
    def getActiveSubscriptionInfo(self, p0: int) -> SubscriptionInfo: ...
    def getActiveSubscriptionInfoCount(self) -> int: ...
    def getActiveSubscriptionInfoCountMax(self) -> int: ...
    def getActiveSubscriptionInfoForSimSlotIndex(self, p0: int) -> SubscriptionInfo: ...
    def getActiveSubscriptionInfoList(self) -> list: ...
    def getAllSubscriptionInfoList(self) -> list: ...
    def getCompleteActiveSubscriptionInfoList(self) -> list: ...
    @staticmethod
    def getDefaultDataSubscriptionId() -> int: ...
    @staticmethod
    def getDefaultSmsSubscriptionId() -> int: ...
    @staticmethod
    def getDefaultSubscriptionId() -> int: ...
    @staticmethod
    def getDefaultVoiceSubscriptionId() -> int: ...
    def getDeviceToDeviceStatusSharingContacts(self, p0: int) -> list: ...
    def getDeviceToDeviceStatusSharingPreference(self, p0: int) -> int: ...
    def getOpportunisticSubscriptions(self) -> list: ...
    @staticmethod
    def getSlotIndex(p0: int) -> int: ...
    def getSubscriptionPlans(self, p0: int) -> list: ...
    def getSubscriptionsInGroup(self, p0: ParcelUuid) -> list: ...
    def isActiveSubscriptionId(self, p0: int) -> bool: ...
    def isNetworkRoaming(self, p0: int) -> bool: ...
    @staticmethod
    def isUsableSubscriptionId(p0: int) -> bool: ...
    @staticmethod
    def isValidSubscriptionId(p0: int) -> bool: ...
    def removeOnOpportunisticSubscriptionsChangedListener(self, p0: Any) -> None: ...
    def removeOnSubscriptionsChangedListener(self, p0: Any) -> None: ...
    def removeSubscriptionsFromGroup(self, p0: list, p1: ParcelUuid) -> None: ...
    def setCarrierPhoneNumber(self, p0: int, p1: str) -> None: ...
    def setDeviceToDeviceStatusSharingContacts(self, p0: int, p1: list) -> None: ...
    def setDeviceToDeviceStatusSharingPreference(self, p0: int, p1: int) -> None: ...
    def setOpportunistic(self, p0: bool, p1: int) -> bool: ...
    @overload
    def setSubscriptionOverrideCongested(self, p0: int, p1: bool, p2: Any, p3: int) -> None: ...
    @overload
    def setSubscriptionOverrideCongested(self, p0: int, p1: bool, p2: int) -> None: ...
    @overload
    def setSubscriptionOverrideUnmetered(self, p0: int, p1: bool, p2: Any, p3: int) -> None: ...
    @overload
    def setSubscriptionOverrideUnmetered(self, p0: int, p1: bool, p2: int) -> None: ...
    @overload
    def setSubscriptionPlans(self, p0: int, p1: list, p2: int) -> None: ...
    @overload
    def setSubscriptionPlans(self, p0: int, p1: list) -> None: ...
    def switchToSubscription(self, p0: int, p1: PendingIntent) -> None: ...
    @staticmethod
    def from_(p0: Context) -> "SubscriptionManager": ...

    class OnSubscriptionsChangedListener:
        def __init__(self) -> None: ...
        def onSubscriptionsChanged(self) -> None: ...

    class OnOpportunisticSubscriptionsChangedListener:
        def __init__(self) -> None: ...
        def onOpportunisticSubscriptionsChanged(self) -> None: ...

from typing import Any, ClassVar, overload
from android.app.PendingIntent import PendingIntent
from android.net.Uri import Uri
from android.os.Handler import Handler
from android.os.OutcomeReceiver import OutcomeReceiver
from android.os.PersistableBundle import PersistableBundle
from android.telecom.PhoneAccountHandle import PhoneAccountHandle
from android.telephony.CellLocation import CellLocation
from android.telephony.IccOpenLogicalChannelResponse import IccOpenLogicalChannelResponse
from android.telephony.NetworkScan import NetworkScan
from android.telephony.NetworkScanRequest import NetworkScanRequest
from android.telephony.PhoneStateListener import PhoneStateListener
from android.telephony.ServiceState import ServiceState
from android.telephony.SignalStrength import SignalStrength
from android.telephony.SignalStrengthUpdateRequest import SignalStrengthUpdateRequest
from android.telephony.TelephonyCallback import TelephonyCallback
from android.telephony.VisualVoicemailSmsFilterSettings import VisualVoicemailSmsFilterSettings
from java.io.IOException import IOException
from java.io.InputStream import InputStream
from java.lang.Throwable import Throwable
from java.nio.file.Path import Path
from java.util.concurrent.Executor import Executor
from java.util.function.Consumer import Consumer

class TelephonyManager:
    ACTION_CARRIER_MESSAGING_CLIENT_SERVICE: ClassVar[str]
    ACTION_CARRIER_SIGNAL_DEFAULT_NETWORK_AVAILABLE: ClassVar[str]
    ACTION_CARRIER_SIGNAL_PCO_VALUE: ClassVar[str]
    ACTION_CARRIER_SIGNAL_REDIRECTED: ClassVar[str]
    ACTION_CARRIER_SIGNAL_REQUEST_NETWORK_FAILED: ClassVar[str]
    ACTION_CARRIER_SIGNAL_RESET: ClassVar[str]
    ACTION_CONFIGURE_VOICEMAIL: ClassVar[str]
    ACTION_MULTI_SIM_CONFIG_CHANGED: ClassVar[str]
    ACTION_NETWORK_COUNTRY_CHANGED: ClassVar[str]
    ACTION_PHONE_STATE_CHANGED: ClassVar[str]
    ACTION_RESET_MOBILE_NETWORK_SETTINGS: ClassVar[str]
    ACTION_RESPOND_VIA_MESSAGE: ClassVar[str]
    ACTION_SECRET_CODE: ClassVar[str]
    ACTION_SHOW_VOICEMAIL_NOTIFICATION: ClassVar[str]
    ACTION_SUBSCRIPTION_CARRIER_IDENTITY_CHANGED: ClassVar[str]
    ACTION_SUBSCRIPTION_SPECIFIC_CARRIER_IDENTITY_CHANGED: ClassVar[str]
    ALLOWED_NETWORK_TYPES_REASON_CARRIER: ClassVar[int]
    ALLOWED_NETWORK_TYPES_REASON_USER: ClassVar[int]
    APPTYPE_CSIM: ClassVar[int]
    APPTYPE_ISIM: ClassVar[int]
    APPTYPE_RUIM: ClassVar[int]
    APPTYPE_SIM: ClassVar[int]
    APPTYPE_UNKNOWN: ClassVar[int]
    APPTYPE_USIM: ClassVar[int]
    AUTHTYPE_EAP_AKA: ClassVar[int]
    AUTHTYPE_EAP_SIM: ClassVar[int]
    AUTHTYPE_GBA_BOOTSTRAP: ClassVar[int]
    AUTHTYPE_GBA_NAF_KEY_EXTERNAL: ClassVar[int]
    CALL_COMPOSER_STATUS_BUSINESS_ONLY: ClassVar[int]
    CALL_COMPOSER_STATUS_OFF: ClassVar[int]
    CALL_COMPOSER_STATUS_ON: ClassVar[int]
    CALL_STATE_IDLE: ClassVar[int]
    CALL_STATE_OFFHOOK: ClassVar[int]
    CALL_STATE_RINGING: ClassVar[int]
    CAPABILITY_SLICING_CONFIG_SUPPORTED: ClassVar[str]
    CARRIER_RESTRICTION_STATUS_NOT_RESTRICTED: ClassVar[int]
    CARRIER_RESTRICTION_STATUS_RESTRICTED: ClassVar[int]
    CARRIER_RESTRICTION_STATUS_RESTRICTED_TO_CALLER: ClassVar[int]
    CARRIER_RESTRICTION_STATUS_UNKNOWN: ClassVar[int]
    CDMA_ROAMING_MODE_AFFILIATED: ClassVar[int]
    CDMA_ROAMING_MODE_ANY: ClassVar[int]
    CDMA_ROAMING_MODE_HOME: ClassVar[int]
    CDMA_ROAMING_MODE_RADIO_DEFAULT: ClassVar[int]
    DATA_ACTIVITY_DORMANT: ClassVar[int]
    DATA_ACTIVITY_IN: ClassVar[int]
    DATA_ACTIVITY_INOUT: ClassVar[int]
    DATA_ACTIVITY_NONE: ClassVar[int]
    DATA_ACTIVITY_OUT: ClassVar[int]
    DATA_CONNECTED: ClassVar[int]
    DATA_CONNECTING: ClassVar[int]
    DATA_DISCONNECTED: ClassVar[int]
    DATA_DISCONNECTING: ClassVar[int]
    DATA_ENABLED_REASON_CARRIER: ClassVar[int]
    DATA_ENABLED_REASON_OVERRIDE: ClassVar[int]
    DATA_ENABLED_REASON_POLICY: ClassVar[int]
    DATA_ENABLED_REASON_THERMAL: ClassVar[int]
    DATA_ENABLED_REASON_UNKNOWN: ClassVar[int]
    DATA_ENABLED_REASON_USER: ClassVar[int]
    DATA_HANDOVER_IN_PROGRESS: ClassVar[int]
    DATA_SUSPENDED: ClassVar[int]
    DATA_UNKNOWN: ClassVar[int]
    DEFAULT_PORT_INDEX: ClassVar[int]
    ERI_FLASH: ClassVar[int]
    ERI_OFF: ClassVar[int]
    ERI_ON: ClassVar[int]
    EVENT_DISPLAY_EMERGENCY_MESSAGE: ClassVar[str]
    EXTRA_ACTIVE_SIM_SUPPORTED_COUNT: ClassVar[str]
    EXTRA_APN_PROTOCOL: ClassVar[str]
    EXTRA_APN_TYPE: ClassVar[str]
    EXTRA_CALL_VOICEMAIL_INTENT: ClassVar[str]
    EXTRA_CARRIER_ID: ClassVar[str]
    EXTRA_CARRIER_NAME: ClassVar[str]
    EXTRA_DATA_FAIL_CAUSE: ClassVar[str]
    EXTRA_DEFAULT_NETWORK_AVAILABLE: ClassVar[str]
    EXTRA_EMERGENCY_CALL_TO_SATELLITE_HANDOVER_TYPE: ClassVar[str]
    EXTRA_EMERGENCY_CALL_TO_SATELLITE_LAUNCH_INTENT: ClassVar[str]
    EXTRA_HIDE_PUBLIC_SETTINGS: ClassVar[str]
    EXTRA_INCOMING_NUMBER: ClassVar[str]
    EXTRA_IS_REFRESH: ClassVar[str]
    EXTRA_LAST_KNOWN_NETWORK_COUNTRY: ClassVar[str]
    EXTRA_LAUNCH_VOICEMAIL_SETTINGS_INTENT: ClassVar[str]
    EXTRA_NETWORK_COUNTRY: ClassVar[str]
    EXTRA_NOTIFICATION_COUNT: ClassVar[str]
    EXTRA_PCO_ID: ClassVar[str]
    EXTRA_PCO_VALUE: ClassVar[str]
    EXTRA_PHONE_ACCOUNT_HANDLE: ClassVar[str]
    EXTRA_REDIRECTION_URL: ClassVar[str]
    EXTRA_SPECIFIC_CARRIER_ID: ClassVar[str]
    EXTRA_SPECIFIC_CARRIER_NAME: ClassVar[str]
    EXTRA_STATE: ClassVar[str]
    EXTRA_STATE_IDLE: ClassVar[str]
    EXTRA_STATE_OFFHOOK: ClassVar[str]
    EXTRA_STATE_RINGING: ClassVar[str]
    EXTRA_SUBSCRIPTION_ID: ClassVar[str]
    EXTRA_VOICEMAIL_NUMBER: ClassVar[str]
    INCLUDE_LOCATION_DATA_COARSE: ClassVar[int]
    INCLUDE_LOCATION_DATA_FINE: ClassVar[int]
    INCLUDE_LOCATION_DATA_NONE: ClassVar[int]
    METADATA_HIDE_VOICEMAIL_SETTINGS_MENU: ClassVar[str]
    MULTISIM_ALLOWED: ClassVar[int]
    MULTISIM_NOT_SUPPORTED_BY_CARRIER: ClassVar[int]
    MULTISIM_NOT_SUPPORTED_BY_HARDWARE: ClassVar[int]
    NETWORK_SELECTION_MODE_AUTO: ClassVar[int]
    NETWORK_SELECTION_MODE_MANUAL: ClassVar[int]
    NETWORK_SELECTION_MODE_UNKNOWN: ClassVar[int]
    NETWORK_TYPE_1xRTT: ClassVar[int]
    NETWORK_TYPE_BITMASK_1xRTT: ClassVar[int]
    NETWORK_TYPE_BITMASK_CDMA: ClassVar[int]
    NETWORK_TYPE_BITMASK_EDGE: ClassVar[int]
    NETWORK_TYPE_BITMASK_EHRPD: ClassVar[int]
    NETWORK_TYPE_BITMASK_EVDO_0: ClassVar[int]
    NETWORK_TYPE_BITMASK_EVDO_A: ClassVar[int]
    NETWORK_TYPE_BITMASK_EVDO_B: ClassVar[int]
    NETWORK_TYPE_BITMASK_GPRS: ClassVar[int]
    NETWORK_TYPE_BITMASK_GSM: ClassVar[int]
    NETWORK_TYPE_BITMASK_HSDPA: ClassVar[int]
    NETWORK_TYPE_BITMASK_HSPA: ClassVar[int]
    NETWORK_TYPE_BITMASK_HSPAP: ClassVar[int]
    NETWORK_TYPE_BITMASK_HSUPA: ClassVar[int]
    NETWORK_TYPE_BITMASK_IWLAN: ClassVar[int]
    NETWORK_TYPE_BITMASK_LTE: ClassVar[int]
    NETWORK_TYPE_BITMASK_LTE_CA: ClassVar[int]
    NETWORK_TYPE_BITMASK_NR: ClassVar[int]
    NETWORK_TYPE_BITMASK_TD_SCDMA: ClassVar[int]
    NETWORK_TYPE_BITMASK_UMTS: ClassVar[int]
    NETWORK_TYPE_BITMASK_UNKNOWN: ClassVar[int]
    NETWORK_TYPE_CDMA: ClassVar[int]
    NETWORK_TYPE_EDGE: ClassVar[int]
    NETWORK_TYPE_EHRPD: ClassVar[int]
    NETWORK_TYPE_EVDO_0: ClassVar[int]
    NETWORK_TYPE_EVDO_A: ClassVar[int]
    NETWORK_TYPE_EVDO_B: ClassVar[int]
    NETWORK_TYPE_GPRS: ClassVar[int]
    NETWORK_TYPE_GSM: ClassVar[int]
    NETWORK_TYPE_HSDPA: ClassVar[int]
    NETWORK_TYPE_HSPA: ClassVar[int]
    NETWORK_TYPE_HSPAP: ClassVar[int]
    NETWORK_TYPE_HSUPA: ClassVar[int]
    NETWORK_TYPE_IDEN: ClassVar[int]
    NETWORK_TYPE_IWLAN: ClassVar[int]
    NETWORK_TYPE_LTE: ClassVar[int]
    NETWORK_TYPE_NR: ClassVar[int]
    NETWORK_TYPE_TD_SCDMA: ClassVar[int]
    NETWORK_TYPE_UMTS: ClassVar[int]
    NETWORK_TYPE_UNKNOWN: ClassVar[int]
    PHONE_TYPE_CDMA: ClassVar[int]
    PHONE_TYPE_GSM: ClassVar[int]
    PHONE_TYPE_NONE: ClassVar[int]
    PHONE_TYPE_SIP: ClassVar[int]
    PREMIUM_CAPABILITY_PRIORITIZE_LATENCY: ClassVar[int]
    PURCHASE_PREMIUM_CAPABILITY_RESULT_ALREADY_IN_PROGRESS: ClassVar[int]
    PURCHASE_PREMIUM_CAPABILITY_RESULT_ALREADY_PURCHASED: ClassVar[int]
    PURCHASE_PREMIUM_CAPABILITY_RESULT_CARRIER_DISABLED: ClassVar[int]
    PURCHASE_PREMIUM_CAPABILITY_RESULT_CARRIER_ERROR: ClassVar[int]
    PURCHASE_PREMIUM_CAPABILITY_RESULT_ENTITLEMENT_CHECK_FAILED: ClassVar[int]
    PURCHASE_PREMIUM_CAPABILITY_RESULT_FEATURE_NOT_SUPPORTED: ClassVar[int]
    PURCHASE_PREMIUM_CAPABILITY_RESULT_NETWORK_NOT_AVAILABLE: ClassVar[int]
    PURCHASE_PREMIUM_CAPABILITY_RESULT_NOT_DEFAULT_DATA_SUBSCRIPTION: ClassVar[int]
    PURCHASE_PREMIUM_CAPABILITY_RESULT_NOT_FOREGROUND: ClassVar[int]
    PURCHASE_PREMIUM_CAPABILITY_RESULT_PENDING_NETWORK_SETUP: ClassVar[int]
    PURCHASE_PREMIUM_CAPABILITY_RESULT_REQUEST_FAILED: ClassVar[int]
    PURCHASE_PREMIUM_CAPABILITY_RESULT_SUCCESS: ClassVar[int]
    PURCHASE_PREMIUM_CAPABILITY_RESULT_THROTTLED: ClassVar[int]
    PURCHASE_PREMIUM_CAPABILITY_RESULT_TIMEOUT: ClassVar[int]
    PURCHASE_PREMIUM_CAPABILITY_RESULT_USER_CANCELED: ClassVar[int]
    PURCHASE_PREMIUM_CAPABILITY_RESULT_USER_DISABLED: ClassVar[int]
    SET_OPPORTUNISTIC_SUB_INACTIVE_SUBSCRIPTION: ClassVar[int]
    SET_OPPORTUNISTIC_SUB_NO_OPPORTUNISTIC_SUB_AVAILABLE: ClassVar[int]
    SET_OPPORTUNISTIC_SUB_REMOTE_SERVICE_EXCEPTION: ClassVar[int]
    SET_OPPORTUNISTIC_SUB_SUCCESS: ClassVar[int]
    SET_OPPORTUNISTIC_SUB_VALIDATION_FAILED: ClassVar[int]
    SIM_STATE_ABSENT: ClassVar[int]
    SIM_STATE_CARD_IO_ERROR: ClassVar[int]
    SIM_STATE_CARD_RESTRICTED: ClassVar[int]
    SIM_STATE_NETWORK_LOCKED: ClassVar[int]
    SIM_STATE_NOT_READY: ClassVar[int]
    SIM_STATE_PERM_DISABLED: ClassVar[int]
    SIM_STATE_PIN_REQUIRED: ClassVar[int]
    SIM_STATE_PUK_REQUIRED: ClassVar[int]
    SIM_STATE_READY: ClassVar[int]
    SIM_STATE_UNKNOWN: ClassVar[int]
    UNINITIALIZED_CARD_ID: ClassVar[int]
    UNKNOWN_CARRIER_ID: ClassVar[int]
    UNSUPPORTED_CARD_ID: ClassVar[int]
    UPDATE_AVAILABLE_NETWORKS_ABORTED: ClassVar[int]
    UPDATE_AVAILABLE_NETWORKS_DISABLE_MODEM_FAIL: ClassVar[int]
    UPDATE_AVAILABLE_NETWORKS_ENABLE_MODEM_FAIL: ClassVar[int]
    UPDATE_AVAILABLE_NETWORKS_INVALID_ARGUMENTS: ClassVar[int]
    UPDATE_AVAILABLE_NETWORKS_MULTIPLE_NETWORKS_NOT_SUPPORTED: ClassVar[int]
    UPDATE_AVAILABLE_NETWORKS_NO_CARRIER_PRIVILEGE: ClassVar[int]
    UPDATE_AVAILABLE_NETWORKS_NO_OPPORTUNISTIC_SUB_AVAILABLE: ClassVar[int]
    UPDATE_AVAILABLE_NETWORKS_REMOTE_SERVICE_EXCEPTION: ClassVar[int]
    UPDATE_AVAILABLE_NETWORKS_SERVICE_IS_DISABLED: ClassVar[int]
    UPDATE_AVAILABLE_NETWORKS_SUCCESS: ClassVar[int]
    UPDATE_AVAILABLE_NETWORKS_UNKNOWN_FAILURE: ClassVar[int]
    USSD_ERROR_SERVICE_UNAVAIL: ClassVar[int]
    USSD_RETURN_FAILURE: ClassVar[int]
    VVM_TYPE_CVVM: ClassVar[str]
    VVM_TYPE_OMTP: ClassVar[str]
    @overload
    def getSubscriptionId(self, p0: PhoneAccountHandle) -> int: ...
    @overload
    def getSubscriptionId(self) -> int: ...
    def getDataNetworkType(self) -> int: ...
    def getNetworkSpecifier(self) -> str: ...
    def getSignalStrength(self) -> SignalStrength: ...
    def getNetworkType(self) -> int: ...
    def getNai(self) -> str: ...
    def isNetworkRoaming(self) -> bool: ...
    def canChangeDtmfToneLength(self) -> bool: ...
    def clearSignalStrengthUpdateRequest(self, p0: SignalStrengthUpdateRequest) -> None: ...
    def createForPhoneAccountHandle(self, p0: PhoneAccountHandle) -> "TelephonyManager": ...
    def createForSubscriptionId(self, p0: int) -> "TelephonyManager": ...
    def doesSwitchMultiSimConfigTriggerReboot(self) -> bool: ...
    def getActiveModemCount(self) -> int: ...
    def getAllCellInfo(self) -> list: ...
    def getAllowedNetworkTypesForReason(self, p0: int) -> int: ...
    def getCallComposerStatus(self) -> int: ...
    def getCallState(self) -> int: ...
    def getCallStateForSubscription(self) -> int: ...
    def getCardIdForDefaultEuicc(self) -> int: ...
    def getCarrierConfig(self) -> PersistableBundle: ...
    def getCarrierIdFromSimMccMnc(self) -> int: ...
    def getCarrierRestrictionStatus(self, p0: Executor, p1: Consumer) -> None: ...
    def getCellLocation(self) -> CellLocation: ...
    def getDataActivity(self) -> int: ...
    def getDataState(self) -> int: ...
    def getDeviceSoftwareVersion(self) -> str: ...
    @overload
    def getEmergencyNumberList(self) -> dict: ...
    @overload
    def getEmergencyNumberList(self, p0: int) -> dict: ...
    def getEquivalentHomePlmns(self) -> list: ...
    def getForbiddenPlmns(self) -> Any: ...
    def getGroupIdLevel1(self) -> str: ...
    def getIccAuthentication(self, p0: int, p1: int, p2: str) -> str: ...
    @overload
    def getImei(self, p0: int) -> str: ...
    @overload
    def getImei(self) -> str: ...
    def getLine1Number(self) -> str: ...
    def getManualNetworkSelectionPlmn(self) -> str: ...
    @overload
    def getManufacturerCode(self) -> str: ...
    @overload
    def getManufacturerCode(self, p0: int) -> str: ...
    @staticmethod
    def getMaximumCallComposerPictureSize() -> int: ...
    @overload
    def getMeid(self, p0: int) -> str: ...
    @overload
    def getMeid(self) -> str: ...
    def getMmsUAProfUrl(self) -> str: ...
    def getMmsUserAgent(self) -> str: ...
    @overload
    def getNetworkCountryIso(self, p0: int) -> str: ...
    @overload
    def getNetworkCountryIso(self) -> str: ...
    def getNetworkOperator(self) -> str: ...
    def getNetworkOperatorName(self) -> str: ...
    def getNetworkSelectionMode(self) -> int: ...
    def getNetworkSlicingConfiguration(self, p0: Executor, p1: OutcomeReceiver) -> None: ...
    def getPhoneAccountHandle(self) -> PhoneAccountHandle: ...
    def getPhoneCount(self) -> int: ...
    def getPhoneType(self) -> int: ...
    def getPreferredOpportunisticDataSubscription(self) -> int: ...
    def getPrimaryImei(self) -> str: ...
    @overload
    def getServiceState(self) -> ServiceState: ...
    @overload
    def getServiceState(self, p0: int) -> ServiceState: ...
    def getSimCarrierId(self) -> int: ...
    def getSimCarrierIdName(self) -> str: ...
    def getSimCountryIso(self) -> str: ...
    def getSimOperator(self) -> str: ...
    def getSimOperatorName(self) -> str: ...
    def getSimSerialNumber(self) -> str: ...
    def getSimSpecificCarrierId(self) -> int: ...
    def getSimSpecificCarrierIdName(self) -> str: ...
    @overload
    def getSimState(self, p0: int) -> int: ...
    @overload
    def getSimState(self) -> int: ...
    def getSubscriberId(self) -> str: ...
    def getSupportedModemCount(self) -> int: ...
    def getSupportedRadioAccessFamily(self) -> int: ...
    @overload
    def getTypeAllocationCode(self, p0: int) -> str: ...
    @overload
    def getTypeAllocationCode(self) -> str: ...
    def getUiccCardsInfo(self) -> list: ...
    def getVisualVoicemailPackageName(self) -> str: ...
    def getVoiceMailAlphaTag(self) -> str: ...
    def getVoiceMailNumber(self) -> str: ...
    def getVoiceNetworkType(self) -> int: ...
    def getVoicemailRingtoneUri(self, p0: PhoneAccountHandle) -> Uri: ...
    def hasCarrierPrivileges(self) -> bool: ...
    def hasIccCard(self) -> bool: ...
    def iccCloseLogicalChannel(self, p0: int) -> bool: ...
    def iccExchangeSimIO(self, p0: int, p1: int, p2: int, p3: int, p4: int, p5: str) -> Any: ...
    @overload
    def iccOpenLogicalChannel(self, p0: str) -> IccOpenLogicalChannelResponse: ...
    @overload
    def iccOpenLogicalChannel(self, p0: str, p1: int) -> IccOpenLogicalChannelResponse: ...
    def iccTransmitApduBasicChannel(self, p0: int, p1: int, p2: int, p3: int, p4: int, p5: str) -> str: ...
    def iccTransmitApduLogicalChannel(self, p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: str) -> str: ...
    def isConcurrentVoiceAndDataSupported(self) -> bool: ...
    def isDataCapable(self) -> bool: ...
    def isDataConnectionAllowed(self) -> bool: ...
    def isDataEnabled(self) -> bool: ...
    def isDataEnabledForReason(self, p0: int) -> bool: ...
    def isDataRoamingEnabled(self) -> bool: ...
    def isDeviceSmsCapable(self) -> bool: ...
    def isDeviceVoiceCapable(self) -> bool: ...
    def isEmergencyNumber(self, p0: str) -> bool: ...
    def isHearingAidCompatibilitySupported(self) -> bool: ...
    def isManualNetworkSelectionAllowed(self) -> bool: ...
    def isModemEnabledForSlot(self, p0: int) -> bool: ...
    def isMultiSimSupported(self) -> int: ...
    def isPremiumCapabilityAvailableForPurchase(self, p0: int) -> bool: ...
    def isRadioInterfaceCapabilitySupported(self, p0: str) -> bool: ...
    def isRttSupported(self) -> bool: ...
    def isSmsCapable(self) -> bool: ...
    def isTtyModeSupported(self) -> bool: ...
    def isVoiceCapable(self) -> bool: ...
    def isVoicemailVibrationEnabled(self, p0: PhoneAccountHandle) -> bool: ...
    def isWorldPhone(self) -> bool: ...
    def purchasePremiumCapability(self, p0: int, p1: Executor, p2: Consumer) -> None: ...
    def rebootModem(self) -> None: ...
    @overload
    def registerTelephonyCallback(self, p0: Executor, p1: TelephonyCallback) -> None: ...
    @overload
    def registerTelephonyCallback(self, p0: int, p1: Executor, p2: TelephonyCallback) -> None: ...
    def requestCellInfoUpdate(self, p0: Executor, p1: Any) -> None: ...
    @overload
    def requestNetworkScan(self, p0: int, p1: NetworkScanRequest, p2: Executor, p3: Any) -> NetworkScan: ...
    @overload
    def requestNetworkScan(self, p0: NetworkScanRequest, p1: Executor, p2: Any) -> NetworkScan: ...
    def sendDialerSpecialCode(self, p0: str) -> None: ...
    def sendEnvelopeWithStatus(self, p0: str) -> str: ...
    def sendUssdRequest(self, p0: str, p1: Any, p2: Handler) -> None: ...
    def sendVisualVoicemailSms(self, p0: str, p1: int, p2: str, p3: PendingIntent) -> None: ...
    def setAllowedNetworkTypesForReason(self, p0: int, p1: int) -> None: ...
    def setCallComposerStatus(self, p0: int) -> None: ...
    def setDataEnabled(self, p0: bool) -> None: ...
    def setDataEnabledForReason(self, p0: int, p1: bool) -> None: ...
    def setForbiddenPlmns(self, p0: list) -> int: ...
    def setLine1NumberForDisplay(self, p0: str, p1: str) -> bool: ...
    def setNetworkSelectionModeAutomatic(self) -> None: ...
    @overload
    def setNetworkSelectionModeManual(self, p0: str, p1: bool) -> bool: ...
    @overload
    def setNetworkSelectionModeManual(self, p0: str, p1: bool, p2: int) -> bool: ...
    def setOperatorBrandOverride(self, p0: str) -> bool: ...
    def setPreferredNetworkTypeToGlobal(self) -> bool: ...
    def setPreferredOpportunisticDataSubscription(self, p0: int, p1: bool, p2: Executor, p3: Consumer) -> None: ...
    def setSignalStrengthUpdateRequest(self, p0: SignalStrengthUpdateRequest) -> None: ...
    def setVisualVoicemailSmsFilterSettings(self, p0: VisualVoicemailSmsFilterSettings) -> None: ...
    def setVoiceMailNumber(self, p0: str, p1: str) -> bool: ...
    def setVoicemailRingtoneUri(self, p0: PhoneAccountHandle, p1: Uri) -> None: ...
    def setVoicemailVibrationEnabled(self, p0: PhoneAccountHandle, p1: bool) -> None: ...
    def switchMultiSimConfig(self, p0: int) -> None: ...
    def unregisterTelephonyCallback(self, p0: TelephonyCallback) -> None: ...
    def updateAvailableNetworks(self, p0: list, p1: Executor, p2: Consumer) -> None: ...
    @overload
    def uploadCallComposerPicture(self, p0: InputStream, p1: str, p2: Executor, p3: OutcomeReceiver) -> None: ...
    @overload
    def uploadCallComposerPicture(self, p0: Path, p1: str, p2: Executor, p3: OutcomeReceiver) -> None: ...
    def listen(self, p0: PhoneStateListener, p1: int) -> None: ...
    @overload
    def getDeviceId(self) -> str: ...
    @overload
    def getDeviceId(self, p0: int) -> str: ...

    class UssdResponseCallback:
        def __init__(self) -> None: ...
        def onReceiveUssdResponseFailed(self, p0: "TelephonyManager", p1: str, p2: int) -> None: ...
        def onReceiveUssdResponse(self, p0: "TelephonyManager", p1: str, p2: str) -> None: ...

    class TimeoutException:
        ...

    class NetworkSlicingException:
        def toString(self) -> str: ...

    class ModemErrorException:
        ...

    class CellInfoCallback:
        ERROR_MODEM_ERROR: ClassVar[int]
        ERROR_TIMEOUT: ClassVar[int]
        def __init__(self) -> None: ...
        def onCellInfo(self, p0: list) -> None: ...
        def onError(self, p0: int, p1: Throwable) -> None: ...

    class CallComposerException:
        ERROR_AUTHENTICATION_FAILED: ClassVar[int]
        ERROR_FILE_TOO_LARGE: ClassVar[int]
        ERROR_INPUT_CLOSED: ClassVar[int]
        ERROR_IO_EXCEPTION: ClassVar[int]
        ERROR_NETWORK_UNAVAILABLE: ClassVar[int]
        ERROR_REMOTE_END_CLOSED: ClassVar[int]
        ERROR_UNKNOWN: ClassVar[int]
        def __init__(self, p0: int, p1: IOException) -> None: ...
        def getErrorCode(self) -> int: ...
        def getIOException(self) -> IOException: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class CellIdentity:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getOperatorAlphaLong(self) -> str: ...
    def getOperatorAlphaShort(self) -> str: ...
    def equals(self, p0: Any) -> bool: ...
    def hashCode(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class CellSignalStrengthNr:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    SIGNAL_STRENGTH_GOOD: ClassVar[int]
    SIGNAL_STRENGTH_GREAT: ClassVar[int]
    SIGNAL_STRENGTH_MODERATE: ClassVar[int]
    SIGNAL_STRENGTH_NONE_OR_UNKNOWN: ClassVar[int]
    SIGNAL_STRENGTH_POOR: ClassVar[int]
    def getCsiCqiReport(self) -> list: ...
    def getCsiRsrp(self) -> int: ...
    def getCsiRsrq(self) -> int: ...
    def getCsiSinr(self) -> int: ...
    def getSsRsrp(self) -> int: ...
    def getSsRsrq(self) -> int: ...
    def getCsiCqiTableIndex(self) -> int: ...
    def getSsSinr(self) -> int: ...
    def getTimingAdvanceMicros(self) -> int: ...
    def getAsuLevel(self) -> int: ...
    def getDbm(self) -> int: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def getLevel(self) -> int: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class SignalStrengthUpdateRequest:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getSignalThresholdInfos(self) -> list: ...
    def isReportingRequestedWhileIdle(self) -> bool: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

    class Builder:
        def __init__(self) -> None: ...
        def setReportingRequestedWhileIdle(self, p0: bool) -> Any: ...
        def setSignalThresholdInfos(self, p0: list) -> Any: ...
        def build(self) -> "SignalStrengthUpdateRequest": ...

from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.telephony.mbms.GroupCall import GroupCall
from android.telephony.mbms.GroupCallCallback import GroupCallCallback
from android.telephony.mbms.MbmsGroupCallSessionCallback import MbmsGroupCallSessionCallback
from java.util.concurrent.Executor import Executor

class MbmsGroupCallSession:
    def startGroupCall(self, p0: int, p1: list, p2: list, p3: Executor, p4: GroupCallCallback) -> GroupCall: ...
    def close(self) -> None: ...
    @overload
    @staticmethod
    def create(p0: Context, p1: Executor, p2: MbmsGroupCallSessionCallback) -> "MbmsGroupCallSession": ...
    @overload
    @staticmethod
    def create(p0: Context, p1: int, p2: Executor, p3: MbmsGroupCallSessionCallback) -> "MbmsGroupCallSession": ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class UiccCardInfo:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getCardId(self) -> int: ...
    def getIccId(self) -> str: ...
    def getSlotIndex(self) -> int: ...
    def getEid(self) -> str: ...
    def isEuicc(self) -> bool: ...
    def isMultipleEnabledProfilesSupported(self) -> bool: ...
    def isRemovable(self) -> bool: ...
    def getPhysicalSlotIndex(self) -> int: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def getPorts(self) -> list: ...

from typing import Any, ClassVar, overload

class SmsMessage:
    ENCODING_16BIT: ClassVar[int]
    ENCODING_7BIT: ClassVar[int]
    ENCODING_8BIT: ClassVar[int]
    ENCODING_KSC5601: ClassVar[int]
    ENCODING_UNKNOWN: ClassVar[int]
    FORMAT_3GPP: ClassVar[str]
    FORMAT_3GPP2: ClassVar[str]
    MAX_USER_DATA_BYTES: ClassVar[int]
    MAX_USER_DATA_BYTES_WITH_HEADER: ClassVar[int]
    MAX_USER_DATA_SEPTETS: ClassVar[int]
    MAX_USER_DATA_SEPTETS_WITH_HEADER: ClassVar[int]
    @overload
    @staticmethod
    def calculateLength(p0: str, p1: bool) -> Any: ...
    @overload
    @staticmethod
    def calculateLength(p0: str, p1: bool) -> Any: ...
    @overload
    @staticmethod
    def createFromPdu(p0: Any) -> "SmsMessage": ...
    @overload
    @staticmethod
    def createFromPdu(p0: Any, p1: str) -> "SmsMessage": ...
    def getDisplayMessageBody(self) -> str: ...
    def getEmailBody(self) -> str: ...
    def getDisplayOriginatingAddress(self) -> str: ...
    def getEmailFrom(self) -> str: ...
    def getIndexOnIcc(self) -> int: ...
    def getIndexOnSim(self) -> int: ...
    def getMessageBody(self) -> str: ...
    def getMessageClass(self) -> Any: ...
    def getOriginatingAddress(self) -> str: ...
    def getPdu(self) -> Any: ...
    def getProtocolIdentifier(self) -> int: ...
    def getPseudoSubject(self) -> str: ...
    def getRecipientAddress(self) -> str: ...
    def getServiceCenterAddress(self) -> str: ...
    def getStatusOnIcc(self) -> int: ...
    def getStatusOnSim(self) -> int: ...
    @overload
    @staticmethod
    def getSubmitPdu(p0: str, p1: str, p2: int, p3: Any, p4: bool) -> Any: ...
    @overload
    @staticmethod
    def getSubmitPdu(p0: str, p1: str, p2: str, p3: bool) -> Any: ...
    @staticmethod
    def getTPLayerLengthForPDU(p0: str) -> int: ...
    def getUserData(self) -> Any: ...
    def isCphsMwiMessage(self) -> bool: ...
    def isEmail(self) -> bool: ...
    def isMWIClearMessage(self) -> bool: ...
    def isMWISetMessage(self) -> bool: ...
    def isMwiDontStore(self) -> bool: ...
    def isReplace(self) -> bool: ...
    def isReplyPathPresent(self) -> bool: ...
    def isStatusReportMessage(self) -> bool: ...
    def getStatus(self) -> int: ...
    def getTimestampMillis(self) -> int: ...

    class SubmitPdu:
        encodedMessage: Any
        encodedScAddress: Any
        def toString(self) -> str: ...

    class MessageClass:
        CLASS_0: ClassVar["MessageClass"]
        CLASS_1: ClassVar["MessageClass"]
        CLASS_2: ClassVar["MessageClass"]
        CLASS_3: ClassVar["MessageClass"]
        UNKNOWN: ClassVar["MessageClass"]
        CLASS_0: ClassVar[Any]
        CLASS_1: ClassVar[Any]
        CLASS_2: ClassVar[Any]
        CLASS_3: ClassVar[Any]
        UNKNOWN: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class CellSignalStrengthLte:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    SIGNAL_STRENGTH_GOOD: ClassVar[int]
    SIGNAL_STRENGTH_GREAT: ClassVar[int]
    SIGNAL_STRENGTH_MODERATE: ClassVar[int]
    SIGNAL_STRENGTH_NONE_OR_UNKNOWN: ClassVar[int]
    SIGNAL_STRENGTH_POOR: ClassVar[int]
    def getAsuLevel(self) -> int: ...
    def getCqi(self) -> int: ...
    def getCqiTableIndex(self) -> int: ...
    def getRsrq(self) -> int: ...
    def getRssnr(self) -> int: ...
    def getRsrp(self) -> int: ...
    def getTimingAdvance(self) -> int: ...
    def getDbm(self) -> int: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def getRssi(self) -> int: ...
    def getLevel(self) -> int: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel
from android.telephony.CellIdentity import CellIdentity
from android.telephony.CellIdentityTdscdma import CellIdentityTdscdma
from android.telephony.CellSignalStrength import CellSignalStrength
from android.telephony.CellSignalStrengthTdscdma import CellSignalStrengthTdscdma

class CellInfoTdscdma:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    CONNECTION_NONE: ClassVar[int]
    CONNECTION_PRIMARY_SERVING: ClassVar[int]
    CONNECTION_SECONDARY_SERVING: ClassVar[int]
    CONNECTION_UNKNOWN: ClassVar[int]
    CREATOR: ClassVar[Any]
    UNAVAILABLE: ClassVar[int]
    UNAVAILABLE_LONG: ClassVar[int]
    @overload
    def getCellSignalStrength(self) -> CellSignalStrengthTdscdma: ...
    @overload
    def getCellSignalStrength(self) -> CellSignalStrength: ...
    @overload
    def getCellIdentity(self) -> CellIdentity: ...
    @overload
    def getCellIdentity(self) -> CellIdentityTdscdma: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel
from android.telephony.CellIdentity import CellIdentity
from android.telephony.CellIdentityGsm import CellIdentityGsm
from android.telephony.CellSignalStrength import CellSignalStrength
from android.telephony.CellSignalStrengthGsm import CellSignalStrengthGsm

class CellInfoGsm:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    CONNECTION_NONE: ClassVar[int]
    CONNECTION_PRIMARY_SERVING: ClassVar[int]
    CONNECTION_SECONDARY_SERVING: ClassVar[int]
    CONNECTION_UNKNOWN: ClassVar[int]
    CREATOR: ClassVar[Any]
    UNAVAILABLE: ClassVar[int]
    UNAVAILABLE_LONG: ClassVar[int]
    @overload
    def getCellSignalStrength(self) -> CellSignalStrengthGsm: ...
    @overload
    def getCellSignalStrength(self) -> CellSignalStrength: ...
    @overload
    def getCellIdentity(self) -> CellIdentity: ...
    @overload
    def getCellIdentity(self) -> CellIdentityGsm: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel
from java.time.Period import Period
from java.time.ZonedDateTime import ZonedDateTime
from java.util.Iterator import Iterator

class SubscriptionPlan:
    BYTES_UNKNOWN: ClassVar[int]
    BYTES_UNLIMITED: ClassVar[int]
    CREATOR: ClassVar[Any]
    LIMIT_BEHAVIOR_BILLED: ClassVar[int]
    LIMIT_BEHAVIOR_DISABLED: ClassVar[int]
    LIMIT_BEHAVIOR_THROTTLED: ClassVar[int]
    LIMIT_BEHAVIOR_UNKNOWN: ClassVar[int]
    SUBSCRIPTION_STATUS_ACTIVE: ClassVar[int]
    SUBSCRIPTION_STATUS_INACTIVE: ClassVar[int]
    SUBSCRIPTION_STATUS_SUSPENDED: ClassVar[int]
    SUBSCRIPTION_STATUS_TRIAL: ClassVar[int]
    SUBSCRIPTION_STATUS_UNKNOWN: ClassVar[int]
    TIME_UNKNOWN: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getSummary(self) -> str: ...
    def cycleIterator(self) -> Iterator: ...
    def getDataLimitBehavior(self) -> int: ...
    def getDataLimitBytes(self) -> int: ...
    def getDataUsageBytes(self) -> int: ...
    def getDataUsageTime(self) -> int: ...
    def getNetworkTypes(self) -> Any: ...
    def getPlanEndDate(self) -> ZonedDateTime: ...
    def getSubscriptionStatus(self) -> int: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def getTitle(self) -> str: ...

    class Builder:
        def setSummary(self, p0: str) -> Any: ...
        @staticmethod
        def createRecurring(p0: ZonedDateTime, p1: Period) -> Any: ...
        @staticmethod
        def createNonrecurring(p0: ZonedDateTime, p1: ZonedDateTime) -> Any: ...
        def resetNetworkTypes(self) -> Any: ...
        def setDataLimit(self, p0: int, p1: int) -> Any: ...
        def setDataUsage(self, p0: int, p1: int) -> Any: ...
        def setNetworkTypes(self, p0: Any) -> Any: ...
        def setSubscriptionStatus(self, p0: int) -> Any: ...
        def build(self) -> "SubscriptionPlan": ...
        def setTitle(self, p0: str) -> Any: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class CellSignalStrengthGsm:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    SIGNAL_STRENGTH_GOOD: ClassVar[int]
    SIGNAL_STRENGTH_GREAT: ClassVar[int]
    SIGNAL_STRENGTH_MODERATE: ClassVar[int]
    SIGNAL_STRENGTH_NONE_OR_UNKNOWN: ClassVar[int]
    SIGNAL_STRENGTH_POOR: ClassVar[int]
    def getBitErrorRate(self) -> int: ...
    def getAsuLevel(self) -> int: ...
    def getTimingAdvance(self) -> int: ...
    def getDbm(self) -> int: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def getRssi(self) -> int: ...
    def getLevel(self) -> int: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class CellSignalStrengthCdma:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    SIGNAL_STRENGTH_GOOD: ClassVar[int]
    SIGNAL_STRENGTH_GREAT: ClassVar[int]
    SIGNAL_STRENGTH_MODERATE: ClassVar[int]
    SIGNAL_STRENGTH_NONE_OR_UNKNOWN: ClassVar[int]
    SIGNAL_STRENGTH_POOR: ClassVar[int]
    def getCdmaDbm(self) -> int: ...
    def getCdmaEcio(self) -> int: ...
    def getEvdoDbm(self) -> int: ...
    def getEvdoEcio(self) -> int: ...
    def getEvdoSnr(self) -> int: ...
    def getCdmaLevel(self) -> int: ...
    def getEvdoLevel(self) -> int: ...
    def getAsuLevel(self) -> int: ...
    def getDbm(self) -> int: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def getLevel(self) -> int: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class CellSignalStrengthTdscdma:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    SIGNAL_STRENGTH_GOOD: ClassVar[int]
    SIGNAL_STRENGTH_GREAT: ClassVar[int]
    SIGNAL_STRENGTH_MODERATE: ClassVar[int]
    SIGNAL_STRENGTH_NONE_OR_UNKNOWN: ClassVar[int]
    SIGNAL_STRENGTH_POOR: ClassVar[int]
    def getRscp(self) -> int: ...
    def getAsuLevel(self) -> int: ...
    def getDbm(self) -> int: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def getLevel(self) -> int: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class VisualVoicemailSmsFilterSettings:
    CREATOR: ClassVar[Any]
    DESTINATION_PORT_ANY: ClassVar[int]
    DESTINATION_PORT_DATA_SMS: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    clientPrefix: str
    destinationPort: int
    originatingNumbers: list
    def toString(self) -> str: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

    class Builder:
        def __init__(self) -> None: ...
        def setDestinationPort(self, p0: int) -> Any: ...
        def setOriginatingNumbers(self, p0: list) -> Any: ...
        def setClientPrefix(self, p0: str) -> Any: ...
        def build(self) -> "VisualVoicemailSmsFilterSettings": ...

from typing import Any, ClassVar, overload
from android.content.Intent import Intent
from android.os.IBinder import IBinder
from android.telecom.PhoneAccountHandle import PhoneAccountHandle
from android.telephony.VisualVoicemailSms import VisualVoicemailSms

class VisualVoicemailService:
    SERVICE_INTERFACE: ClassVar[str]
    START_CONTINUATION_MASK: ClassVar[int]
    START_FLAG_REDELIVERY: ClassVar[int]
    START_FLAG_RETRY: ClassVar[int]
    START_NOT_STICKY: ClassVar[int]
    START_REDELIVER_INTENT: ClassVar[int]
    START_STICKY: ClassVar[int]
    START_STICKY_COMPATIBILITY: ClassVar[int]
    STOP_FOREGROUND_DETACH: ClassVar[int]
    STOP_FOREGROUND_LEGACY: ClassVar[int]
    STOP_FOREGROUND_REMOVE: ClassVar[int]
    TRIM_MEMORY_BACKGROUND: ClassVar[int]
    TRIM_MEMORY_COMPLETE: ClassVar[int]
    TRIM_MEMORY_MODERATE: ClassVar[int]
    TRIM_MEMORY_RUNNING_CRITICAL: ClassVar[int]
    TRIM_MEMORY_RUNNING_LOW: ClassVar[int]
    TRIM_MEMORY_RUNNING_MODERATE: ClassVar[int]
    TRIM_MEMORY_UI_HIDDEN: ClassVar[int]
    ACCESSIBILITY_SERVICE: ClassVar[str]
    ACCOUNT_SERVICE: ClassVar[str]
    ACTIVITY_SERVICE: ClassVar[str]
    ADVANCED_PROTECTION_SERVICE: ClassVar[str]
    ALARM_SERVICE: ClassVar[str]
    APPWIDGET_SERVICE: ClassVar[str]
    APP_FUNCTION_SERVICE: ClassVar[str]
    APP_OPS_SERVICE: ClassVar[str]
    APP_SEARCH_SERVICE: ClassVar[str]
    AUDIO_SERVICE: ClassVar[str]
    BATTERY_SERVICE: ClassVar[str]
    BIND_ABOVE_CLIENT: ClassVar[int]
    BIND_ADJUST_WITH_ACTIVITY: ClassVar[int]
    BIND_ALLOW_ACTIVITY_STARTS: ClassVar[int]
    BIND_ALLOW_OOM_MANAGEMENT: ClassVar[int]
    BIND_AUTO_CREATE: ClassVar[int]
    BIND_DEBUG_UNBIND: ClassVar[int]
    BIND_EXTERNAL_SERVICE: ClassVar[int]
    BIND_EXTERNAL_SERVICE_LONG: ClassVar[int]
    BIND_IMPORTANT: ClassVar[int]
    BIND_INCLUDE_CAPABILITIES: ClassVar[int]
    BIND_NOT_FOREGROUND: ClassVar[int]
    BIND_NOT_PERCEPTIBLE: ClassVar[int]
    BIND_PACKAGE_ISOLATED_PROCESS: ClassVar[int]
    BIND_SHARED_ISOLATED_PROCESS: ClassVar[int]
    BIND_WAIVE_PRIORITY: ClassVar[int]
    BIOMETRIC_SERVICE: ClassVar[str]
    BLOB_STORE_SERVICE: ClassVar[str]
    BLUETOOTH_SERVICE: ClassVar[str]
    BUGREPORT_SERVICE: ClassVar[str]
    CAMERA_SERVICE: ClassVar[str]
    CAPTIONING_SERVICE: ClassVar[str]
    CARRIER_CONFIG_SERVICE: ClassVar[str]
    CLIPBOARD_SERVICE: ClassVar[str]
    COMPANION_DEVICE_SERVICE: ClassVar[str]
    CONNECTIVITY_DIAGNOSTICS_SERVICE: ClassVar[str]
    CONNECTIVITY_SERVICE: ClassVar[str]
    CONSUMER_IR_SERVICE: ClassVar[str]
    CONTACT_KEYS_SERVICE: ClassVar[str]
    CONTEXT_IGNORE_SECURITY: ClassVar[int]
    CONTEXT_INCLUDE_CODE: ClassVar[int]
    CONTEXT_RESTRICTED: ClassVar[int]
    CREDENTIAL_SERVICE: ClassVar[str]
    CROSS_PROFILE_APPS_SERVICE: ClassVar[str]
    DEVICE_ID_DEFAULT: ClassVar[int]
    DEVICE_ID_INVALID: ClassVar[int]
    DEVICE_LOCK_SERVICE: ClassVar[str]
    DEVICE_POLICY_SERVICE: ClassVar[str]
    DISPLAY_HASH_SERVICE: ClassVar[str]
    DISPLAY_SERVICE: ClassVar[str]
    DOMAIN_VERIFICATION_SERVICE: ClassVar[str]
    DOWNLOAD_SERVICE: ClassVar[str]
    DROPBOX_SERVICE: ClassVar[str]
    EUICC_SERVICE: ClassVar[str]
    FILE_INTEGRITY_SERVICE: ClassVar[str]
    FINGERPRINT_SERVICE: ClassVar[str]
    GAME_SERVICE: ClassVar[str]
    GRAMMATICAL_INFLECTION_SERVICE: ClassVar[str]
    HARDWARE_PROPERTIES_SERVICE: ClassVar[str]
    HEALTHCONNECT_SERVICE: ClassVar[str]
    INPUT_METHOD_SERVICE: ClassVar[str]
    INPUT_SERVICE: ClassVar[str]
    IPSEC_SERVICE: ClassVar[str]
    JOB_SCHEDULER_SERVICE: ClassVar[str]
    KEYGUARD_SERVICE: ClassVar[str]
    KEYSTORE_SERVICE: ClassVar[str]
    LAUNCHER_APPS_SERVICE: ClassVar[str]
    LAYOUT_INFLATER_SERVICE: ClassVar[str]
    LOCALE_SERVICE: ClassVar[str]
    LOCATION_SERVICE: ClassVar[str]
    MEDIA_COMMUNICATION_SERVICE: ClassVar[str]
    MEDIA_METRICS_SERVICE: ClassVar[str]
    MEDIA_PROJECTION_SERVICE: ClassVar[str]
    MEDIA_QUALITY_SERVICE: ClassVar[str]
    MEDIA_ROUTER_SERVICE: ClassVar[str]
    MEDIA_SESSION_SERVICE: ClassVar[str]
    MIDI_SERVICE: ClassVar[str]
    MODE_APPEND: ClassVar[int]
    MODE_ENABLE_WRITE_AHEAD_LOGGING: ClassVar[int]
    MODE_MULTI_PROCESS: ClassVar[int]
    MODE_NO_LOCALIZED_COLLATORS: ClassVar[int]
    MODE_PRIVATE: ClassVar[int]
    MODE_WORLD_READABLE: ClassVar[int]
    MODE_WORLD_WRITEABLE: ClassVar[int]
    NETWORK_STATS_SERVICE: ClassVar[str]
    NFC_SERVICE: ClassVar[str]
    NOTIFICATION_SERVICE: ClassVar[str]
    NSD_SERVICE: ClassVar[str]
    OVERLAY_SERVICE: ClassVar[str]
    PEOPLE_SERVICE: ClassVar[str]
    PERFORMANCE_HINT_SERVICE: ClassVar[str]
    PERSISTENT_DATA_BLOCK_SERVICE: ClassVar[str]
    POWER_SERVICE: ClassVar[str]
    PRINT_SERVICE: ClassVar[str]
    PROFILING_SERVICE: ClassVar[str]
    RECEIVER_EXPORTED: ClassVar[int]
    RECEIVER_NOT_EXPORTED: ClassVar[int]
    RECEIVER_VISIBLE_TO_INSTANT_APPS: ClassVar[int]
    RESTRICTIONS_SERVICE: ClassVar[str]
    ROLE_SERVICE: ClassVar[str]
    SATELLITE_SERVICE: ClassVar[str]
    SEARCH_SERVICE: ClassVar[str]
    SECURITY_STATE_SERVICE: ClassVar[str]
    SENSOR_SERVICE: ClassVar[str]
    SHORTCUT_SERVICE: ClassVar[str]
    STATUS_BAR_SERVICE: ClassVar[str]
    STORAGE_SERVICE: ClassVar[str]
    STORAGE_STATS_SERVICE: ClassVar[str]
    SYSTEM_HEALTH_SERVICE: ClassVar[str]
    TELECOM_SERVICE: ClassVar[str]
    TELEPHONY_IMS_SERVICE: ClassVar[str]
    TELEPHONY_SERVICE: ClassVar[str]
    TELEPHONY_SUBSCRIPTION_SERVICE: ClassVar[str]
    TETHERING_SERVICE: ClassVar[str]
    TEXT_CLASSIFICATION_SERVICE: ClassVar[str]
    TEXT_SERVICES_MANAGER_SERVICE: ClassVar[str]
    TV_AD_SERVICE: ClassVar[str]
    TV_INPUT_SERVICE: ClassVar[str]
    TV_INTERACTIVE_APP_SERVICE: ClassVar[str]
    UI_MODE_SERVICE: ClassVar[str]
    USAGE_STATS_SERVICE: ClassVar[str]
    USB_SERVICE: ClassVar[str]
    USER_SERVICE: ClassVar[str]
    VIBRATOR_MANAGER_SERVICE: ClassVar[str]
    VIBRATOR_SERVICE: ClassVar[str]
    VIRTUAL_DEVICE_SERVICE: ClassVar[str]
    VPN_MANAGEMENT_SERVICE: ClassVar[str]
    WALLPAPER_SERVICE: ClassVar[str]
    WIFI_AWARE_SERVICE: ClassVar[str]
    WIFI_P2P_SERVICE: ClassVar[str]
    WIFI_RTT_RANGING_SERVICE: ClassVar[str]
    WIFI_SERVICE: ClassVar[str]
    WINDOW_SERVICE: ClassVar[str]
    def __init__(self) -> None: ...
    def onSimRemoved(self, p0: Any, p1: PhoneAccountHandle) -> None: ...
    def onSmsReceived(self, p0: Any, p1: VisualVoicemailSms) -> None: ...
    def onCellServiceConnected(self, p0: Any, p1: PhoneAccountHandle) -> None: ...
    def onStopped(self, p0: Any) -> None: ...
    def onBind(self, p0: Intent) -> IBinder: ...

    class VisualVoicemailTask:
        def equals(self, p0: Any) -> bool: ...
        def hashCode(self) -> int: ...
        def finish(self) -> None: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class UiccPortInfo:
    CREATOR: ClassVar[Any]
    ICCID_REDACTED: ClassVar[str]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getIccId(self) -> str: ...
    def getPortIndex(self) -> int: ...
    def getLogicalSlotIndex(self) -> int: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def isActive(self) -> bool: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class ServiceState:
    CREATOR: ClassVar[Any]
    DUPLEX_MODE_FDD: ClassVar[int]
    DUPLEX_MODE_TDD: ClassVar[int]
    DUPLEX_MODE_UNKNOWN: ClassVar[int]
    STATE_EMERGENCY_ONLY: ClassVar[int]
    STATE_IN_SERVICE: ClassVar[int]
    STATE_OUT_OF_SERVICE: ClassVar[int]
    STATE_POWER_OFF: ClassVar[int]
    UNKNOWN_ID: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    @overload
    def __init__(self, p0: Parcel) -> None: ...
    @overload
    def __init__(self, p0: "ServiceState") -> None: ...
    @overload
    def __init__(self) -> None: ...
    def getOperatorAlphaLong(self) -> str: ...
    def getOperatorAlphaShort(self) -> str: ...
    def getNetworkRegistrationInfoList(self) -> list: ...
    def getCdmaNetworkId(self) -> int: ...
    def getCdmaSystemId(self) -> int: ...
    def getCellBandwidths(self) -> Any: ...
    def getChannelNumber(self) -> int: ...
    def getDuplexMode(self) -> int: ...
    def getIsManualSelection(self) -> bool: ...
    def isSearching(self) -> bool: ...
    def isUsingNonTerrestrialNetwork(self) -> bool: ...
    def setIsManualSelection(self, p0: bool) -> None: ...
    def setOperatorName(self, p0: str, p1: str, p2: str) -> None: ...
    def setRoaming(self, p0: bool) -> None: ...
    def setStateOff(self) -> None: ...
    def setStateOutOfService(self) -> None: ...
    def getOperatorNumeric(self) -> str: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def getState(self) -> int: ...
    def setState(self, p0: int) -> None: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def getRoaming(self) -> bool: ...

from typing import Any, ClassVar, overload
from android.os.Bundle import Bundle
from android.os.Parcel import Parcel
from android.telecom.PhoneAccountHandle import PhoneAccountHandle

class VisualVoicemailSms:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getMessageBody(self) -> str: ...
    def getPhoneAccountHandle(self) -> PhoneAccountHandle: ...
    def getFields(self) -> Bundle: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def getPrefix(self) -> str: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel
from android.telephony.ClosedSubscriberGroupInfo import ClosedSubscriberGroupInfo

class CellIdentityLte:
    CREATOR: ClassVar[Any]
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getMcc(self) -> int: ...
    def getMnc(self) -> int: ...
    def getPci(self) -> int: ...
    def getTac(self) -> int: ...
    def getBands(self) -> Any: ...
    def getCi(self) -> int: ...
    def getBandwidth(self) -> int: ...
    def getEarfcn(self) -> int: ...
    def getClosedSubscriberGroupInfo(self) -> ClosedSubscriberGroupInfo: ...
    def getAdditionalPlmns(self) -> set: ...
    def getMccString(self) -> str: ...
    def getMncString(self) -> str: ...
    def getMobileNetworkOperator(self) -> str: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class SignalStrength:
    CREATOR: ClassVar[Any]
    INVALID: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def __init__(self, p0: "SignalStrength") -> None: ...
    def getCdmaDbm(self) -> int: ...
    def getCdmaEcio(self) -> int: ...
    @overload
    def getCellSignalStrengths(self, p0: type) -> list: ...
    @overload
    def getCellSignalStrengths(self) -> list: ...
    def getEvdoDbm(self) -> int: ...
    def getEvdoEcio(self) -> int: ...
    def getEvdoSnr(self) -> int: ...
    def getGsmBitErrorRate(self) -> int: ...
    def getGsmSignalStrength(self) -> int: ...
    def isGsm(self) -> bool: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def getTimestampMillis(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def getLevel(self) -> int: ...

from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.telephony.mbms.MbmsStreamingSessionCallback import MbmsStreamingSessionCallback
from android.telephony.mbms.StreamingService import StreamingService
from android.telephony.mbms.StreamingServiceCallback import StreamingServiceCallback
from android.telephony.mbms.StreamingServiceInfo import StreamingServiceInfo
from java.util.concurrent.Executor import Executor

class MbmsStreamingSession:
    def requestUpdateStreamingServices(self, p0: list) -> None: ...
    def startStreaming(self, p0: StreamingServiceInfo, p1: Executor, p2: StreamingServiceCallback) -> StreamingService: ...
    def close(self) -> None: ...
    @overload
    @staticmethod
    def create(p0: Context, p1: Executor, p2: MbmsStreamingSessionCallback) -> "MbmsStreamingSession": ...
    @overload
    @staticmethod
    def create(p0: Context, p1: Executor, p2: int, p3: MbmsStreamingSessionCallback) -> "MbmsStreamingSession": ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class RadioAccessSpecifier:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def __init__(self, p0: int, p1: Any, p2: Any) -> None: ...
    def getChannels(self) -> Any: ...
    def getBands(self) -> Any: ...
    def getRadioAccessNetwork(self) -> int: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class SignalThresholdInfo:
    CREATOR: ClassVar[Any]
    SIGNAL_MEASUREMENT_TYPE_ECNO: ClassVar[int]
    SIGNAL_MEASUREMENT_TYPE_RSCP: ClassVar[int]
    SIGNAL_MEASUREMENT_TYPE_RSRP: ClassVar[int]
    SIGNAL_MEASUREMENT_TYPE_RSRQ: ClassVar[int]
    SIGNAL_MEASUREMENT_TYPE_RSSI: ClassVar[int]
    SIGNAL_MEASUREMENT_TYPE_RSSNR: ClassVar[int]
    SIGNAL_MEASUREMENT_TYPE_SSRSRP: ClassVar[int]
    SIGNAL_MEASUREMENT_TYPE_SSRSRQ: ClassVar[int]
    SIGNAL_MEASUREMENT_TYPE_SSSINR: ClassVar[int]
    SIGNAL_MEASUREMENT_TYPE_UNKNOWN: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getHysteresisDb(self) -> int: ...
    @staticmethod
    def getMaximumNumberOfThresholdsAllowed() -> int: ...
    @staticmethod
    def getMinimumNumberOfThresholdsAllowed() -> int: ...
    def getRadioAccessNetworkType(self) -> int: ...
    def getSignalMeasurementType(self) -> int: ...
    def getThresholds(self) -> Any: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

    class Builder:
        def __init__(self) -> None: ...
        def setRadioAccessNetworkType(self, p0: int) -> Any: ...
        def setHysteresisDb(self, p0: int) -> Any: ...
        def setSignalMeasurementType(self, p0: int) -> Any: ...
        def setThresholds(self, p0: Any) -> Any: ...
        def build(self) -> "SignalThresholdInfo": ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel
from android.telephony.CellIdentity import CellIdentity
from android.telephony.CellIdentityLte import CellIdentityLte
from android.telephony.CellSignalStrength import CellSignalStrength
from android.telephony.CellSignalStrengthLte import CellSignalStrengthLte

class CellInfoLte:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    CONNECTION_NONE: ClassVar[int]
    CONNECTION_PRIMARY_SERVING: ClassVar[int]
    CONNECTION_SECONDARY_SERVING: ClassVar[int]
    CONNECTION_UNKNOWN: ClassVar[int]
    CREATOR: ClassVar[Any]
    UNAVAILABLE: ClassVar[int]
    UNAVAILABLE_LONG: ClassVar[int]
    @overload
    def getCellSignalStrength(self) -> CellSignalStrengthLte: ...
    @overload
    def getCellSignalStrength(self) -> CellSignalStrength: ...
    @overload
    def getCellIdentity(self) -> CellIdentity: ...
    @overload
    def getCellIdentity(self) -> CellIdentityLte: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class ClosedSubscriberGroupInfo:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getCsgIdentity(self) -> int: ...
    def getCsgIndicator(self) -> bool: ...
    def getHomeNodebName(self) -> str: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel
from android.telephony.ClosedSubscriberGroupInfo import ClosedSubscriberGroupInfo

class CellIdentityTdscdma:
    CREATOR: ClassVar[Any]
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getCpid(self) -> int: ...
    def getCid(self) -> int: ...
    def getLac(self) -> int: ...
    def getClosedSubscriberGroupInfo(self) -> ClosedSubscriberGroupInfo: ...
    def getAdditionalPlmns(self) -> set: ...
    def getMccString(self) -> str: ...
    def getMncString(self) -> str: ...
    def getMobileNetworkOperator(self) -> str: ...
    def getUarfcn(self) -> int: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class CellSignalStrengthWcdma:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    SIGNAL_STRENGTH_GOOD: ClassVar[int]
    SIGNAL_STRENGTH_GREAT: ClassVar[int]
    SIGNAL_STRENGTH_MODERATE: ClassVar[int]
    SIGNAL_STRENGTH_NONE_OR_UNKNOWN: ClassVar[int]
    SIGNAL_STRENGTH_POOR: ClassVar[int]
    def getEcNo(self) -> int: ...
    def getAsuLevel(self) -> int: ...
    def getDbm(self) -> int: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def getLevel(self) -> int: ...

from typing import Any, ClassVar, overload

class CellSignalStrength:
    SIGNAL_STRENGTH_GOOD: ClassVar[int]
    SIGNAL_STRENGTH_GREAT: ClassVar[int]
    SIGNAL_STRENGTH_MODERATE: ClassVar[int]
    SIGNAL_STRENGTH_NONE_OR_UNKNOWN: ClassVar[int]
    SIGNAL_STRENGTH_POOR: ClassVar[int]
    def getAsuLevel(self) -> int: ...
    def getDbm(self) -> int: ...
    def equals(self, p0: Any) -> bool: ...
    def hashCode(self) -> int: ...
    def getLevel(self) -> int: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel
from android.telephony.CellIdentity import CellIdentity
from android.telephony.CellIdentityCdma import CellIdentityCdma
from android.telephony.CellSignalStrength import CellSignalStrength
from android.telephony.CellSignalStrengthCdma import CellSignalStrengthCdma

class CellInfoCdma:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    CONNECTION_NONE: ClassVar[int]
    CONNECTION_PRIMARY_SERVING: ClassVar[int]
    CONNECTION_SECONDARY_SERVING: ClassVar[int]
    CONNECTION_UNKNOWN: ClassVar[int]
    CREATOR: ClassVar[Any]
    UNAVAILABLE: ClassVar[int]
    UNAVAILABLE_LONG: ClassVar[int]
    @overload
    def getCellSignalStrength(self) -> CellSignalStrengthCdma: ...
    @overload
    def getCellSignalStrength(self) -> CellSignalStrength: ...
    @overload
    def getCellIdentity(self) -> CellIdentity: ...
    @overload
    def getCellIdentity(self) -> CellIdentityCdma: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class IccOpenLogicalChannelResponse:
    CREATOR: ClassVar[Any]
    INVALID_CHANNEL: ClassVar[int]
    STATUS_MISSING_RESOURCE: ClassVar[int]
    STATUS_NO_ERROR: ClassVar[int]
    STATUS_NO_SUCH_ELEMENT: ClassVar[int]
    STATUS_UNKNOWN_ERROR: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getStatus(self) -> int: ...
    def toString(self) -> str: ...
    def getChannel(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def getSelectResponse(self) -> Any: ...

from typing import Any, ClassVar, overload
from android.text.Editable import Editable

class PhoneNumberFormattingTextWatcher:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, p0: str) -> None: ...
    def afterTextChanged(self, p0: Editable) -> None: ...
    def beforeTextChanged(self, p0: str, p1: int, p2: int, p3: int) -> None: ...
    def onTextChanged(self, p0: str, p1: int, p2: int, p3: int) -> None: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class CellIdentityNr:
    CREATOR: ClassVar[Any]
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getNci(self) -> int: ...
    def getPci(self) -> int: ...
    def getTac(self) -> int: ...
    def getBands(self) -> Any: ...
    def getAdditionalPlmns(self) -> set: ...
    def getMccString(self) -> str: ...
    def getMncString(self) -> str: ...
    def getNrarfcn(self) -> int: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload

class TelephonyScanManager:
    def __init__(self) -> None: ...

    class NetworkScanCallback:
        def __init__(self) -> None: ...
        def onError(self, p0: int) -> None: ...
        def onComplete(self) -> None: ...
        def onResults(self, p0: list) -> None: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class NeighboringCellInfo:
    CREATOR: ClassVar[Any]
    UNKNOWN_CID: ClassVar[int]
    UNKNOWN_RSSI: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, p0: int, p1: int) -> None: ...
    @overload
    def __init__(self, p0: int, p1: str, p2: int) -> None: ...
    @overload
    def __init__(self, p0: Parcel) -> None: ...
    def getNetworkType(self) -> int: ...
    def getPsc(self) -> int: ...
    def getCid(self) -> int: ...
    def getLac(self) -> int: ...
    def toString(self) -> str: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def getRssi(self) -> int: ...
    def setRssi(self, p0: int) -> None: ...
    def setCid(self, p0: int) -> None: ...

from typing import Any, ClassVar, overload
from android.app.PendingIntent import PendingIntent
from android.content.Context import Context
from android.database.CursorWindow import CursorWindow
from android.net.Uri import Uri
from android.os.Bundle import Bundle
from java.util.concurrent.Executor import Executor

class SmsManager:
    EXTRA_MMS_DATA: ClassVar[str]
    EXTRA_MMS_HTTP_STATUS: ClassVar[str]
    MMS_CONFIG_ALIAS_ENABLED: ClassVar[str]
    MMS_CONFIG_ALIAS_MAX_CHARS: ClassVar[str]
    MMS_CONFIG_ALIAS_MIN_CHARS: ClassVar[str]
    MMS_CONFIG_ALLOW_ATTACH_AUDIO: ClassVar[str]
    MMS_CONFIG_APPEND_TRANSACTION_ID: ClassVar[str]
    MMS_CONFIG_EMAIL_GATEWAY_NUMBER: ClassVar[str]
    MMS_CONFIG_GROUP_MMS_ENABLED: ClassVar[str]
    MMS_CONFIG_HTTP_PARAMS: ClassVar[str]
    MMS_CONFIG_HTTP_SOCKET_TIMEOUT: ClassVar[str]
    MMS_CONFIG_MAX_IMAGE_HEIGHT: ClassVar[str]
    MMS_CONFIG_MAX_IMAGE_WIDTH: ClassVar[str]
    MMS_CONFIG_MAX_MESSAGE_SIZE: ClassVar[str]
    MMS_CONFIG_MESSAGE_TEXT_MAX_SIZE: ClassVar[str]
    MMS_CONFIG_MMS_DELIVERY_REPORT_ENABLED: ClassVar[str]
    MMS_CONFIG_MMS_ENABLED: ClassVar[str]
    MMS_CONFIG_MMS_READ_REPORT_ENABLED: ClassVar[str]
    MMS_CONFIG_MULTIPART_SMS_ENABLED: ClassVar[str]
    MMS_CONFIG_NAI_SUFFIX: ClassVar[str]
    MMS_CONFIG_NOTIFY_WAP_MMSC_ENABLED: ClassVar[str]
    MMS_CONFIG_RECIPIENT_LIMIT: ClassVar[str]
    MMS_CONFIG_SEND_MULTIPART_SMS_AS_SEPARATE_MESSAGES: ClassVar[str]
    MMS_CONFIG_SHOW_CELL_BROADCAST_APP_LINKS: ClassVar[str]
    MMS_CONFIG_SMS_DELIVERY_REPORT_ENABLED: ClassVar[str]
    MMS_CONFIG_SMS_TO_MMS_TEXT_LENGTH_THRESHOLD: ClassVar[str]
    MMS_CONFIG_SMS_TO_MMS_TEXT_THRESHOLD: ClassVar[str]
    MMS_CONFIG_SUBJECT_MAX_LENGTH: ClassVar[str]
    MMS_CONFIG_SUPPORT_HTTP_CHARSET_HEADER: ClassVar[str]
    MMS_CONFIG_SUPPORT_MMS_CONTENT_DISPOSITION: ClassVar[str]
    MMS_CONFIG_UA_PROF_TAG_NAME: ClassVar[str]
    MMS_CONFIG_UA_PROF_URL: ClassVar[str]
    MMS_CONFIG_USER_AGENT: ClassVar[str]
    MMS_ERROR_CONFIGURATION_ERROR: ClassVar[int]
    MMS_ERROR_DATA_DISABLED: ClassVar[int]
    MMS_ERROR_HTTP_FAILURE: ClassVar[int]
    MMS_ERROR_INACTIVE_SUBSCRIPTION: ClassVar[int]
    MMS_ERROR_INVALID_APN: ClassVar[int]
    MMS_ERROR_INVALID_SUBSCRIPTION_ID: ClassVar[int]
    MMS_ERROR_IO_ERROR: ClassVar[int]
    MMS_ERROR_MMS_DISABLED_BY_CARRIER: ClassVar[int]
    MMS_ERROR_NO_DATA_NETWORK: ClassVar[int]
    MMS_ERROR_RETRY: ClassVar[int]
    MMS_ERROR_UNABLE_CONNECT_MMS: ClassVar[int]
    MMS_ERROR_UNSPECIFIED: ClassVar[int]
    RESULT_BLUETOOTH_DISCONNECTED: ClassVar[int]
    RESULT_CANCELLED: ClassVar[int]
    RESULT_ENCODING_ERROR: ClassVar[int]
    RESULT_ERROR_FDN_CHECK_FAILURE: ClassVar[int]
    RESULT_ERROR_GENERIC_FAILURE: ClassVar[int]
    RESULT_ERROR_LIMIT_EXCEEDED: ClassVar[int]
    RESULT_ERROR_NONE: ClassVar[int]
    RESULT_ERROR_NO_SERVICE: ClassVar[int]
    RESULT_ERROR_NULL_PDU: ClassVar[int]
    RESULT_ERROR_RADIO_OFF: ClassVar[int]
    RESULT_ERROR_SHORT_CODE_NEVER_ALLOWED: ClassVar[int]
    RESULT_ERROR_SHORT_CODE_NOT_ALLOWED: ClassVar[int]
    RESULT_INTERNAL_ERROR: ClassVar[int]
    RESULT_INVALID_ARGUMENTS: ClassVar[int]
    RESULT_INVALID_BLUETOOTH_ADDRESS: ClassVar[int]
    RESULT_INVALID_SMSC_ADDRESS: ClassVar[int]
    RESULT_INVALID_SMS_FORMAT: ClassVar[int]
    RESULT_INVALID_STATE: ClassVar[int]
    RESULT_MODEM_ERROR: ClassVar[int]
    RESULT_NETWORK_ERROR: ClassVar[int]
    RESULT_NETWORK_REJECT: ClassVar[int]
    RESULT_NO_BLUETOOTH_SERVICE: ClassVar[int]
    RESULT_NO_DEFAULT_SMS_APP: ClassVar[int]
    RESULT_NO_MEMORY: ClassVar[int]
    RESULT_NO_RESOURCES: ClassVar[int]
    RESULT_OPERATION_NOT_ALLOWED: ClassVar[int]
    RESULT_RADIO_NOT_AVAILABLE: ClassVar[int]
    RESULT_RECEIVE_DISPATCH_FAILURE: ClassVar[int]
    RESULT_RECEIVE_INJECTED_NULL_PDU: ClassVar[int]
    RESULT_RECEIVE_NULL_MESSAGE_FROM_RIL: ClassVar[int]
    RESULT_RECEIVE_RUNTIME_EXCEPTION: ClassVar[int]
    RESULT_RECEIVE_SQL_EXCEPTION: ClassVar[int]
    RESULT_RECEIVE_URI_EXCEPTION: ClassVar[int]
    RESULT_RECEIVE_WHILE_ENCRYPTED: ClassVar[int]
    RESULT_REMOTE_EXCEPTION: ClassVar[int]
    RESULT_REQUEST_NOT_SUPPORTED: ClassVar[int]
    RESULT_RIL_ABORTED: ClassVar[int]
    RESULT_RIL_ACCESS_BARRED: ClassVar[int]
    RESULT_RIL_BLOCKED_DUE_TO_CALL: ClassVar[int]
    RESULT_RIL_CANCELLED: ClassVar[int]
    RESULT_RIL_DEVICE_IN_USE: ClassVar[int]
    RESULT_RIL_ENCODING_ERR: ClassVar[int]
    RESULT_RIL_GENERIC_ERROR: ClassVar[int]
    RESULT_RIL_INTERNAL_ERR: ClassVar[int]
    RESULT_RIL_INVALID_ARGUMENTS: ClassVar[int]
    RESULT_RIL_INVALID_MODEM_STATE: ClassVar[int]
    RESULT_RIL_INVALID_RESPONSE: ClassVar[int]
    RESULT_RIL_INVALID_SIM_STATE: ClassVar[int]
    RESULT_RIL_INVALID_SMSC_ADDRESS: ClassVar[int]
    RESULT_RIL_INVALID_SMS_FORMAT: ClassVar[int]
    RESULT_RIL_INVALID_STATE: ClassVar[int]
    RESULT_RIL_MODEM_ERR: ClassVar[int]
    RESULT_RIL_NETWORK_ERR: ClassVar[int]
    RESULT_RIL_NETWORK_NOT_READY: ClassVar[int]
    RESULT_RIL_NETWORK_REJECT: ClassVar[int]
    RESULT_RIL_NO_MEMORY: ClassVar[int]
    RESULT_RIL_NO_NETWORK_FOUND: ClassVar[int]
    RESULT_RIL_NO_RESOURCES: ClassVar[int]
    RESULT_RIL_NO_SMS_TO_ACK: ClassVar[int]
    RESULT_RIL_NO_SUBSCRIPTION: ClassVar[int]
    RESULT_RIL_OPERATION_NOT_ALLOWED: ClassVar[int]
    RESULT_RIL_RADIO_NOT_AVAILABLE: ClassVar[int]
    RESULT_RIL_REQUEST_NOT_SUPPORTED: ClassVar[int]
    RESULT_RIL_REQUEST_RATE_LIMITED: ClassVar[int]
    RESULT_RIL_SIMULTANEOUS_SMS_AND_CALL_NOT_ALLOWED: ClassVar[int]
    RESULT_RIL_SIM_ABSENT: ClassVar[int]
    RESULT_RIL_SIM_BUSY: ClassVar[int]
    RESULT_RIL_SIM_ERROR: ClassVar[int]
    RESULT_RIL_SIM_FULL: ClassVar[int]
    RESULT_RIL_SIM_PIN2: ClassVar[int]
    RESULT_RIL_SIM_PUK2: ClassVar[int]
    RESULT_RIL_SMS_SEND_FAIL_RETRY: ClassVar[int]
    RESULT_RIL_SUBSCRIPTION_NOT_AVAILABLE: ClassVar[int]
    RESULT_RIL_SYSTEM_ERR: ClassVar[int]
    RESULT_SMS_BLOCKED_DURING_EMERGENCY: ClassVar[int]
    RESULT_SMS_SEND_RETRY_FAILED: ClassVar[int]
    RESULT_SYSTEM_ERROR: ClassVar[int]
    RESULT_UNEXPECTED_EVENT_STOP_SENDING: ClassVar[int]
    RESULT_USER_NOT_ALLOWED: ClassVar[int]
    SMS_RP_CAUSE_CALL_BARRING: ClassVar[int]
    SMS_RP_CAUSE_CONGESTION: ClassVar[int]
    SMS_RP_CAUSE_DESTINATION_OUT_OF_ORDER: ClassVar[int]
    SMS_RP_CAUSE_FACILITY_NOT_IMPLEMENTED: ClassVar[int]
    SMS_RP_CAUSE_FACILITY_NOT_SUBSCRIBED: ClassVar[int]
    SMS_RP_CAUSE_FACILITY_REJECTED: ClassVar[int]
    SMS_RP_CAUSE_INFORMATION_ELEMENT_NON_EXISTENT: ClassVar[int]
    SMS_RP_CAUSE_INTERWORKING_UNSPECIFIED: ClassVar[int]
    SMS_RP_CAUSE_INVALID_MANDATORY_INFORMATION: ClassVar[int]
    SMS_RP_CAUSE_INVALID_MESSAGE_REFERENCE_VALUE: ClassVar[int]
    SMS_RP_CAUSE_MESSAGE_INCOMPATIBLE_WITH_PROTOCOL_STATE: ClassVar[int]
    SMS_RP_CAUSE_MESSAGE_TYPE_NON_EXISTENT: ClassVar[int]
    SMS_RP_CAUSE_NETWORK_OUT_OF_ORDER: ClassVar[int]
    SMS_RP_CAUSE_OPERATOR_DETERMINED_BARRING: ClassVar[int]
    SMS_RP_CAUSE_PROTOCOL_ERROR: ClassVar[int]
    SMS_RP_CAUSE_RESERVED: ClassVar[int]
    SMS_RP_CAUSE_RESOURCES_UNAVAILABLE: ClassVar[int]
    SMS_RP_CAUSE_SEMANTICALLY_INCORRECT_MESSAGE: ClassVar[int]
    SMS_RP_CAUSE_SHORT_MESSAGE_TRANSFER_REJECTED: ClassVar[int]
    SMS_RP_CAUSE_TEMPORARY_FAILURE: ClassVar[int]
    SMS_RP_CAUSE_UNALLOCATED_NUMBER: ClassVar[int]
    SMS_RP_CAUSE_UNIDENTIFIED_SUBSCRIBER: ClassVar[int]
    SMS_RP_CAUSE_UNKNOWN_SUBSCRIBER: ClassVar[int]
    STATUS_ON_ICC_FREE: ClassVar[int]
    STATUS_ON_ICC_READ: ClassVar[int]
    STATUS_ON_ICC_SENT: ClassVar[int]
    STATUS_ON_ICC_UNREAD: ClassVar[int]
    STATUS_ON_ICC_UNSENT: ClassVar[int]
    def getSubscriptionId(self) -> int: ...
    @staticmethod
    def getDefaultSmsSubscriptionId() -> int: ...
    def createForSubscriptionId(self, p0: int) -> "SmsManager": ...
    def sendDataMessage(self, p0: str, p1: str, p2: int, p3: Any, p4: PendingIntent, p5: PendingIntent) -> None: ...
    @overload
    def sendMultipartTextMessage(self, p0: str, p1: str, p2: list, p3: list, p4: list) -> None: ...
    @overload
    def sendMultipartTextMessage(self, p0: str, p1: str, p2: list, p3: list, p4: list, p5: int) -> None: ...
    @overload
    def sendMultipartTextMessage(self, p0: str, p1: str, p2: list, p3: list, p4: list, p5: str, p6: str) -> None: ...
    def divideMessage(self, p0: str) -> list: ...
    @overload
    def sendTextMessage(self, p0: str, p1: str, p2: str, p3: PendingIntent, p4: PendingIntent, p5: int) -> None: ...
    @overload
    def sendTextMessage(self, p0: str, p1: str, p2: str, p3: PendingIntent, p4: PendingIntent) -> None: ...
    @staticmethod
    def getDefault() -> "SmsManager": ...
    def createAppSpecificSmsToken(self, p0: PendingIntent) -> str: ...
    def createAppSpecificSmsTokenWithPackageInfo(self, p0: str, p1: PendingIntent) -> str: ...
    @overload
    def downloadMultimediaMessage(self, p0: Context, p1: str, p2: Uri, p3: Bundle, p4: PendingIntent) -> None: ...
    @overload
    def downloadMultimediaMessage(self, p0: Context, p1: str, p2: Uri, p3: Bundle, p4: PendingIntent, p5: int) -> None: ...
    def getCarrierConfigValues(self) -> Bundle: ...
    def getSmsCapacityOnIcc(self) -> int: ...
    @staticmethod
    def getSmsManagerForSubscriptionId(p0: int) -> "SmsManager": ...
    def getSmsMessagesForFinancialApp(self, p0: Bundle, p1: Executor, p2: Any) -> None: ...
    def getSmscAddress(self) -> str: ...
    def injectSmsPdu(self, p0: Any, p1: str, p2: PendingIntent) -> None: ...
    @overload
    def sendMultimediaMessage(self, p0: Context, p1: Uri, p2: str, p3: Bundle, p4: PendingIntent, p5: int) -> None: ...
    @overload
    def sendMultimediaMessage(self, p0: Context, p1: Uri, p2: str, p3: Bundle, p4: PendingIntent) -> None: ...
    def sendTextMessageWithoutPersisting(self, p0: str, p1: str, p2: str, p3: PendingIntent, p4: PendingIntent) -> None: ...
    def setSmscAddress(self, p0: str) -> bool: ...

    class FinancialSmsCallback:
        def __init__(self) -> None: ...
        def onFinancialSmsMessages(self, p0: CursorWindow) -> None: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class CellIdentityCdma:
    CREATOR: ClassVar[Any]
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getSystemId(self) -> int: ...
    def getBasestationId(self) -> int: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def getLatitude(self) -> int: ...
    def getLongitude(self) -> int: ...
    def getNetworkId(self) -> int: ...

from typing import Any, ClassVar, overload

class NetworkScan:
    ERROR_INTERRUPTED: ClassVar[int]
    ERROR_INVALID_SCAN: ClassVar[int]
    ERROR_INVALID_SCANID: ClassVar[int]
    ERROR_MODEM_ERROR: ClassVar[int]
    ERROR_MODEM_UNAVAILABLE: ClassVar[int]
    ERROR_RADIO_INTERFACE_ERROR: ClassVar[int]
    ERROR_UNSUPPORTED: ClassVar[int]
    SUCCESS: ClassVar[int]
    def stopScan(self) -> None: ...

from typing import Any, ClassVar, overload

class DataFailCause:
    ACCESS_ATTEMPT_ALREADY_IN_PROGRESS: ClassVar[int]
    ACCESS_BLOCK: ClassVar[int]
    ACCESS_BLOCK_ALL: ClassVar[int]
    ACCESS_CLASS_DSAC_REJECTION: ClassVar[int]
    ACCESS_CONTROL_LIST_CHECK_FAILURE: ClassVar[int]
    ACTIVATION_REJECTED_BCM_VIOLATION: ClassVar[int]
    ACTIVATION_REJECT_GGSN: ClassVar[int]
    ACTIVATION_REJECT_UNSPECIFIED: ClassVar[int]
    ACTIVE_PDP_CONTEXT_MAX_NUMBER_REACHED: ClassVar[int]
    ALL_MATCHING_RULES_FAILED: ClassVar[int]
    APN_DISABLED: ClassVar[int]
    APN_DISALLOWED_ON_ROAMING: ClassVar[int]
    APN_MISMATCH: ClassVar[int]
    APN_PARAMETERS_CHANGED: ClassVar[int]
    APN_PENDING_HANDOVER: ClassVar[int]
    APN_TYPE_CONFLICT: ClassVar[int]
    AUTH_FAILURE_ON_EMERGENCY_CALL: ClassVar[int]
    BEARER_HANDLING_NOT_SUPPORTED: ClassVar[int]
    CALL_DISALLOWED_IN_ROAMING: ClassVar[int]
    CALL_PREEMPT_BY_EMERGENCY_APN: ClassVar[int]
    CANNOT_ENCODE_OTA_MESSAGE: ClassVar[int]
    CDMA_ALERT_STOP: ClassVar[int]
    CDMA_INCOMING_CALL: ClassVar[int]
    CDMA_INTERCEPT: ClassVar[int]
    CDMA_LOCK: ClassVar[int]
    CDMA_RELEASE_DUE_TO_SO_REJECTION: ClassVar[int]
    CDMA_REORDER: ClassVar[int]
    CDMA_RETRY_ORDER: ClassVar[int]
    CHANNEL_ACQUISITION_FAILURE: ClassVar[int]
    CLOSE_IN_PROGRESS: ClassVar[int]
    COLLISION_WITH_NETWORK_INITIATED_REQUEST: ClassVar[int]
    COMPANION_IFACE_IN_USE: ClassVar[int]
    CONCURRENT_SERVICES_INCOMPATIBLE: ClassVar[int]
    CONCURRENT_SERVICES_NOT_ALLOWED: ClassVar[int]
    CONCURRENT_SERVICE_NOT_SUPPORTED_BY_BASE_STATION: ClassVar[int]
    CONDITIONAL_IE_ERROR: ClassVar[int]
    CONGESTION: ClassVar[int]
    CONNECTION_RELEASED: ClassVar[int]
    CS_DOMAIN_NOT_AVAILABLE: ClassVar[int]
    CS_FALLBACK_CALL_ESTABLISHMENT_NOT_ALLOWED: ClassVar[int]
    DATA_PLAN_EXPIRED: ClassVar[int]
    DATA_ROAMING_SETTINGS_DISABLED: ClassVar[int]
    DATA_SETTINGS_DISABLED: ClassVar[int]
    DBM_OR_SMS_IN_PROGRESS: ClassVar[int]
    DDS_SWITCHED: ClassVar[int]
    DDS_SWITCH_IN_PROGRESS: ClassVar[int]
    DRB_RELEASED_BY_RRC: ClassVar[int]
    DS_EXPLICIT_DEACTIVATION: ClassVar[int]
    DUAL_SWITCH: ClassVar[int]
    DUN_CALL_DISALLOWED: ClassVar[int]
    DUPLICATE_BEARER_ID: ClassVar[int]
    EHRPD_TO_HRPD_FALLBACK: ClassVar[int]
    EMBMS_NOT_ENABLED: ClassVar[int]
    EMBMS_REGULAR_DEACTIVATION: ClassVar[int]
    EMERGENCY_IFACE_ONLY: ClassVar[int]
    EMERGENCY_MODE: ClassVar[int]
    EMM_ACCESS_BARRED: ClassVar[int]
    EMM_ACCESS_BARRED_INFINITE_RETRY: ClassVar[int]
    EMM_ATTACH_FAILED: ClassVar[int]
    EMM_ATTACH_STARTED: ClassVar[int]
    EMM_DETACHED: ClassVar[int]
    EMM_T3417_EXPIRED: ClassVar[int]
    EMM_T3417_EXT_EXPIRED: ClassVar[int]
    EPS_SERVICES_AND_NON_EPS_SERVICES_NOT_ALLOWED: ClassVar[int]
    EPS_SERVICES_NOT_ALLOWED_IN_PLMN: ClassVar[int]
    ERROR_UNSPECIFIED: ClassVar[int]
    ESM_BAD_OTA_MESSAGE: ClassVar[int]
    ESM_BEARER_DEACTIVATED_TO_SYNC_WITH_NETWORK: ClassVar[int]
    ESM_COLLISION_SCENARIOS: ClassVar[int]
    ESM_CONTEXT_TRANSFERRED_DUE_TO_IRAT: ClassVar[int]
    ESM_DOWNLOAD_SERVER_REJECTED_THE_CALL: ClassVar[int]
    ESM_FAILURE: ClassVar[int]
    ESM_INFO_NOT_RECEIVED: ClassVar[int]
    ESM_LOCAL_CAUSE_NONE: ClassVar[int]
    ESM_NW_ACTIVATED_DED_BEARER_WITH_ID_OF_DEF_BEARER: ClassVar[int]
    ESM_PROCEDURE_TIME_OUT: ClassVar[int]
    ESM_UNKNOWN_EPS_BEARER_CONTEXT: ClassVar[int]
    EVDO_CONNECTION_DENY_BY_BILLING_OR_AUTHENTICATION_FAILURE: ClassVar[int]
    EVDO_CONNECTION_DENY_BY_GENERAL_OR_NETWORK_BUSY: ClassVar[int]
    EVDO_HDR_CHANGED: ClassVar[int]
    EVDO_HDR_CONNECTION_SETUP_TIMEOUT: ClassVar[int]
    EVDO_HDR_EXITED: ClassVar[int]
    EVDO_HDR_NO_SESSION: ClassVar[int]
    EVDO_USING_GPS_FIX_INSTEAD_OF_HDR_CALL: ClassVar[int]
    FADE: ClassVar[int]
    FAILED_TO_ACQUIRE_COLOCATED_HDR: ClassVar[int]
    FEATURE_NOT_SUPP: ClassVar[int]
    FILTER_SEMANTIC_ERROR: ClassVar[int]
    FILTER_SYTAX_ERROR: ClassVar[int]
    FORBIDDEN_APN_NAME: ClassVar[int]
    GPRS_REGISTRATION_FAIL: ClassVar[int]
    GPRS_SERVICES_AND_NON_GPRS_SERVICES_NOT_ALLOWED: ClassVar[int]
    GPRS_SERVICES_NOT_ALLOWED: ClassVar[int]
    GPRS_SERVICES_NOT_ALLOWED_IN_THIS_PLMN: ClassVar[int]
    HANDOFF_PREFERENCE_CHANGED: ClassVar[int]
    HDR_ACCESS_FAILURE: ClassVar[int]
    HDR_FADE: ClassVar[int]
    HDR_NO_LOCK_GRANTED: ClassVar[int]
    IFACE_AND_POL_FAMILY_MISMATCH: ClassVar[int]
    IFACE_MISMATCH: ClassVar[int]
    ILLEGAL_ME: ClassVar[int]
    ILLEGAL_MS: ClassVar[int]
    IMEI_NOT_ACCEPTED: ClassVar[int]
    IMPLICITLY_DETACHED: ClassVar[int]
    IMSI_UNKNOWN_IN_HOME_SUBSCRIBER_SERVER: ClassVar[int]
    INCOMING_CALL_REJECTED: ClassVar[int]
    INSUFFICIENT_RESOURCES: ClassVar[int]
    INTERFACE_IN_USE: ClassVar[int]
    INTERNAL_CALL_PREEMPT_BY_HIGH_PRIO_APN: ClassVar[int]
    INTERNAL_EPC_NONEPC_TRANSITION: ClassVar[int]
    INVALID_CONNECTION_ID: ClassVar[int]
    INVALID_DNS_ADDR: ClassVar[int]
    INVALID_EMM_STATE: ClassVar[int]
    INVALID_MANDATORY_INFO: ClassVar[int]
    INVALID_MODE: ClassVar[int]
    INVALID_PCSCF_ADDR: ClassVar[int]
    INVALID_PCSCF_OR_DNS_ADDRESS: ClassVar[int]
    INVALID_PRIMARY_NSAPI: ClassVar[int]
    INVALID_SIM_STATE: ClassVar[int]
    INVALID_TRANSACTION_ID: ClassVar[int]
    IPV6_ADDRESS_TRANSFER_FAILED: ClassVar[int]
    IPV6_PREFIX_UNAVAILABLE: ClassVar[int]
    IP_ADDRESS_MISMATCH: ClassVar[int]
    IP_VERSION_MISMATCH: ClassVar[int]
    IRAT_HANDOVER_FAILED: ClassVar[int]
    IS707B_MAX_ACCESS_PROBES: ClassVar[int]
    IWLAN_AUTHORIZATION_REJECTED: ClassVar[int]
    IWLAN_CONGESTION: ClassVar[int]
    IWLAN_DNS_RESOLUTION_NAME_FAILURE: ClassVar[int]
    IWLAN_DNS_RESOLUTION_TIMEOUT: ClassVar[int]
    IWLAN_IKEV2_AUTH_FAILURE: ClassVar[int]
    IWLAN_IKEV2_CERT_INVALID: ClassVar[int]
    IWLAN_IKEV2_CONFIG_FAILURE: ClassVar[int]
    IWLAN_IKEV2_MSG_TIMEOUT: ClassVar[int]
    IWLAN_ILLEGAL_ME: ClassVar[int]
    IWLAN_IMEI_NOT_ACCEPTED: ClassVar[int]
    IWLAN_MAX_CONNECTION_REACHED: ClassVar[int]
    IWLAN_NETWORK_FAILURE: ClassVar[int]
    IWLAN_NON_3GPP_ACCESS_TO_EPC_NOT_ALLOWED: ClassVar[int]
    IWLAN_NO_APN_SUBSCRIPTION: ClassVar[int]
    IWLAN_PDN_CONNECTION_REJECTION: ClassVar[int]
    IWLAN_PLMN_NOT_ALLOWED: ClassVar[int]
    IWLAN_RAT_TYPE_NOT_ALLOWED: ClassVar[int]
    IWLAN_SEMANTIC_ERRORS_IN_PACKET_FILTERS: ClassVar[int]
    IWLAN_SEMANTIC_ERROR_IN_THE_TFT_OPERATION: ClassVar[int]
    IWLAN_SYNTACTICAL_ERRORS_IN_PACKET_FILTERS: ClassVar[int]
    IWLAN_SYNTACTICAL_ERROR_IN_THE_TFT_OPERATION: ClassVar[int]
    IWLAN_TUNNEL_NOT_FOUND: ClassVar[int]
    IWLAN_UNAUTHENTICATED_EMERGENCY_NOT_SUPPORTED: ClassVar[int]
    IWLAN_USER_UNKNOWN: ClassVar[int]
    LIMITED_TO_IPV4: ClassVar[int]
    LIMITED_TO_IPV6: ClassVar[int]
    LLC_SNDCP: ClassVar[int]
    LOCAL_END: ClassVar[int]
    LOCATION_AREA_NOT_ALLOWED: ClassVar[int]
    LOST_CONNECTION: ClassVar[int]
    LOWER_LAYER_REGISTRATION_FAILURE: ClassVar[int]
    LOW_POWER_MODE_OR_POWERING_DOWN: ClassVar[int]
    LTE_NAS_SERVICE_REQUEST_FAILED: ClassVar[int]
    LTE_THROTTLING_NOT_REQUIRED: ClassVar[int]
    MAC_FAILURE: ClassVar[int]
    MATCH_ALL_RULE_NOT_ALLOWED: ClassVar[int]
    MAXIMIUM_NSAPIS_EXCEEDED: ClassVar[int]
    MAXINUM_SIZE_OF_L2_MESSAGE_EXCEEDED: ClassVar[int]
    MAX_ACCESS_PROBE: ClassVar[int]
    MAX_IPV4_CONNECTIONS: ClassVar[int]
    MAX_IPV6_CONNECTIONS: ClassVar[int]
    MAX_PPP_INACTIVITY_TIMER_EXPIRED: ClassVar[int]
    MESSAGE_INCORRECT_SEMANTIC: ClassVar[int]
    MESSAGE_TYPE_UNSUPPORTED: ClassVar[int]
    MIP_CONFIG_FAILURE: ClassVar[int]
    MIP_FA_ADMIN_PROHIBITED: ClassVar[int]
    MIP_FA_DELIVERY_STYLE_NOT_SUPPORTED: ClassVar[int]
    MIP_FA_ENCAPSULATION_UNAVAILABLE: ClassVar[int]
    MIP_FA_HOME_AGENT_AUTHENTICATION_FAILURE: ClassVar[int]
    MIP_FA_INSUFFICIENT_RESOURCES: ClassVar[int]
    MIP_FA_MALFORMED_REPLY: ClassVar[int]
    MIP_FA_MALFORMED_REQUEST: ClassVar[int]
    MIP_FA_MISSING_CHALLENGE: ClassVar[int]
    MIP_FA_MISSING_HOME_ADDRESS: ClassVar[int]
    MIP_FA_MISSING_HOME_AGENT: ClassVar[int]
    MIP_FA_MISSING_NAI: ClassVar[int]
    MIP_FA_MOBILE_NODE_AUTHENTICATION_FAILURE: ClassVar[int]
    MIP_FA_REASON_UNSPECIFIED: ClassVar[int]
    MIP_FA_REQUESTED_LIFETIME_TOO_LONG: ClassVar[int]
    MIP_FA_REVERSE_TUNNEL_IS_MANDATORY: ClassVar[int]
    MIP_FA_REVERSE_TUNNEL_UNAVAILABLE: ClassVar[int]
    MIP_FA_STALE_CHALLENGE: ClassVar[int]
    MIP_FA_UNKNOWN_CHALLENGE: ClassVar[int]
    MIP_FA_VJ_HEADER_COMPRESSION_UNAVAILABLE: ClassVar[int]
    MIP_HA_ADMIN_PROHIBITED: ClassVar[int]
    MIP_HA_ENCAPSULATION_UNAVAILABLE: ClassVar[int]
    MIP_HA_FOREIGN_AGENT_AUTHENTICATION_FAILURE: ClassVar[int]
    MIP_HA_INSUFFICIENT_RESOURCES: ClassVar[int]
    MIP_HA_MALFORMED_REQUEST: ClassVar[int]
    MIP_HA_MOBILE_NODE_AUTHENTICATION_FAILURE: ClassVar[int]
    MIP_HA_REASON_UNSPECIFIED: ClassVar[int]
    MIP_HA_REGISTRATION_ID_MISMATCH: ClassVar[int]
    MIP_HA_REVERSE_TUNNEL_IS_MANDATORY: ClassVar[int]
    MIP_HA_REVERSE_TUNNEL_UNAVAILABLE: ClassVar[int]
    MIP_HA_UNKNOWN_HOME_AGENT_ADDRESS: ClassVar[int]
    MISSING_UNKNOWN_APN: ClassVar[int]
    MODEM_APP_PREEMPTED: ClassVar[int]
    MODEM_RESTART: ClassVar[int]
    MSC_TEMPORARILY_NOT_REACHABLE: ClassVar[int]
    MSG_AND_PROTOCOL_STATE_UNCOMPATIBLE: ClassVar[int]
    MSG_TYPE_NONCOMPATIBLE_STATE: ClassVar[int]
    MS_IDENTITY_CANNOT_BE_DERIVED_BY_THE_NETWORK: ClassVar[int]
    MULTIPLE_PDP_CALL_NOT_ALLOWED: ClassVar[int]
    MULTI_CONN_TO_SAME_PDN_NOT_ALLOWED: ClassVar[int]
    NAS_LAYER_FAILURE: ClassVar[int]
    NAS_REQUEST_REJECTED_BY_NETWORK: ClassVar[int]
    NAS_SIGNALLING: ClassVar[int]
    NETWORK_FAILURE: ClassVar[int]
    NETWORK_INITIATED_DETACH_NO_AUTO_REATTACH: ClassVar[int]
    NETWORK_INITIATED_DETACH_WITH_AUTO_REATTACH: ClassVar[int]
    NETWORK_INITIATED_TERMINATION: ClassVar[int]
    NONE: ClassVar[int]
    NON_IP_NOT_SUPPORTED: ClassVar[int]
    NORMAL_RELEASE: ClassVar[int]
    NO_CDMA_SERVICE: ClassVar[int]
    NO_COLLOCATED_HDR: ClassVar[int]
    NO_EPS_BEARER_CONTEXT_ACTIVATED: ClassVar[int]
    NO_GPRS_CONTEXT: ClassVar[int]
    NO_HYBRID_HDR_SERVICE: ClassVar[int]
    NO_PDP_CONTEXT_ACTIVATED: ClassVar[int]
    NO_RESPONSE_FROM_BASE_STATION: ClassVar[int]
    NO_SERVICE: ClassVar[int]
    NO_SERVICE_ON_GATEWAY: ClassVar[int]
    NSAPI_IN_USE: ClassVar[int]
    NULL_APN_DISALLOWED: ClassVar[int]
    OEM_DCFAILCAUSE_1: ClassVar[int]
    OEM_DCFAILCAUSE_10: ClassVar[int]
    OEM_DCFAILCAUSE_11: ClassVar[int]
    OEM_DCFAILCAUSE_12: ClassVar[int]
    OEM_DCFAILCAUSE_13: ClassVar[int]
    OEM_DCFAILCAUSE_14: ClassVar[int]
    OEM_DCFAILCAUSE_15: ClassVar[int]
    OEM_DCFAILCAUSE_2: ClassVar[int]
    OEM_DCFAILCAUSE_3: ClassVar[int]
    OEM_DCFAILCAUSE_4: ClassVar[int]
    OEM_DCFAILCAUSE_5: ClassVar[int]
    OEM_DCFAILCAUSE_6: ClassVar[int]
    OEM_DCFAILCAUSE_7: ClassVar[int]
    OEM_DCFAILCAUSE_8: ClassVar[int]
    OEM_DCFAILCAUSE_9: ClassVar[int]
    ONLY_IPV4V6_ALLOWED: ClassVar[int]
    ONLY_IPV4_ALLOWED: ClassVar[int]
    ONLY_IPV6_ALLOWED: ClassVar[int]
    ONLY_NON_IP_ALLOWED: ClassVar[int]
    ONLY_SINGLE_BEARER_ALLOWED: ClassVar[int]
    OPERATOR_BARRED: ClassVar[int]
    OTASP_COMMIT_IN_PROGRESS: ClassVar[int]
    PDN_CONN_DOES_NOT_EXIST: ClassVar[int]
    PDN_INACTIVITY_TIMER_EXPIRED: ClassVar[int]
    PDN_IPV4_CALL_DISALLOWED: ClassVar[int]
    PDN_IPV4_CALL_THROTTLED: ClassVar[int]
    PDN_IPV6_CALL_DISALLOWED: ClassVar[int]
    PDN_IPV6_CALL_THROTTLED: ClassVar[int]
    PDN_NON_IP_CALL_DISALLOWED: ClassVar[int]
    PDN_NON_IP_CALL_THROTTLED: ClassVar[int]
    PDP_ACTIVATE_MAX_RETRY_FAILED: ClassVar[int]
    PDP_DUPLICATE: ClassVar[int]
    PDP_ESTABLISH_TIMEOUT_EXPIRED: ClassVar[int]
    PDP_INACTIVE_TIMEOUT_EXPIRED: ClassVar[int]
    PDP_LOWERLAYER_ERROR: ClassVar[int]
    PDP_MODIFY_COLLISION: ClassVar[int]
    PDP_MODIFY_TIMEOUT_EXPIRED: ClassVar[int]
    PDP_PPP_NOT_SUPPORTED: ClassVar[int]
    PDP_WITHOUT_ACTIVE_TFT: ClassVar[int]
    PHONE_IN_USE: ClassVar[int]
    PHYSICAL_LINK_CLOSE_IN_PROGRESS: ClassVar[int]
    PLMN_NOT_ALLOWED: ClassVar[int]
    PPP_AUTH_FAILURE: ClassVar[int]
    PPP_CHAP_FAILURE: ClassVar[int]
    PPP_CLOSE_IN_PROGRESS: ClassVar[int]
    PPP_OPTION_MISMATCH: ClassVar[int]
    PPP_PAP_FAILURE: ClassVar[int]
    PPP_TIMEOUT: ClassVar[int]
    PREF_RADIO_TECH_CHANGED: ClassVar[int]
    PROFILE_BEARER_INCOMPATIBLE: ClassVar[int]
    PROTOCOL_ERRORS: ClassVar[int]
    QOS_NOT_ACCEPTED: ClassVar[int]
    RADIO_ACCESS_BEARER_FAILURE: ClassVar[int]
    RADIO_ACCESS_BEARER_SETUP_FAILURE: ClassVar[int]
    RADIO_NOT_AVAILABLE: ClassVar[int]
    RADIO_POWER_OFF: ClassVar[int]
    REDIRECTION_OR_HANDOFF_IN_PROGRESS: ClassVar[int]
    REGISTRATION_FAIL: ClassVar[int]
    REGULAR_DEACTIVATION: ClassVar[int]
    REJECTED_BY_BASE_STATION: ClassVar[int]
    RRC_CONNECTION_ABORTED_AFTER_HANDOVER: ClassVar[int]
    RRC_CONNECTION_ABORTED_AFTER_IRAT_CELL_CHANGE: ClassVar[int]
    RRC_CONNECTION_ABORTED_DUE_TO_IRAT_CHANGE: ClassVar[int]
    RRC_CONNECTION_ABORTED_DURING_IRAT_CELL_CHANGE: ClassVar[int]
    RRC_CONNECTION_ABORT_REQUEST: ClassVar[int]
    RRC_CONNECTION_ACCESS_BARRED: ClassVar[int]
    RRC_CONNECTION_ACCESS_STRATUM_FAILURE: ClassVar[int]
    RRC_CONNECTION_ANOTHER_PROCEDURE_IN_PROGRESS: ClassVar[int]
    RRC_CONNECTION_CELL_NOT_CAMPED: ClassVar[int]
    RRC_CONNECTION_CELL_RESELECTION: ClassVar[int]
    RRC_CONNECTION_CONFIG_FAILURE: ClassVar[int]
    RRC_CONNECTION_INVALID_REQUEST: ClassVar[int]
    RRC_CONNECTION_LINK_FAILURE: ClassVar[int]
    RRC_CONNECTION_NORMAL_RELEASE: ClassVar[int]
    RRC_CONNECTION_OUT_OF_SERVICE_DURING_CELL_REGISTER: ClassVar[int]
    RRC_CONNECTION_RADIO_LINK_FAILURE: ClassVar[int]
    RRC_CONNECTION_REESTABLISHMENT_FAILURE: ClassVar[int]
    RRC_CONNECTION_REJECT_BY_NETWORK: ClassVar[int]
    RRC_CONNECTION_RELEASED_SECURITY_NOT_ACTIVE: ClassVar[int]
    RRC_CONNECTION_RF_UNAVAILABLE: ClassVar[int]
    RRC_CONNECTION_SYSTEM_INFORMATION_BLOCK_READ_ERROR: ClassVar[int]
    RRC_CONNECTION_SYSTEM_INTERVAL_FAILURE: ClassVar[int]
    RRC_CONNECTION_TIMER_EXPIRED: ClassVar[int]
    RRC_CONNECTION_TRACKING_AREA_ID_CHANGED: ClassVar[int]
    RRC_UPLINK_CONNECTION_RELEASE: ClassVar[int]
    RRC_UPLINK_DATA_TRANSMISSION_FAILURE: ClassVar[int]
    RRC_UPLINK_DELIVERY_FAILED_DUE_TO_HANDOVER: ClassVar[int]
    RRC_UPLINK_ERROR_REQUEST_FROM_NAS: ClassVar[int]
    RRC_UPLINK_RADIO_LINK_FAILURE: ClassVar[int]
    RUIM_NOT_PRESENT: ClassVar[int]
    SECURITY_MODE_REJECTED: ClassVar[int]
    SERVICE_NOT_ALLOWED_ON_PLMN: ClassVar[int]
    SERVICE_OPTION_NOT_SUBSCRIBED: ClassVar[int]
    SERVICE_OPTION_NOT_SUPPORTED: ClassVar[int]
    SERVICE_OPTION_OUT_OF_ORDER: ClassVar[int]
    SIGNAL_LOST: ClassVar[int]
    SIM_CARD_CHANGED: ClassVar[int]
    SLICE_REJECTED: ClassVar[int]
    SYNCHRONIZATION_FAILURE: ClassVar[int]
    TEST_LOOPBACK_REGULAR_DEACTIVATION: ClassVar[int]
    TETHERED_CALL_ACTIVE: ClassVar[int]
    TFT_SEMANTIC_ERROR: ClassVar[int]
    TFT_SYTAX_ERROR: ClassVar[int]
    THERMAL_EMERGENCY: ClassVar[int]
    THERMAL_MITIGATION: ClassVar[int]
    TRAT_SWAP_FAILED: ClassVar[int]
    UE_INITIATED_DETACH_OR_DISCONNECT: ClassVar[int]
    UE_IS_ENTERING_POWERSAVE_MODE: ClassVar[int]
    UE_RAT_CHANGE: ClassVar[int]
    UE_SECURITY_CAPABILITIES_MISMATCH: ClassVar[int]
    UMTS_HANDOVER_TO_IWLAN: ClassVar[int]
    UMTS_REACTIVATION_REQ: ClassVar[int]
    UNACCEPTABLE_NETWORK_PARAMETER: ClassVar[int]
    UNACCEPTABLE_NON_EPS_AUTHENTICATION: ClassVar[int]
    UNKNOWN: ClassVar[int]
    UNKNOWN_INFO_ELEMENT: ClassVar[int]
    UNKNOWN_PDP_ADDRESS_TYPE: ClassVar[int]
    UNKNOWN_PDP_CONTEXT: ClassVar[int]
    UNPREFERRED_RAT: ClassVar[int]
    UNSUPPORTED_1X_PREV: ClassVar[int]
    UNSUPPORTED_APN_IN_CURRENT_PLMN: ClassVar[int]
    UNSUPPORTED_QCI_VALUE: ClassVar[int]
    USER_AUTHENTICATION: ClassVar[int]
    VSNCP_ADMINISTRATIVELY_PROHIBITED: ClassVar[int]
    VSNCP_APN_UNAUTHORIZED: ClassVar[int]
    VSNCP_GEN_ERROR: ClassVar[int]
    VSNCP_INSUFFICIENT_PARAMETERS: ClassVar[int]
    VSNCP_NO_PDN_GATEWAY_ADDRESS: ClassVar[int]
    VSNCP_PDN_EXISTS_FOR_THIS_APN: ClassVar[int]
    VSNCP_PDN_GATEWAY_REJECT: ClassVar[int]
    VSNCP_PDN_GATEWAY_UNREACHABLE: ClassVar[int]
    VSNCP_PDN_ID_IN_USE: ClassVar[int]
    VSNCP_PDN_LIMIT_EXCEEDED: ClassVar[int]
    VSNCP_RECONNECT_NOT_ALLOWED: ClassVar[int]
    VSNCP_RESOURCE_UNAVAILABLE: ClassVar[int]
    VSNCP_SUBSCRIBER_LIMITATION: ClassVar[int]
    VSNCP_TIMEOUT: ClassVar[int]

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class NetworkScanRequest:
    CREATOR: ClassVar[Any]
    SCAN_TYPE_ONE_SHOT: ClassVar[int]
    SCAN_TYPE_PERIODIC: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def __init__(self, p0: int, p1: Any, p2: int, p3: int, p4: bool, p5: int, p6: list) -> None: ...
    def getIncrementalResults(self) -> bool: ...
    def getIncrementalResultsPeriodicity(self) -> int: ...
    def getMaxSearchTime(self) -> int: ...
    def getPlmns(self) -> list: ...
    def getScanType(self) -> int: ...
    def getSearchPeriodicity(self) -> int: ...
    def getSpecifiers(self) -> Any: ...
    def equals(self, p0: Any) -> bool: ...
    def hashCode(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload

class CellLocation:
    def __init__(self) -> None: ...
    @staticmethod
    def getEmpty() -> "CellLocation": ...
    @staticmethod
    def requestLocationUpdate() -> None: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class CellIdentityGsm:
    CREATOR: ClassVar[Any]
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getMcc(self) -> int: ...
    def getMnc(self) -> int: ...
    def getBsic(self) -> int: ...
    def getArfcn(self) -> int: ...
    def getPsc(self) -> int: ...
    def getCid(self) -> int: ...
    def getLac(self) -> int: ...
    def getAdditionalPlmns(self) -> set: ...
    def getMccString(self) -> str: ...
    def getMncString(self) -> str: ...
    def getMobileNetworkOperator(self) -> str: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.os.PersistableBundle import PersistableBundle
from java.util.concurrent.Executor import Executor

class CarrierConfigManager:
    ACTION_CARRIER_CONFIG_CHANGED: ClassVar[str]
    CARRIER_NR_AVAILABILITY_NSA: ClassVar[int]
    CARRIER_NR_AVAILABILITY_SA: ClassVar[int]
    CROSS_SIM_SPN_FORMAT_CARRIER_NAME_ONLY: ClassVar[int]
    CROSS_SIM_SPN_FORMAT_CARRIER_NAME_WITH_BRANDING: ClassVar[int]
    DATA_CYCLE_THRESHOLD_DISABLED: ClassVar[int]
    DATA_CYCLE_USE_PLATFORM_DEFAULT: ClassVar[int]
    ENABLE_EAP_METHOD_PREFIX_BOOL: ClassVar[str]
    EXTRA_REBROADCAST_ON_UNLOCK: ClassVar[str]
    EXTRA_SLOT_INDEX: ClassVar[str]
    EXTRA_SUBSCRIPTION_INDEX: ClassVar[str]
    IMSI_KEY_AVAILABILITY_INT: ClassVar[str]
    KEY_5G_NR_SSRSRP_THRESHOLDS_INT_ARRAY: ClassVar[str]
    KEY_5G_NR_SSRSRQ_THRESHOLDS_INT_ARRAY: ClassVar[str]
    KEY_5G_NR_SSSINR_THRESHOLDS_INT_ARRAY: ClassVar[str]
    KEY_ADDITIONAL_CALL_SETTING_BOOL: ClassVar[str]
    KEY_ADDITIONAL_SETTINGS_CALLER_ID_VISIBILITY_BOOL: ClassVar[str]
    KEY_ADDITIONAL_SETTINGS_CALL_WAITING_VISIBILITY_BOOL: ClassVar[str]
    KEY_ALLOW_ADDING_APNS_BOOL: ClassVar[str]
    KEY_ALLOW_ADD_CALL_DURING_VIDEO_CALL_BOOL: ClassVar[str]
    KEY_ALLOW_EMERGENCY_NUMBERS_IN_CALL_LOG_BOOL: ClassVar[str]
    KEY_ALLOW_EMERGENCY_VIDEO_CALLS_BOOL: ClassVar[str]
    KEY_ALLOW_HOLD_CALL_DURING_EMERGENCY_BOOL: ClassVar[str]
    KEY_ALLOW_HOLD_VIDEO_CALL_BOOL: ClassVar[str]
    KEY_ALLOW_LOCAL_DTMF_TONES_BOOL: ClassVar[str]
    KEY_ALLOW_MERGE_WIFI_CALLS_WHEN_VOWIFI_OFF_BOOL: ClassVar[str]
    KEY_ALLOW_NON_EMERGENCY_CALLS_IN_ECM_BOOL: ClassVar[str]
    KEY_ALLOW_VIDEO_CALLING_FALLBACK_BOOL: ClassVar[str]
    KEY_ALWAYS_SHOW_DATA_RAT_ICON_BOOL: ClassVar[str]
    KEY_ALWAYS_SHOW_EMERGENCY_ALERT_ONOFF_BOOL: ClassVar[str]
    KEY_ALWAYS_SHOW_PRIMARY_SIGNAL_BAR_IN_OPPORTUNISTIC_NETWORK_BOOLEAN: ClassVar[str]
    KEY_APN_EXPAND_BOOL: ClassVar[str]
    KEY_APN_SETTINGS_DEFAULT_APN_TYPES_STRING_ARRAY: ClassVar[str]
    KEY_AUTO_RETRY_ENABLED_BOOL: ClassVar[str]
    KEY_CALL_BARRING_DEFAULT_SERVICE_CLASS_INT: ClassVar[str]
    KEY_CALL_BARRING_SUPPORTS_DEACTIVATE_ALL_BOOL: ClassVar[str]
    KEY_CALL_BARRING_SUPPORTS_PASSWORD_CHANGE_BOOL: ClassVar[str]
    KEY_CALL_BARRING_VISIBILITY_BOOL: ClassVar[str]
    KEY_CALL_COMPOSER_PICTURE_SERVER_URL_STRING: ClassVar[str]
    KEY_CALL_FORWARDING_BLOCKS_WHILE_ROAMING_STRING_ARRAY: ClassVar[str]
    KEY_CALL_REDIRECTION_SERVICE_COMPONENT_NAME_STRING: ClassVar[str]
    KEY_CAPABILITIES_EXEMPT_FROM_SINGLE_DC_CHECK_INT_ARRAY: ClassVar[str]
    KEY_CARRIER_ALLOW_DEFLECT_IMS_CALL_BOOL: ClassVar[str]
    KEY_CARRIER_ALLOW_TURNOFF_IMS_BOOL: ClassVar[str]
    KEY_CARRIER_APP_REQUIRED_DURING_SIM_SETUP_BOOL: ClassVar[str]
    KEY_CARRIER_CALL_SCREENING_APP_STRING: ClassVar[str]
    KEY_CARRIER_CERTIFICATE_STRING_ARRAY: ClassVar[str]
    KEY_CARRIER_CONFIG_APPLIED_BOOL: ClassVar[str]
    KEY_CARRIER_CONFIG_VERSION_STRING: ClassVar[str]
    KEY_CARRIER_CROSS_SIM_IMS_AVAILABLE_BOOL: ClassVar[str]
    KEY_CARRIER_DATA_CALL_PERMANENT_FAILURE_STRINGS: ClassVar[str]
    KEY_CARRIER_DEFAULT_ACTIONS_ON_DCFAILURE_STRING_ARRAY: ClassVar[str]
    KEY_CARRIER_DEFAULT_ACTIONS_ON_DEFAULT_NETWORK_AVAILABLE: ClassVar[str]
    KEY_CARRIER_DEFAULT_ACTIONS_ON_REDIRECTION_STRING_ARRAY: ClassVar[str]
    KEY_CARRIER_DEFAULT_ACTIONS_ON_RESET: ClassVar[str]
    KEY_CARRIER_DEFAULT_REDIRECTION_URL_STRING_ARRAY: ClassVar[str]
    KEY_CARRIER_DEFAULT_WFC_IMS_ENABLED_BOOL: ClassVar[str]
    KEY_CARRIER_DEFAULT_WFC_IMS_MODE_INT: ClassVar[str]
    KEY_CARRIER_DEFAULT_WFC_IMS_ROAMING_MODE_INT: ClassVar[str]
    KEY_CARRIER_FORCE_DISABLE_ETWS_CMAS_TEST_BOOL: ClassVar[str]
    KEY_CARRIER_IMS_GBA_REQUIRED_BOOL: ClassVar[str]
    KEY_CARRIER_INSTANT_LETTERING_AVAILABLE_BOOL: ClassVar[str]
    KEY_CARRIER_INSTANT_LETTERING_ENCODING_STRING: ClassVar[str]
    KEY_CARRIER_INSTANT_LETTERING_ESCAPED_CHARS_STRING: ClassVar[str]
    KEY_CARRIER_INSTANT_LETTERING_INVALID_CHARS_STRING: ClassVar[str]
    KEY_CARRIER_INSTANT_LETTERING_LENGTH_LIMIT_INT: ClassVar[str]
    KEY_CARRIER_METERED_APN_TYPES_STRINGS: ClassVar[str]
    KEY_CARRIER_METERED_ROAMING_APN_TYPES_STRINGS: ClassVar[str]
    KEY_CARRIER_NAME_OVERRIDE_BOOL: ClassVar[str]
    KEY_CARRIER_NAME_STRING: ClassVar[str]
    KEY_CARRIER_NR_AVAILABILITIES_INT_ARRAY: ClassVar[str]
    KEY_CARRIER_PROVISIONS_WIFI_MERGED_NETWORKS_BOOL: ClassVar[str]
    KEY_CARRIER_RCS_PROVISIONING_REQUIRED_BOOL: ClassVar[str]
    KEY_CARRIER_ROAMING_NTN_EMERGENCY_CALL_TO_SATELLITE_HANDOVER_TYPE_INT: ClassVar[str]
    KEY_CARRIER_SERVICE_NAME_STRING_ARRAY: ClassVar[str]
    KEY_CARRIER_SERVICE_NUMBER_STRING_ARRAY: ClassVar[str]
    KEY_CARRIER_SETTINGS_ACTIVITY_COMPONENT_NAME_STRING: ClassVar[str]
    KEY_CARRIER_SETTINGS_ENABLE_BOOL: ClassVar[str]
    KEY_CARRIER_SUPPORTED_SATELLITE_SERVICES_PER_PROVIDER_BUNDLE: ClassVar[str]
    KEY_CARRIER_SUPPORTS_OPP_DATA_AUTO_PROVISIONING_BOOL: ClassVar[str]
    KEY_CARRIER_SUPPORTS_SS_OVER_UT_BOOL: ClassVar[str]
    KEY_CARRIER_SUPPORTS_TETHERING_BOOL: ClassVar[str]
    KEY_CARRIER_USE_IMS_FIRST_FOR_EMERGENCY_BOOL: ClassVar[str]
    KEY_CARRIER_USSD_METHOD_INT: ClassVar[str]
    KEY_CARRIER_UT_PROVISIONING_REQUIRED_BOOL: ClassVar[str]
    KEY_CARRIER_VOLTE_AVAILABLE_BOOL: ClassVar[str]
    KEY_CARRIER_VOLTE_OVERRIDE_WFC_PROVISIONING_BOOL: ClassVar[str]
    KEY_CARRIER_VOLTE_PROVISIONED_BOOL: ClassVar[str]
    KEY_CARRIER_VOLTE_PROVISIONING_REQUIRED_BOOL: ClassVar[str]
    KEY_CARRIER_VOLTE_TTY_SUPPORTED_BOOL: ClassVar[str]
    KEY_CARRIER_VT_AVAILABLE_BOOL: ClassVar[str]
    KEY_CARRIER_VVM_PACKAGE_NAME_STRING: ClassVar[str]
    KEY_CARRIER_VVM_PACKAGE_NAME_STRING_ARRAY: ClassVar[str]
    KEY_CARRIER_WFC_IMS_AVAILABLE_BOOL: ClassVar[str]
    KEY_CARRIER_WFC_SUPPORTS_WIFI_ONLY_BOOL: ClassVar[str]
    KEY_CDMA_3WAYCALL_FLASH_DELAY_INT: ClassVar[str]
    KEY_CDMA_DTMF_TONE_DELAY_INT: ClassVar[str]
    KEY_CDMA_NONROAMING_NETWORKS_STRING_ARRAY: ClassVar[str]
    KEY_CDMA_ROAMING_MODE_INT: ClassVar[str]
    KEY_CDMA_ROAMING_NETWORKS_STRING_ARRAY: ClassVar[str]
    KEY_CELLULAR_SERVICE_CAPABILITIES_INT_ARRAY: ClassVar[str]
    KEY_CELLULAR_USAGE_SETTING_INT: ClassVar[str]
    KEY_CHECK_PRICING_WITH_CARRIER_FOR_DATA_ROAMING_BOOL: ClassVar[str]
    KEY_CI_ACTION_ON_SYS_UPDATE_BOOL: ClassVar[str]
    KEY_CI_ACTION_ON_SYS_UPDATE_EXTRA_STRING: ClassVar[str]
    KEY_CI_ACTION_ON_SYS_UPDATE_EXTRA_VAL_STRING: ClassVar[str]
    KEY_CI_ACTION_ON_SYS_UPDATE_INTENT_STRING: ClassVar[str]
    KEY_CONFIG_IMS_MMTEL_PACKAGE_OVERRIDE_STRING: ClassVar[str]
    KEY_CONFIG_IMS_PACKAGE_OVERRIDE_STRING: ClassVar[str]
    KEY_CONFIG_IMS_RCS_PACKAGE_OVERRIDE_STRING: ClassVar[str]
    KEY_CONFIG_PLANS_PACKAGE_OVERRIDE_STRING: ClassVar[str]
    KEY_CONFIG_TELEPHONY_USE_OWN_NUMBER_FOR_VOICEMAIL_BOOL: ClassVar[str]
    KEY_CONFIG_WIFI_DISABLE_IN_ECBM: ClassVar[str]
    KEY_CROSS_SIM_SPN_FORMAT_INT: ClassVar[str]
    KEY_CSP_ENABLED_BOOL: ClassVar[str]
    KEY_DATA_LIMIT_NOTIFICATION_BOOL: ClassVar[str]
    KEY_DATA_LIMIT_THRESHOLD_BYTES_LONG: ClassVar[str]
    KEY_DATA_RAPID_NOTIFICATION_BOOL: ClassVar[str]
    KEY_DATA_SWITCH_VALIDATION_MIN_INTERVAL_MILLIS_LONG: ClassVar[str]
    KEY_DATA_SWITCH_VALIDATION_TIMEOUT_LONG: ClassVar[str]
    KEY_DATA_WARNING_NOTIFICATION_BOOL: ClassVar[str]
    KEY_DATA_WARNING_THRESHOLD_BYTES_LONG: ClassVar[str]
    KEY_DEFAULT_SIM_CALL_MANAGER_STRING: ClassVar[str]
    KEY_DEFAULT_VM_NUMBER_ROAMING_AND_IMS_UNREGISTERED_STRING: ClassVar[str]
    KEY_DEFAULT_VM_NUMBER_STRING: ClassVar[str]
    KEY_DIAL_STRING_REPLACE_STRING_ARRAY: ClassVar[str]
    KEY_DISABLE_CDMA_ACTIVATION_CODE_BOOL: ClassVar[str]
    KEY_DISABLE_CHARGE_INDICATION_BOOL: ClassVar[str]
    KEY_DISABLE_SUPPLEMENTARY_SERVICES_IN_AIRPLANE_MODE_BOOL: ClassVar[str]
    KEY_DISCONNECT_CAUSE_PLAY_BUSYTONE_INT_ARRAY: ClassVar[str]
    KEY_DISPLAY_CALL_STRENGTH_INDICATOR_BOOL: ClassVar[str]
    KEY_DISPLAY_HD_AUDIO_PROPERTY_BOOL: ClassVar[str]
    KEY_DROP_VIDEO_CALL_WHEN_ANSWERING_AUDIO_CALL_BOOL: ClassVar[str]
    KEY_DTMF_TYPE_ENABLED_BOOL: ClassVar[str]
    KEY_DURATION_BLOCKING_DISABLED_AFTER_EMERGENCY_INT: ClassVar[str]
    KEY_EDITABLE_ENHANCED_4G_LTE_BOOL: ClassVar[str]
    KEY_EDITABLE_VOICEMAIL_NUMBER_BOOL: ClassVar[str]
    KEY_EDITABLE_VOICEMAIL_NUMBER_SETTING_BOOL: ClassVar[str]
    KEY_EDITABLE_WFC_MODE_BOOL: ClassVar[str]
    KEY_EDITABLE_WFC_ROAMING_MODE_BOOL: ClassVar[str]
    KEY_EMERGENCY_NOTIFICATION_DELAY_INT: ClassVar[str]
    KEY_EMERGENCY_NUMBER_PREFIX_STRING_ARRAY: ClassVar[str]
    KEY_ENABLE_CROSS_SIM_CALLING_ON_OPPORTUNISTIC_DATA_BOOL: ClassVar[str]
    KEY_ENABLE_DIALER_KEY_VIBRATION_BOOL: ClassVar[str]
    KEY_ENHANCED_4G_LTE_ON_BY_DEFAULT_BOOL: ClassVar[str]
    KEY_ENHANCED_4G_LTE_TITLE_VARIANT_INT: ClassVar[str]
    KEY_ESIM_DOWNLOAD_RETRY_BACKOFF_TIMER_SEC_INT: ClassVar[str]
    KEY_ESIM_MAX_DOWNLOAD_RETRY_ATTEMPTS_INT: ClassVar[str]
    KEY_FORCE_HOME_NETWORK_BOOL: ClassVar[str]
    KEY_GSM_DTMF_TONE_DELAY_INT: ClassVar[str]
    KEY_GSM_NONROAMING_NETWORKS_STRING_ARRAY: ClassVar[str]
    KEY_GSM_ROAMING_NETWORKS_STRING_ARRAY: ClassVar[str]
    KEY_HAS_IN_CALL_NOISE_SUPPRESSION_BOOL: ClassVar[str]
    KEY_HIDE_CARRIER_NETWORK_SETTINGS_BOOL: ClassVar[str]
    KEY_HIDE_ENHANCED_4G_LTE_BOOL: ClassVar[str]
    KEY_HIDE_IMS_APN_BOOL: ClassVar[str]
    KEY_HIDE_LTE_PLUS_DATA_ICON_BOOL: ClassVar[str]
    KEY_HIDE_PREFERRED_NETWORK_TYPE_BOOL: ClassVar[str]
    KEY_HIDE_PRESET_APN_DETAILS_BOOL: ClassVar[str]
    KEY_HIDE_SIM_LOCK_SETTINGS_BOOL: ClassVar[str]
    KEY_HIDE_TTY_HCO_VCO_WITH_RTT_BOOL: ClassVar[str]
    KEY_IGNORE_DATA_ENABLED_CHANGED_FOR_VIDEO_CALLS: ClassVar[str]
    KEY_IGNORE_RTT_MODE_SETTING_BOOL: ClassVar[str]
    KEY_IGNORE_SIM_NETWORK_LOCKED_EVENTS_BOOL: ClassVar[str]
    KEY_IMS_CONFERENCE_SIZE_LIMIT_INT: ClassVar[str]
    KEY_IMS_DTMF_TONE_DELAY_INT: ClassVar[str]
    KEY_INCLUDE_LTE_FOR_NR_ADVANCED_THRESHOLD_BANDWIDTH_BOOL: ClassVar[str]
    KEY_IS_IMS_CONFERENCE_SIZE_ENFORCED_BOOL: ClassVar[str]
    KEY_IS_OPPORTUNISTIC_SUBSCRIPTION_BOOL: ClassVar[str]
    KEY_LTE_ENABLED_BOOL: ClassVar[str]
    KEY_LTE_RSRQ_THRESHOLDS_INT_ARRAY: ClassVar[str]
    KEY_LTE_RSSNR_THRESHOLDS_INT_ARRAY: ClassVar[str]
    KEY_MDN_IS_ADDITIONAL_VOICEMAIL_NUMBER_BOOL: ClassVar[str]
    KEY_MMS_ALIAS_ENABLED_BOOL: ClassVar[str]
    KEY_MMS_ALIAS_MAX_CHARS_INT: ClassVar[str]
    KEY_MMS_ALIAS_MIN_CHARS_INT: ClassVar[str]
    KEY_MMS_ALLOW_ATTACH_AUDIO_BOOL: ClassVar[str]
    KEY_MMS_APPEND_TRANSACTION_ID_BOOL: ClassVar[str]
    KEY_MMS_CLOSE_CONNECTION_BOOL: ClassVar[str]
    KEY_MMS_EMAIL_GATEWAY_NUMBER_STRING: ClassVar[str]
    KEY_MMS_GROUP_MMS_ENABLED_BOOL: ClassVar[str]
    KEY_MMS_HTTP_PARAMS_STRING: ClassVar[str]
    KEY_MMS_HTTP_SOCKET_TIMEOUT_INT: ClassVar[str]
    KEY_MMS_MAX_IMAGE_HEIGHT_INT: ClassVar[str]
    KEY_MMS_MAX_IMAGE_WIDTH_INT: ClassVar[str]
    KEY_MMS_MAX_MESSAGE_SIZE_INT: ClassVar[str]
    KEY_MMS_MESSAGE_TEXT_MAX_SIZE_INT: ClassVar[str]
    KEY_MMS_MMS_DELIVERY_REPORT_ENABLED_BOOL: ClassVar[str]
    KEY_MMS_MMS_ENABLED_BOOL: ClassVar[str]
    KEY_MMS_MMS_READ_REPORT_ENABLED_BOOL: ClassVar[str]
    KEY_MMS_MULTIPART_SMS_ENABLED_BOOL: ClassVar[str]
    KEY_MMS_NAI_SUFFIX_STRING: ClassVar[str]
    KEY_MMS_NETWORK_RELEASE_TIMEOUT_MILLIS_INT: ClassVar[str]
    KEY_MMS_NOTIFY_WAP_MMSC_ENABLED_BOOL: ClassVar[str]
    KEY_MMS_RECIPIENT_LIMIT_INT: ClassVar[str]
    KEY_MMS_SEND_MULTIPART_SMS_AS_SEPARATE_MESSAGES_BOOL: ClassVar[str]
    KEY_MMS_SHOW_CELL_BROADCAST_APP_LINKS_BOOL: ClassVar[str]
    KEY_MMS_SMS_DELIVERY_REPORT_ENABLED_BOOL: ClassVar[str]
    KEY_MMS_SMS_TO_MMS_TEXT_LENGTH_THRESHOLD_INT: ClassVar[str]
    KEY_MMS_SMS_TO_MMS_TEXT_THRESHOLD_INT: ClassVar[str]
    KEY_MMS_SUBJECT_MAX_LENGTH_INT: ClassVar[str]
    KEY_MMS_SUPPORT_HTTP_CHARSET_HEADER_BOOL: ClassVar[str]
    KEY_MMS_SUPPORT_MMS_CONTENT_DISPOSITION_BOOL: ClassVar[str]
    KEY_MMS_UA_PROF_TAG_NAME_STRING: ClassVar[str]
    KEY_MMS_UA_PROF_URL_STRING: ClassVar[str]
    KEY_MMS_USER_AGENT_STRING: ClassVar[str]
    KEY_MONTHLY_DATA_CYCLE_DAY_INT: ClassVar[str]
    KEY_NTN_LTE_RSRP_THRESHOLDS_INT_ARRAY: ClassVar[str]
    KEY_NTN_LTE_RSRQ_THRESHOLDS_INT_ARRAY: ClassVar[str]
    KEY_NTN_LTE_RSSNR_THRESHOLDS_INT_ARRAY: ClassVar[str]
    KEY_ONLY_AUTO_SELECT_IN_HOME_NETWORK_BOOL: ClassVar[str]
    KEY_ONLY_SINGLE_DC_ALLOWED_INT_ARRAY: ClassVar[str]
    KEY_OPERATOR_SELECTION_EXPAND_BOOL: ClassVar[str]
    KEY_OPPORTUNISTIC_NETWORK_BACKOFF_TIME_LONG: ClassVar[str]
    KEY_OPPORTUNISTIC_NETWORK_DATA_SWITCH_EXIT_HYSTERESIS_TIME_LONG: ClassVar[str]
    KEY_OPPORTUNISTIC_NETWORK_DATA_SWITCH_HYSTERESIS_TIME_LONG: ClassVar[str]
    KEY_OPPORTUNISTIC_NETWORK_ENTRY_OR_EXIT_HYSTERESIS_TIME_LONG: ClassVar[str]
    KEY_OPPORTUNISTIC_NETWORK_ENTRY_THRESHOLD_BANDWIDTH_INT: ClassVar[str]
    KEY_OPPORTUNISTIC_NETWORK_ENTRY_THRESHOLD_RSRP_INT: ClassVar[str]
    KEY_OPPORTUNISTIC_NETWORK_ENTRY_THRESHOLD_RSSNR_INT: ClassVar[str]
    KEY_OPPORTUNISTIC_NETWORK_EXIT_THRESHOLD_RSRP_INT: ClassVar[str]
    KEY_OPPORTUNISTIC_NETWORK_EXIT_THRESHOLD_RSSNR_INT: ClassVar[str]
    KEY_OPPORTUNISTIC_NETWORK_MAX_BACKOFF_TIME_LONG: ClassVar[str]
    KEY_OPPORTUNISTIC_NETWORK_PING_PONG_TIME_LONG: ClassVar[str]
    KEY_PARAMETERS_USED_FOR_NTN_LTE_SIGNAL_BAR_INT: ClassVar[str]
    KEY_PING_TEST_BEFORE_DATA_SWITCH_BOOL: ClassVar[str]
    KEY_PREFER_2G_BOOL: ClassVar[str]
    KEY_PREFER_3G_VISIBILITY_BOOL: ClassVar[str]
    KEY_PREMIUM_CAPABILITY_MAXIMUM_DAILY_NOTIFICATION_COUNT_INT: ClassVar[str]
    KEY_PREMIUM_CAPABILITY_MAXIMUM_MONTHLY_NOTIFICATION_COUNT_INT: ClassVar[str]
    KEY_PREMIUM_CAPABILITY_NETWORK_SETUP_TIME_MILLIS_LONG: ClassVar[str]
    KEY_PREMIUM_CAPABILITY_NOTIFICATION_BACKOFF_HYSTERESIS_TIME_MILLIS_LONG: ClassVar[str]
    KEY_PREMIUM_CAPABILITY_NOTIFICATION_DISPLAY_TIMEOUT_MILLIS_LONG: ClassVar[str]
    KEY_PREMIUM_CAPABILITY_PURCHASE_CONDITION_BACKOFF_HYSTERESIS_TIME_MILLIS_LONG: ClassVar[str]
    KEY_PREMIUM_CAPABILITY_PURCHASE_URL_STRING: ClassVar[str]
    KEY_PREMIUM_CAPABILITY_SUPPORTED_ON_LTE_BOOL: ClassVar[str]
    KEY_PREVENT_CLIR_ACTIVATION_AND_DEACTIVATION_CODE_BOOL: ClassVar[str]
    KEY_RADIO_RESTART_FAILURE_CAUSES_INT_ARRAY: ClassVar[str]
    KEY_RATCHET_NR_ADVANCED_BANDWIDTH_IF_RRC_IDLE_BOOL: ClassVar[str]
    KEY_RCS_CONFIG_SERVER_URL_STRING: ClassVar[str]
    KEY_READ_ONLY_APN_FIELDS_STRING_ARRAY: ClassVar[str]
    KEY_READ_ONLY_APN_TYPES_STRING_ARRAY: ClassVar[str]
    KEY_REQUIRE_ENTITLEMENT_CHECKS_BOOL: ClassVar[str]
    KEY_RESTART_RADIO_ON_PDP_FAIL_REGULAR_DEACTIVATION_BOOL: ClassVar[str]
    KEY_RTT_AUTO_UPGRADE_BOOL: ClassVar[str]
    KEY_RTT_DOWNGRADE_SUPPORTED_BOOL: ClassVar[str]
    KEY_RTT_SUPPORTED_BOOL: ClassVar[str]
    KEY_RTT_SUPPORTED_FOR_VT_BOOL: ClassVar[str]
    KEY_RTT_SUPPORTED_WHILE_ROAMING_BOOL: ClassVar[str]
    KEY_RTT_UPGRADE_SUPPORTED_BOOL: ClassVar[str]
    KEY_RTT_UPGRADE_SUPPORTED_FOR_DOWNGRADED_VT_CALL_BOOL: ClassVar[str]
    KEY_SATELLITE_ATTACH_SUPPORTED_BOOL: ClassVar[str]
    KEY_SATELLITE_CONNECTION_HYSTERESIS_SEC_INT: ClassVar[str]
    KEY_SATELLITE_ENTITLEMENT_STATUS_REFRESH_DAYS_INT: ClassVar[str]
    KEY_SATELLITE_ENTITLEMENT_SUPPORTED_BOOL: ClassVar[str]
    KEY_SATELLITE_ESOS_SUPPORTED_BOOL: ClassVar[str]
    KEY_SATELLITE_ROAMING_ESOS_INACTIVITY_TIMEOUT_SEC_INT: ClassVar[str]
    KEY_SATELLITE_ROAMING_P2P_SMS_INACTIVITY_TIMEOUT_SEC_INT: ClassVar[str]
    KEY_SATELLITE_ROAMING_P2P_SMS_SUPPORTED_BOOL: ClassVar[str]
    KEY_SATELLITE_ROAMING_SCREEN_OFF_INACTIVITY_TIMEOUT_SEC_INT: ClassVar[str]
    KEY_SHOW_4G_FOR_3G_DATA_ICON_BOOL: ClassVar[str]
    KEY_SHOW_4G_FOR_LTE_DATA_ICON_BOOL: ClassVar[str]
    KEY_SHOW_APN_SETTING_CDMA_BOOL: ClassVar[str]
    KEY_SHOW_BLOCKING_PAY_PHONE_OPTION_BOOL: ClassVar[str]
    KEY_SHOW_CALL_BLOCKING_DISABLED_NOTIFICATION_ALWAYS_BOOL: ClassVar[str]
    KEY_SHOW_CDMA_CHOICES_BOOL: ClassVar[str]
    KEY_SHOW_FORWARDED_NUMBER_BOOL: ClassVar[str]
    KEY_SHOW_ICCID_IN_SIM_STATUS_BOOL: ClassVar[str]
    KEY_SHOW_IMS_REGISTRATION_STATUS_BOOL: ClassVar[str]
    KEY_SHOW_ONSCREEN_DIAL_BUTTON_BOOL: ClassVar[str]
    KEY_SHOW_ROAMING_INDICATOR_BOOL: ClassVar[str]
    KEY_SHOW_SIGNAL_STRENGTH_IN_SIM_STATUS_BOOL: ClassVar[str]
    KEY_SHOW_VIDEO_CALL_CHARGES_ALERT_DIALOG_BOOL: ClassVar[str]
    KEY_SHOW_WFC_LOCATION_PRIVACY_POLICY_BOOL: ClassVar[str]
    KEY_SIMPLIFIED_NETWORK_SETTINGS_BOOL: ClassVar[str]
    KEY_SIM_COUNTRY_ISO_OVERRIDE_STRING: ClassVar[str]
    KEY_SIM_NETWORK_UNLOCK_ALLOW_DISMISS_BOOL: ClassVar[str]
    KEY_SMDP_SERVER_ADDRESS_STRING: ClassVar[str]
    KEY_SMS_REQUIRES_DESTINATION_NUMBER_CONVERSION_BOOL: ClassVar[str]
    KEY_SUBSCRIPTION_GROUP_UUID_STRING: ClassVar[str]
    KEY_SUPPORTED_PREMIUM_CAPABILITIES_INT_ARRAY: ClassVar[str]
    KEY_SUPPORTS_BUSINESS_CALL_COMPOSER_BOOL: ClassVar[str]
    KEY_SUPPORTS_CALL_COMPOSER_BOOL: ClassVar[str]
    KEY_SUPPORTS_DEVICE_TO_DEVICE_COMMUNICATION_USING_DTMF_BOOL: ClassVar[str]
    KEY_SUPPORTS_DEVICE_TO_DEVICE_COMMUNICATION_USING_RTP_BOOL: ClassVar[str]
    KEY_SUPPORTS_SDP_NEGOTIATION_OF_D2D_RTP_HEADER_EXTENSIONS_BOOL: ClassVar[str]
    KEY_SUPPORT_3GPP_CALL_FORWARDING_WHILE_ROAMING_BOOL: ClassVar[str]
    KEY_SUPPORT_ADD_CONFERENCE_PARTICIPANTS_BOOL: ClassVar[str]
    KEY_SUPPORT_ADHOC_CONFERENCE_CALLS_BOOL: ClassVar[str]
    KEY_SUPPORT_CLIR_NETWORK_DEFAULT_BOOL: ClassVar[str]
    KEY_SUPPORT_CONFERENCE_CALL_BOOL: ClassVar[str]
    KEY_SUPPORT_EMERGENCY_SMS_OVER_IMS_BOOL: ClassVar[str]
    KEY_SUPPORT_ENHANCED_CALL_BLOCKING_BOOL: ClassVar[str]
    KEY_SUPPORT_IMS_CONFERENCE_EVENT_PACKAGE_BOOL: ClassVar[str]
    KEY_SUPPORT_PAUSE_IMS_VIDEO_CALLS_BOOL: ClassVar[str]
    KEY_SUPPORT_SWAP_AFTER_MERGE_BOOL: ClassVar[str]
    KEY_SUPPORT_TDSCDMA_BOOL: ClassVar[str]
    KEY_SUPPORT_TDSCDMA_ROAMING_NETWORKS_STRING_ARRAY: ClassVar[str]
    KEY_SWITCH_DATA_TO_PRIMARY_IF_PRIMARY_IS_OOS_BOOL: ClassVar[str]
    KEY_TREAT_DOWNGRADED_VIDEO_CALLS_AS_VIDEO_CALLS_BOOL: ClassVar[str]
    KEY_TTY_SUPPORTED_BOOL: ClassVar[str]
    KEY_UNLOGGABLE_NUMBERS_STRING_ARRAY: ClassVar[str]
    KEY_USE_ACS_FOR_RCS_BOOL: ClassVar[str]
    KEY_USE_HFA_FOR_PROVISIONING_BOOL: ClassVar[str]
    KEY_USE_IP_FOR_CALLING_INDICATOR_BOOL: ClassVar[str]
    KEY_USE_OTASP_FOR_PROVISIONING_BOOL: ClassVar[str]
    KEY_USE_RCS_PRESENCE_BOOL: ClassVar[str]
    KEY_USE_RCS_SIP_OPTIONS_BOOL: ClassVar[str]
    KEY_USE_WFC_HOME_NETWORK_MODE_IN_ROAMING_NETWORK_BOOL: ClassVar[str]
    KEY_VOICEMAIL_NOTIFICATION_PERSISTENT_BOOL: ClassVar[str]
    KEY_VOICE_PRIVACY_DISABLE_UI_BOOL: ClassVar[str]
    KEY_VOLTE_REPLACEMENT_RAT_INT: ClassVar[str]
    KEY_VONR_ENABLED_BOOL: ClassVar[str]
    KEY_VONR_ON_BY_DEFAULT_BOOL: ClassVar[str]
    KEY_VONR_SETTING_VISIBILITY_BOOL: ClassVar[str]
    KEY_VT_UPGRADE_SUPPORTED_FOR_DOWNGRADED_RTT_CALL_BOOL: ClassVar[str]
    KEY_VVM_CELLULAR_DATA_REQUIRED_BOOL: ClassVar[str]
    KEY_VVM_CLIENT_PREFIX_STRING: ClassVar[str]
    KEY_VVM_DESTINATION_NUMBER_STRING: ClassVar[str]
    KEY_VVM_DISABLED_CAPABILITIES_STRING_ARRAY: ClassVar[str]
    KEY_VVM_LEGACY_MODE_ENABLED_BOOL: ClassVar[str]
    KEY_VVM_PORT_NUMBER_INT: ClassVar[str]
    KEY_VVM_PREFETCH_BOOL: ClassVar[str]
    KEY_VVM_SSL_ENABLED_BOOL: ClassVar[str]
    KEY_VVM_TYPE_STRING: ClassVar[str]
    KEY_WFC_EMERGENCY_ADDRESS_CARRIER_APP_STRING: ClassVar[str]
    KEY_WORLD_MODE_ENABLED_BOOL: ClassVar[str]
    KEY_WORLD_PHONE_BOOL: ClassVar[str]
    REMOVE_GROUP_UUID_STRING: ClassVar[str]
    SERVICE_CLASS_NONE: ClassVar[int]
    SERVICE_CLASS_VOICE: ClassVar[int]
    USSD_OVER_CS_ONLY: ClassVar[int]
    USSD_OVER_CS_PREFERRED: ClassVar[int]
    USSD_OVER_IMS_ONLY: ClassVar[int]
    USSD_OVER_IMS_PREFERRED: ClassVar[int]
    def getConfigByComponentForSubId(self, p0: str, p1: int) -> PersistableBundle: ...
    @overload
    def getConfigForSubId(self, p0: int) -> PersistableBundle: ...
    @overload
    def getConfigForSubId(self, p0: int, p1: Any) -> PersistableBundle: ...
    @staticmethod
    def isConfigForIdentifiedCarrier(p0: PersistableBundle) -> bool: ...
    def notifyConfigChangedForSubId(self, p0: int) -> None: ...
    def registerCarrierConfigChangeListener(self, p0: Executor, p1: Any) -> None: ...
    def unregisterCarrierConfigChangeListener(self, p0: Any) -> None: ...
    @overload
    def getConfig(self, p0: Any) -> PersistableBundle: ...
    @overload
    def getConfig(self) -> PersistableBundle: ...

    class Iwlan:
        AUTHENTICATION_METHOD_CERT: ClassVar[int]
        AUTHENTICATION_METHOD_EAP_ONLY: ClassVar[int]
        EPDG_ADDRESS_CELLULAR_LOC: ClassVar[int]
        EPDG_ADDRESS_IPV4_ONLY: ClassVar[int]
        EPDG_ADDRESS_IPV4_PREFERRED: ClassVar[int]
        EPDG_ADDRESS_IPV6_PREFERRED: ClassVar[int]
        EPDG_ADDRESS_PCO: ClassVar[int]
        EPDG_ADDRESS_PLMN: ClassVar[int]
        EPDG_ADDRESS_STATIC: ClassVar[int]
        EPDG_ADDRESS_VISITED_COUNTRY: ClassVar[int]
        ID_TYPE_FQDN: ClassVar[int]
        ID_TYPE_KEY_ID: ClassVar[int]
        ID_TYPE_RFC822_ADDR: ClassVar[int]
        KEY_ADD_KE_TO_CHILD_SESSION_REKEY_BOOL: ClassVar[str]
        KEY_CHILD_SA_REKEY_HARD_TIMER_SEC_INT: ClassVar[str]
        KEY_CHILD_SA_REKEY_SOFT_TIMER_SEC_INT: ClassVar[str]
        KEY_CHILD_SESSION_AES_CBC_KEY_SIZE_INT_ARRAY: ClassVar[str]
        KEY_CHILD_SESSION_AES_CTR_KEY_SIZE_INT_ARRAY: ClassVar[str]
        KEY_CHILD_SESSION_AES_GCM_KEY_SIZE_INT_ARRAY: ClassVar[str]
        KEY_DIFFIE_HELLMAN_GROUPS_INT_ARRAY: ClassVar[str]
        KEY_DPD_TIMER_SEC_INT: ClassVar[str]
        KEY_EPDG_ADDRESS_IP_TYPE_PREFERENCE_INT: ClassVar[str]
        KEY_EPDG_ADDRESS_PRIORITY_INT_ARRAY: ClassVar[str]
        KEY_EPDG_AUTHENTICATION_METHOD_INT: ClassVar[str]
        KEY_EPDG_PCO_ID_IPV4_INT: ClassVar[str]
        KEY_EPDG_PCO_ID_IPV6_INT: ClassVar[str]
        KEY_EPDG_STATIC_ADDRESS_ROAMING_STRING: ClassVar[str]
        KEY_EPDG_STATIC_ADDRESS_STRING: ClassVar[str]
        KEY_IKE_LOCAL_ID_TYPE_INT: ClassVar[str]
        KEY_IKE_REKEY_HARD_TIMER_SEC_INT: ClassVar[str]
        KEY_IKE_REKEY_SOFT_TIMER_SEC_INT: ClassVar[str]
        KEY_IKE_REMOTE_ID_TYPE_INT: ClassVar[str]
        KEY_IKE_SESSION_AES_CBC_KEY_SIZE_INT_ARRAY: ClassVar[str]
        KEY_IKE_SESSION_AES_CTR_KEY_SIZE_INT_ARRAY: ClassVar[str]
        KEY_IKE_SESSION_AES_GCM_KEY_SIZE_INT_ARRAY: ClassVar[str]
        KEY_MAX_RETRIES_INT: ClassVar[str]
        KEY_MCC_MNCS_STRING_ARRAY: ClassVar[str]
        KEY_NATT_KEEP_ALIVE_TIMER_SEC_INT: ClassVar[str]
        KEY_PREFIX: ClassVar[str]
        KEY_RETRANSMIT_TIMER_MSEC_INT_ARRAY: ClassVar[str]
        KEY_SUPPORTED_CHILD_SESSION_AEAD_ALGORITHMS_INT_ARRAY: ClassVar[str]
        KEY_SUPPORTED_CHILD_SESSION_ENCRYPTION_ALGORITHMS_INT_ARRAY: ClassVar[str]
        KEY_SUPPORTED_IKE_SESSION_AEAD_ALGORITHMS_INT_ARRAY: ClassVar[str]
        KEY_SUPPORTED_IKE_SESSION_ENCRYPTION_ALGORITHMS_INT_ARRAY: ClassVar[str]
        KEY_SUPPORTED_INTEGRITY_ALGORITHMS_INT_ARRAY: ClassVar[str]
        KEY_SUPPORTED_PRF_ALGORITHMS_INT_ARRAY: ClassVar[str]
        KEY_SUPPORTS_CHILD_SESSION_MULTIPLE_SA_PROPOSALS_BOOL: ClassVar[str]
        KEY_SUPPORTS_EAP_AKA_FAST_REAUTH_BOOL: ClassVar[str]
        KEY_SUPPORTS_IKE_SESSION_MULTIPLE_SA_PROPOSALS_BOOL: ClassVar[str]

    class ImsWfc:
        KEY_EMERGENCY_CALL_OVER_EMERGENCY_PDN_BOOL: ClassVar[str]
        KEY_PIDF_SHORT_CODE_STRING_ARRAY: ClassVar[str]
        KEY_PREFIX: ClassVar[str]

    class ImsVt:
        KEY_H264_PAYLOAD_DESCRIPTION_BUNDLE: ClassVar[str]
        KEY_H264_PAYLOAD_TYPE_INT_ARRAY: ClassVar[str]
        KEY_H264_VIDEO_CODEC_ATTRIBUTE_PROFILE_LEVEL_ID_STRING: ClassVar[str]
        KEY_PREFIX: ClassVar[str]
        KEY_VIDEO_AS_BANDWIDTH_KBPS_INT: ClassVar[str]
        KEY_VIDEO_CODEC_ATTRIBUTE_FRAME_RATE_INT: ClassVar[str]
        KEY_VIDEO_CODEC_ATTRIBUTE_PACKETIZATION_MODE_INT: ClassVar[str]
        KEY_VIDEO_CODEC_ATTRIBUTE_RESOLUTION_INT_ARRAY: ClassVar[str]
        KEY_VIDEO_CODEC_CAPABILITY_PAYLOAD_TYPES_BUNDLE: ClassVar[str]
        KEY_VIDEO_ON_DEFAULT_BEARER_SUPPORTED_BOOL: ClassVar[str]
        KEY_VIDEO_QOS_PRECONDITION_SUPPORTED_BOOL: ClassVar[str]
        KEY_VIDEO_RR_BANDWIDTH_BPS_INT: ClassVar[str]
        KEY_VIDEO_RS_BANDWIDTH_BPS_INT: ClassVar[str]
        KEY_VIDEO_RTCP_INACTIVITY_TIMER_MILLIS_INT: ClassVar[str]
        KEY_VIDEO_RTP_DSCP_INT: ClassVar[str]
        KEY_VIDEO_RTP_INACTIVITY_TIMER_MILLIS_INT: ClassVar[str]

    class ImsVoice:
        ALERTING_SRVCC_SUPPORT: ClassVar[int]
        BANDWIDTH_EFFICIENT: ClassVar[int]
        BASIC_SRVCC_SUPPORT: ClassVar[int]
        CONFERENCE_SUBSCRIBE_TYPE_IN_DIALOG: ClassVar[int]
        CONFERENCE_SUBSCRIBE_TYPE_OUT_OF_DIALOG: ClassVar[int]
        EVS_ENCODED_BW_TYPE_FB: ClassVar[int]
        EVS_ENCODED_BW_TYPE_NB: ClassVar[int]
        EVS_ENCODED_BW_TYPE_NB_WB: ClassVar[int]
        EVS_ENCODED_BW_TYPE_NB_WB_SWB: ClassVar[int]
        EVS_ENCODED_BW_TYPE_NB_WB_SWB_FB: ClassVar[int]
        EVS_ENCODED_BW_TYPE_SWB: ClassVar[int]
        EVS_ENCODED_BW_TYPE_WB: ClassVar[int]
        EVS_ENCODED_BW_TYPE_WB_SWB: ClassVar[int]
        EVS_ENCODED_BW_TYPE_WB_SWB_FB: ClassVar[int]
        EVS_OPERATIONAL_MODE_AMRWB_IO: ClassVar[int]
        EVS_OPERATIONAL_MODE_PRIMARY: ClassVar[int]
        EVS_PRIMARY_MODE_BITRATE_128_0_KBPS: ClassVar[int]
        EVS_PRIMARY_MODE_BITRATE_13_2_KBPS: ClassVar[int]
        EVS_PRIMARY_MODE_BITRATE_16_4_KBPS: ClassVar[int]
        EVS_PRIMARY_MODE_BITRATE_24_4_KBPS: ClassVar[int]
        EVS_PRIMARY_MODE_BITRATE_32_0_KBPS: ClassVar[int]
        EVS_PRIMARY_MODE_BITRATE_48_0_KBPS: ClassVar[int]
        EVS_PRIMARY_MODE_BITRATE_5_9_KBPS: ClassVar[int]
        EVS_PRIMARY_MODE_BITRATE_64_0_KBPS: ClassVar[int]
        EVS_PRIMARY_MODE_BITRATE_7_2_KBPS: ClassVar[int]
        EVS_PRIMARY_MODE_BITRATE_8_0_KBPS: ClassVar[int]
        EVS_PRIMARY_MODE_BITRATE_96_0_KBPS: ClassVar[int]
        EVS_PRIMARY_MODE_BITRATE_9_6_KBPS: ClassVar[int]
        KEY_AMRNB_PAYLOAD_DESCRIPTION_BUNDLE: ClassVar[str]
        KEY_AMRNB_PAYLOAD_TYPE_INT_ARRAY: ClassVar[str]
        KEY_AMRWB_PAYLOAD_DESCRIPTION_BUNDLE: ClassVar[str]
        KEY_AMRWB_PAYLOAD_TYPE_INT_ARRAY: ClassVar[str]
        KEY_AMR_CODEC_ATTRIBUTE_MODESET_INT_ARRAY: ClassVar[str]
        KEY_AMR_CODEC_ATTRIBUTE_PAYLOAD_FORMAT_INT: ClassVar[str]
        KEY_AUDIO_AS_BANDWIDTH_KBPS_INT: ClassVar[str]
        KEY_AUDIO_CODEC_CAPABILITY_PAYLOAD_TYPES_BUNDLE: ClassVar[str]
        KEY_AUDIO_INACTIVITY_CALL_END_REASONS_INT_ARRAY: ClassVar[str]
        KEY_AUDIO_RR_BANDWIDTH_BPS_INT: ClassVar[str]
        KEY_AUDIO_RS_BANDWIDTH_BPS_INT: ClassVar[str]
        KEY_AUDIO_RTCP_INACTIVITY_TIMER_MILLIS_INT: ClassVar[str]
        KEY_AUDIO_RTP_INACTIVITY_TIMER_MILLIS_INT: ClassVar[str]
        KEY_CARRIER_VOLTE_ROAMING_AVAILABLE_BOOL: ClassVar[str]
        KEY_CODEC_ATTRIBUTE_MODE_CHANGE_CAPABILITY_INT: ClassVar[str]
        KEY_CODEC_ATTRIBUTE_MODE_CHANGE_NEIGHBOR_INT: ClassVar[str]
        KEY_CODEC_ATTRIBUTE_MODE_CHANGE_PERIOD_INT: ClassVar[str]
        KEY_CONFERENCE_FACTORY_URI_STRING: ClassVar[str]
        KEY_CONFERENCE_SUBSCRIBE_TYPE_INT: ClassVar[str]
        KEY_DEDICATED_BEARER_WAIT_TIMER_MILLIS_INT: ClassVar[str]
        KEY_DTMFNB_PAYLOAD_TYPE_INT_ARRAY: ClassVar[str]
        KEY_DTMFWB_PAYLOAD_TYPE_INT_ARRAY: ClassVar[str]
        KEY_EVS_CODEC_ATTRIBUTE_BANDWIDTH_INT: ClassVar[str]
        KEY_EVS_CODEC_ATTRIBUTE_BITRATE_INT_ARRAY: ClassVar[str]
        KEY_EVS_CODEC_ATTRIBUTE_CHANNELS_INT: ClassVar[str]
        KEY_EVS_CODEC_ATTRIBUTE_CH_AW_RECV_INT: ClassVar[str]
        KEY_EVS_CODEC_ATTRIBUTE_CMR_INT: ClassVar[str]
        KEY_EVS_CODEC_ATTRIBUTE_DTX_BOOL: ClassVar[str]
        KEY_EVS_CODEC_ATTRIBUTE_DTX_RECV_BOOL: ClassVar[str]
        KEY_EVS_CODEC_ATTRIBUTE_HF_ONLY_INT: ClassVar[str]
        KEY_EVS_CODEC_ATTRIBUTE_MODE_SWITCH_INT: ClassVar[str]
        KEY_EVS_PAYLOAD_DESCRIPTION_BUNDLE: ClassVar[str]
        KEY_EVS_PAYLOAD_TYPE_INT_ARRAY: ClassVar[str]
        KEY_INCLUDE_CALLER_ID_SERVICE_CODES_IN_SIP_INVITE_BOOL: ClassVar[str]
        KEY_MINIMUM_SESSION_EXPIRES_TIMER_SEC_INT: ClassVar[str]
        KEY_MO_CALL_REQUEST_TIMEOUT_MILLIS_INT: ClassVar[str]
        KEY_MULTIENDPOINT_SUPPORTED_BOOL: ClassVar[str]
        KEY_OIP_SOURCE_FROM_HEADER_BOOL: ClassVar[str]
        KEY_PRACK_SUPPORTED_FOR_18X_BOOL: ClassVar[str]
        KEY_PREFIX: ClassVar[str]
        KEY_RINGBACK_TIMER_MILLIS_INT: ClassVar[str]
        KEY_RINGING_TIMER_MILLIS_INT: ClassVar[str]
        KEY_SESSION_EXPIRES_TIMER_SEC_INT: ClassVar[str]
        KEY_SESSION_PRIVACY_TYPE_INT: ClassVar[str]
        KEY_SESSION_REFRESHER_TYPE_INT: ClassVar[str]
        KEY_SESSION_REFRESH_METHOD_INT: ClassVar[str]
        KEY_SESSION_TIMER_SUPPORTED_BOOL: ClassVar[str]
        KEY_SRVCC_TYPE_INT_ARRAY: ClassVar[str]
        KEY_VOICE_ON_DEFAULT_BEARER_SUPPORTED_BOOL: ClassVar[str]
        KEY_VOICE_QOS_PRECONDITION_SUPPORTED_BOOL: ClassVar[str]
        MIDCALL_SRVCC_SUPPORT: ClassVar[int]
        OCTET_ALIGNED: ClassVar[int]
        PREALERTING_SRVCC_SUPPORT: ClassVar[int]
        SESSION_PRIVACY_TYPE_HEADER: ClassVar[int]
        SESSION_PRIVACY_TYPE_ID: ClassVar[int]
        SESSION_PRIVACY_TYPE_NONE: ClassVar[int]
        SESSION_REFRESHER_TYPE_UAC: ClassVar[int]
        SESSION_REFRESHER_TYPE_UAS: ClassVar[int]
        SESSION_REFRESHER_TYPE_UNKNOWN: ClassVar[int]
        SESSION_REFRESH_METHOD_INVITE: ClassVar[int]
        SESSION_REFRESH_METHOD_UPDATE_PREFERRED: ClassVar[int]

    class ImsSs:
        CALL_WAITING_SYNC_FIRST_CHANGE: ClassVar[int]
        CALL_WAITING_SYNC_FIRST_POWER_UP: ClassVar[int]
        CALL_WAITING_SYNC_IMS_ONLY: ClassVar[int]
        CALL_WAITING_SYNC_NONE: ClassVar[int]
        CALL_WAITING_SYNC_USER_CHANGE: ClassVar[int]
        KEY_NETWORK_INITIATED_USSD_OVER_IMS_SUPPORTED_BOOL: ClassVar[str]
        KEY_PREFIX: ClassVar[str]
        KEY_TERMINAL_BASED_CALL_WAITING_DEFAULT_ENABLED_BOOL: ClassVar[str]
        KEY_TERMINAL_BASED_CALL_WAITING_SYNC_TYPE_INT: ClassVar[str]
        KEY_USE_CSFB_ON_XCAP_OVER_UT_FAILURE_BOOL: ClassVar[str]
        KEY_UT_AS_SERVER_FQDN_STRING: ClassVar[str]
        KEY_UT_AS_SERVER_PORT_INT: ClassVar[str]
        KEY_UT_IPTYPE_HOME_INT: ClassVar[str]
        KEY_UT_IPTYPE_ROAMING_INT: ClassVar[str]
        KEY_UT_REQUIRES_IMS_REGISTRATION_BOOL: ClassVar[str]
        KEY_UT_SERVER_BASED_SERVICES_INT_ARRAY: ClassVar[str]
        KEY_UT_SUPPORTED_WHEN_PS_DATA_OFF_BOOL: ClassVar[str]
        KEY_UT_SUPPORTED_WHEN_ROAMING_BOOL: ClassVar[str]
        KEY_UT_TERMINAL_BASED_SERVICES_INT_ARRAY: ClassVar[str]
        KEY_UT_TRANSPORT_TYPE_INT: ClassVar[str]
        KEY_XCAP_OVER_UT_SUPPORTED_RATS_INT_ARRAY: ClassVar[str]
        SUPPLEMENTARY_SERVICE_CB_ACR: ClassVar[int]
        SUPPLEMENTARY_SERVICE_CB_ALL: ClassVar[int]
        SUPPLEMENTARY_SERVICE_CB_BAIC: ClassVar[int]
        SUPPLEMENTARY_SERVICE_CB_BAOC: ClassVar[int]
        SUPPLEMENTARY_SERVICE_CB_BIC_ROAM: ClassVar[int]
        SUPPLEMENTARY_SERVICE_CB_BIL: ClassVar[int]
        SUPPLEMENTARY_SERVICE_CB_BOIC: ClassVar[int]
        SUPPLEMENTARY_SERVICE_CB_BOIC_EXHC: ClassVar[int]
        SUPPLEMENTARY_SERVICE_CB_IBS: ClassVar[int]
        SUPPLEMENTARY_SERVICE_CB_OBS: ClassVar[int]
        SUPPLEMENTARY_SERVICE_CF_ALL: ClassVar[int]
        SUPPLEMENTARY_SERVICE_CF_ALL_CONDITONAL_FORWARDING: ClassVar[int]
        SUPPLEMENTARY_SERVICE_CF_CFB: ClassVar[int]
        SUPPLEMENTARY_SERVICE_CF_CFNL: ClassVar[int]
        SUPPLEMENTARY_SERVICE_CF_CFNRC: ClassVar[int]
        SUPPLEMENTARY_SERVICE_CF_CFNRY: ClassVar[int]
        SUPPLEMENTARY_SERVICE_CF_CFU: ClassVar[int]
        SUPPLEMENTARY_SERVICE_CW: ClassVar[int]
        SUPPLEMENTARY_SERVICE_IDENTIFICATION_OIP: ClassVar[int]
        SUPPLEMENTARY_SERVICE_IDENTIFICATION_OIR: ClassVar[int]
        SUPPLEMENTARY_SERVICE_IDENTIFICATION_TIP: ClassVar[int]
        SUPPLEMENTARY_SERVICE_IDENTIFICATION_TIR: ClassVar[int]

    class ImsSms:
        KEY_PREFIX: ClassVar[str]
        KEY_SMS_CSFB_RETRY_ON_FAILURE_BOOL: ClassVar[str]
        KEY_SMS_MAX_RETRY_COUNT_INT: ClassVar[str]
        KEY_SMS_MAX_RETRY_OVER_IMS_COUNT_INT: ClassVar[str]
        KEY_SMS_OVER_IMS_FORMAT_INT: ClassVar[str]
        KEY_SMS_OVER_IMS_SEND_RETRY_DELAY_MILLIS_INT: ClassVar[str]
        KEY_SMS_OVER_IMS_SUPPORTED_BOOL: ClassVar[str]
        KEY_SMS_OVER_IMS_SUPPORTED_RATS_INT_ARRAY: ClassVar[str]
        KEY_SMS_RP_CAUSE_VALUES_TO_FALLBACK_INT_ARRAY: ClassVar[str]
        KEY_SMS_RP_CAUSE_VALUES_TO_RETRY_OVER_IMS_INT_ARRAY: ClassVar[str]
        KEY_SMS_TR1_TIMER_MILLIS_INT: ClassVar[str]
        KEY_SMS_TR2_TIMER_MILLIS_INT: ClassVar[str]
        SMS_FORMAT_3GPP: ClassVar[int]
        SMS_FORMAT_3GPP2: ClassVar[int]

    class ImsServiceEntitlement:
        KEY_ENTITLEMENT_SERVER_URL_STRING: ClassVar[str]
        KEY_FCM_SENDER_ID_STRING: ClassVar[str]
        KEY_IMS_PROVISIONING_BOOL: ClassVar[str]
        KEY_PREFIX: ClassVar[str]
        KEY_SHOW_VOWIFI_WEBVIEW_BOOL: ClassVar[str]

    class ImsRtt:
        KEY_PREFIX: ClassVar[str]
        KEY_RED_PAYLOAD_TYPE_INT: ClassVar[str]
        KEY_T140_PAYLOAD_TYPE_INT: ClassVar[str]
        KEY_TEXT_AS_BANDWIDTH_KBPS_INT: ClassVar[str]
        KEY_TEXT_CODEC_CAPABILITY_PAYLOAD_TYPES_BUNDLE: ClassVar[str]
        KEY_TEXT_ON_DEFAULT_BEARER_SUPPORTED_BOOL: ClassVar[str]
        KEY_TEXT_QOS_PRECONDITION_SUPPORTED_BOOL: ClassVar[str]
        KEY_TEXT_RR_BANDWIDTH_BPS_INT: ClassVar[str]
        KEY_TEXT_RS_BANDWIDTH_BPS_INT: ClassVar[str]

    class ImsEmergency:
        DOMAIN_CS: ClassVar[int]
        DOMAIN_PS_3GPP: ClassVar[int]
        DOMAIN_PS_NON_3GPP: ClassVar[int]
        KEY_CROSS_STACK_REDIAL_TIMER_SEC_INT: ClassVar[str]
        KEY_EMERGENCY_CALLBACK_MODE_SUPPORTED_BOOL: ClassVar[str]
        KEY_EMERGENCY_CALL_SETUP_TIMER_ON_CURRENT_NETWORK_SEC_INT: ClassVar[str]
        KEY_EMERGENCY_CDMA_PREFERRED_NUMBERS_STRING_ARRAY: ClassVar[str]
        KEY_EMERGENCY_DOMAIN_PREFERENCE_INT_ARRAY: ClassVar[str]
        KEY_EMERGENCY_DOMAIN_PREFERENCE_ROAMING_INT_ARRAY: ClassVar[str]
        KEY_EMERGENCY_LTE_PREFERRED_AFTER_NR_FAILED_BOOL: ClassVar[str]
        KEY_EMERGENCY_NETWORK_SCAN_TYPE_INT: ClassVar[str]
        KEY_EMERGENCY_OVER_CS_ROAMING_SUPPORTED_ACCESS_NETWORK_TYPES_INT_ARRAY: ClassVar[str]
        KEY_EMERGENCY_OVER_CS_SUPPORTED_ACCESS_NETWORK_TYPES_INT_ARRAY: ClassVar[str]
        KEY_EMERGENCY_OVER_IMS_ROAMING_SUPPORTED_3GPP_NETWORK_TYPES_INT_ARRAY: ClassVar[str]
        KEY_EMERGENCY_OVER_IMS_SUPPORTED_3GPP_NETWORK_TYPES_INT_ARRAY: ClassVar[str]
        KEY_EMERGENCY_OVER_IMS_SUPPORTED_RATS_INT_ARRAY: ClassVar[str]
        KEY_EMERGENCY_QOS_PRECONDITION_SUPPORTED_BOOL: ClassVar[str]
        KEY_EMERGENCY_REGISTRATION_TIMER_MILLIS_INT: ClassVar[str]
        KEY_EMERGENCY_REQUIRES_IMS_REGISTRATION_BOOL: ClassVar[str]
        KEY_EMERGENCY_REQUIRES_VOLTE_ENABLED_BOOL: ClassVar[str]
        KEY_EMERGENCY_SCAN_TIMER_SEC_INT: ClassVar[str]
        KEY_EMERGENCY_VOWIFI_REQUIRES_CONDITION_INT: ClassVar[str]
        KEY_MAXIMUM_CELLULAR_SEARCH_TIMER_SEC_INT: ClassVar[str]
        KEY_MAXIMUM_NUMBER_OF_EMERGENCY_TRIES_OVER_VOWIFI_INT: ClassVar[str]
        KEY_PREFER_IMS_EMERGENCY_WHEN_VOICE_CALLS_ON_CS_BOOL: ClassVar[str]
        KEY_PREFIX: ClassVar[str]
        KEY_QUICK_CROSS_STACK_REDIAL_TIMER_SEC_INT: ClassVar[str]
        KEY_REFRESH_GEOLOCATION_TIMEOUT_MILLIS_INT: ClassVar[str]
        KEY_RETRY_EMERGENCY_ON_IMS_PDN_BOOL: ClassVar[str]
        KEY_SCAN_LIMITED_SERVICE_AFTER_VOLTE_FAILURE_BOOL: ClassVar[str]
        KEY_START_QUICK_CROSS_STACK_REDIAL_TIMER_WHEN_REGISTERED_BOOL: ClassVar[str]
        REDIAL_TIMER_DISABLED: ClassVar[int]
        SCAN_TYPE_FULL_SERVICE: ClassVar[int]
        SCAN_TYPE_FULL_SERVICE_FOLLOWED_BY_LIMITED_SERVICE: ClassVar[int]
        SCAN_TYPE_NO_PREFERENCE: ClassVar[int]
        VOWIFI_REQUIRES_NONE: ClassVar[int]
        VOWIFI_REQUIRES_SETTING_ENABLED: ClassVar[int]
        VOWIFI_REQUIRES_VALID_EID: ClassVar[int]

    class Ims:
        E911_RTCP_INACTIVITY_ON_CONNECTED: ClassVar[int]
        E911_RTP_INACTIVITY_ON_CONNECTED: ClassVar[int]
        GEOLOCATION_PIDF_FOR_EMERGENCY_ON_CELLULAR: ClassVar[int]
        GEOLOCATION_PIDF_FOR_EMERGENCY_ON_WIFI: ClassVar[int]
        GEOLOCATION_PIDF_FOR_NON_EMERGENCY_ON_CELLULAR: ClassVar[int]
        GEOLOCATION_PIDF_FOR_NON_EMERGENCY_ON_WIFI: ClassVar[int]
        IPSEC_AUTHENTICATION_ALGORITHM_HMAC_MD5: ClassVar[int]
        IPSEC_AUTHENTICATION_ALGORITHM_HMAC_SHA1: ClassVar[int]
        IPSEC_ENCRYPTION_ALGORITHM_AES_CBC: ClassVar[int]
        IPSEC_ENCRYPTION_ALGORITHM_DES_EDE3_CBC: ClassVar[int]
        IPSEC_ENCRYPTION_ALGORITHM_NULL: ClassVar[int]
        KEY_CAPABILITY_TYPE_CALL_COMPOSER_INT_ARRAY: ClassVar[str]
        KEY_CAPABILITY_TYPE_OPTIONS_UCE_INT_ARRAY: ClassVar[str]
        KEY_CAPABILITY_TYPE_PRESENCE_UCE_INT_ARRAY: ClassVar[str]
        KEY_CAPABILITY_TYPE_SMS_INT_ARRAY: ClassVar[str]
        KEY_CAPABILITY_TYPE_UT_INT_ARRAY: ClassVar[str]
        KEY_CAPABILITY_TYPE_VIDEO_INT_ARRAY: ClassVar[str]
        KEY_CAPABILITY_TYPE_VOICE_INT_ARRAY: ClassVar[str]
        KEY_ENABLE_PRESENCE_CAPABILITY_EXCHANGE_BOOL: ClassVar[str]
        KEY_ENABLE_PRESENCE_GROUP_SUBSCRIBE_BOOL: ClassVar[str]
        KEY_ENABLE_PRESENCE_PUBLISH_BOOL: ClassVar[str]
        KEY_GEOLOCATION_PIDF_IN_SIP_INVITE_SUPPORT_INT_ARRAY: ClassVar[str]
        KEY_GEOLOCATION_PIDF_IN_SIP_REGISTER_SUPPORT_INT_ARRAY: ClassVar[str]
        KEY_GRUU_ENABLED_BOOL: ClassVar[str]
        KEY_IMS_PDN_ENABLED_IN_NO_VOPS_SUPPORT_INT_ARRAY: ClassVar[str]
        KEY_IMS_SINGLE_REGISTRATION_REQUIRED_BOOL: ClassVar[str]
        KEY_IMS_USER_AGENT_STRING: ClassVar[str]
        KEY_IPSEC_AUTHENTICATION_ALGORITHMS_INT_ARRAY: ClassVar[str]
        KEY_IPSEC_ENCRYPTION_ALGORITHMS_INT_ARRAY: ClassVar[str]
        KEY_IPV4_SIP_MTU_SIZE_CELLULAR_INT: ClassVar[str]
        KEY_IPV6_SIP_MTU_SIZE_CELLULAR_INT: ClassVar[str]
        KEY_KEEP_PDN_UP_IN_NO_VOPS_BOOL: ClassVar[str]
        KEY_MMTEL_REQUIRES_PROVISIONING_BUNDLE: ClassVar[str]
        KEY_NON_RCS_CAPABILITIES_CACHE_EXPIRATION_SEC_INT: ClassVar[str]
        KEY_PHONE_CONTEXT_DOMAIN_NAME_STRING: ClassVar[str]
        KEY_PREFIX: ClassVar[str]
        KEY_RCS_BULK_CAPABILITY_EXCHANGE_BOOL: ClassVar[str]
        KEY_RCS_FEATURE_TAG_ALLOWED_STRING_ARRAY: ClassVar[str]
        KEY_RCS_REQUIRES_PROVISIONING_BUNDLE: ClassVar[str]
        KEY_REGISTRATION_EVENT_PACKAGE_SUPPORTED_BOOL: ClassVar[str]
        KEY_REGISTRATION_EXPIRY_TIMER_SEC_INT: ClassVar[str]
        KEY_REGISTRATION_RETRY_BASE_TIMER_MILLIS_INT: ClassVar[str]
        KEY_REGISTRATION_RETRY_MAX_TIMER_MILLIS_INT: ClassVar[str]
        KEY_REGISTRATION_SUBSCRIBE_EXPIRY_TIMER_SEC_INT: ClassVar[str]
        KEY_REQUEST_URI_TYPE_INT: ClassVar[str]
        KEY_SIP_OVER_IPSEC_ENABLED_BOOL: ClassVar[str]
        KEY_SIP_PREFERRED_TRANSPORT_INT: ClassVar[str]
        KEY_SIP_SERVER_PORT_NUMBER_INT: ClassVar[str]
        KEY_SIP_TIMER_B_MILLIS_INT: ClassVar[str]
        KEY_SIP_TIMER_C_MILLIS_INT: ClassVar[str]
        KEY_SIP_TIMER_D_MILLIS_INT: ClassVar[str]
        KEY_SIP_TIMER_F_MILLIS_INT: ClassVar[str]
        KEY_SIP_TIMER_H_MILLIS_INT: ClassVar[str]
        KEY_SIP_TIMER_J_MILLIS_INT: ClassVar[str]
        KEY_SIP_TIMER_T1_MILLIS_INT: ClassVar[str]
        KEY_SIP_TIMER_T2_MILLIS_INT: ClassVar[str]
        KEY_SIP_TIMER_T4_MILLIS_INT: ClassVar[str]
        KEY_SUPPORTED_RATS_INT_ARRAY: ClassVar[str]
        KEY_USE_SIP_URI_FOR_PRESENCE_SUBSCRIBE_BOOL: ClassVar[str]
        KEY_WIFI_OFF_DEFERRING_TIME_MILLIS_INT: ClassVar[str]
        NETWORK_TYPE_HOME: ClassVar[int]
        NETWORK_TYPE_ROAMING: ClassVar[int]
        PREFERRED_TRANSPORT_DYNAMIC_UDP_TCP: ClassVar[int]
        PREFERRED_TRANSPORT_TCP: ClassVar[int]
        PREFERRED_TRANSPORT_TLS: ClassVar[int]
        PREFERRED_TRANSPORT_UDP: ClassVar[int]
        REQUEST_URI_FORMAT_SIP: ClassVar[int]
        REQUEST_URI_FORMAT_TEL: ClassVar[int]
        RTCP_INACTIVITY_ON_CONNECTED: ClassVar[int]
        RTCP_INACTIVITY_ON_HOLD: ClassVar[int]
        RTP_INACTIVITY_ON_CONNECTED: ClassVar[int]

    class Gps:
        KEY_ENABLE_NI_SUPL_MESSAGE_INJECTION_BOOL: ClassVar[str]
        KEY_PERSIST_LPP_MODE_BOOL: ClassVar[str]
        KEY_PREFIX: ClassVar[str]

    class CarrierConfigChangeListener:
        def onCarrierConfigChanged(self, p0: int, p1: int, p2: int, p3: int) -> None: ...

    class Bsf:
        KEY_BSF_SERVER_FQDN_STRING: ClassVar[str]
        KEY_BSF_SERVER_PORT_INT: ClassVar[str]
        KEY_BSF_TRANSPORT_TYPE_INT: ClassVar[str]
        KEY_PREFIX: ClassVar[str]

    class Apn:
        KEY_PREFIX: ClassVar[str]
        KEY_SETTINGS_DEFAULT_PROTOCOL_STRING: ClassVar[str]
        KEY_SETTINGS_DEFAULT_ROAMING_PROTOCOL_STRING: ClassVar[str]
        PROTOCOL_IPV4: ClassVar[str]
        PROTOCOL_IPV4V6: ClassVar[str]
        PROTOCOL_IPV6: ClassVar[str]

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class PhysicalChannelConfig:
    BAND_UNKNOWN: ClassVar[int]
    CELL_BANDWIDTH_UNKNOWN: ClassVar[int]
    CHANNEL_NUMBER_UNKNOWN: ClassVar[int]
    CONNECTION_PRIMARY_SERVING: ClassVar[int]
    CONNECTION_SECONDARY_SERVING: ClassVar[int]
    CONNECTION_UNKNOWN: ClassVar[int]
    CREATOR: ClassVar[Any]
    FREQUENCY_UNKNOWN: ClassVar[int]
    PHYSICAL_CELL_ID_MAXIMUM_VALUE: ClassVar[int]
    PHYSICAL_CELL_ID_UNKNOWN: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getNetworkType(self) -> int: ...
    def getBand(self) -> int: ...
    def getCellBandwidthDownlinkKhz(self) -> int: ...
    def getCellBandwidthUplinkKhz(self) -> int: ...
    def getConnectionStatus(self) -> int: ...
    def getDownlinkChannelNumber(self) -> int: ...
    def getDownlinkFrequencyKhz(self) -> int: ...
    def getPhysicalCellId(self) -> int: ...
    def getUplinkChannelNumber(self) -> int: ...
    def getUplinkFrequencyKhz(self) -> int: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel
from android.telephony.CellIdentity import CellIdentity
from android.telephony.CellSignalStrength import CellSignalStrength

class CellInfoNr:
    CREATOR: ClassVar[Any]
    CONNECTION_NONE: ClassVar[int]
    CONNECTION_PRIMARY_SERVING: ClassVar[int]
    CONNECTION_SECONDARY_SERVING: ClassVar[int]
    CONNECTION_UNKNOWN: ClassVar[int]
    CREATOR: ClassVar[Any]
    UNAVAILABLE: ClassVar[int]
    UNAVAILABLE_LONG: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getCellSignalStrength(self) -> CellSignalStrength: ...
    def getCellIdentity(self) -> CellIdentity: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.net.LinkProperties import LinkProperties
from android.os.Parcel import Parcel
from android.telephony.data.ApnSetting import ApnSetting

class PreciseDataConnectionState:
    CREATOR: ClassVar[Any]
    NETWORK_VALIDATION_FAILURE: ClassVar[int]
    NETWORK_VALIDATION_IN_PROGRESS: ClassVar[int]
    NETWORK_VALIDATION_NOT_REQUESTED: ClassVar[int]
    NETWORK_VALIDATION_SUCCESS: ClassVar[int]
    NETWORK_VALIDATION_UNSUPPORTED: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getLastCauseCode(self) -> int: ...
    def getLinkProperties(self) -> LinkProperties: ...
    def getApnSetting(self) -> ApnSetting: ...
    def getNetworkValidationStatus(self) -> int: ...
    def getTransportType(self) -> int: ...
    def getNetworkType(self) -> int: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def getId(self) -> int: ...
    def getState(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.telephony.mbms.DownloadProgressListener import DownloadProgressListener
from android.telephony.mbms.DownloadRequest import DownloadRequest
from android.telephony.mbms.DownloadStatusListener import DownloadStatusListener
from android.telephony.mbms.FileInfo import FileInfo
from android.telephony.mbms.MbmsDownloadSessionCallback import MbmsDownloadSessionCallback
from java.io.File import File
from java.util.concurrent.Executor import Executor

class MbmsDownloadSession:
    DEFAULT_TOP_LEVEL_TEMP_DIRECTORY: ClassVar[str]
    EXTRA_MBMS_COMPLETED_FILE_URI: ClassVar[str]
    EXTRA_MBMS_DOWNLOAD_REQUEST: ClassVar[str]
    EXTRA_MBMS_DOWNLOAD_RESULT: ClassVar[str]
    EXTRA_MBMS_FILE_INFO: ClassVar[str]
    RESULT_CANCELLED: ClassVar[int]
    RESULT_DOWNLOAD_FAILURE: ClassVar[int]
    RESULT_EXPIRED: ClassVar[int]
    RESULT_FILE_ROOT_UNREACHABLE: ClassVar[int]
    RESULT_IO_ERROR: ClassVar[int]
    RESULT_OUT_OF_STORAGE: ClassVar[int]
    RESULT_SERVICE_ID_NOT_DEFINED: ClassVar[int]
    RESULT_SUCCESSFUL: ClassVar[int]
    STATUS_ACTIVELY_DOWNLOADING: ClassVar[int]
    STATUS_PENDING_DOWNLOAD: ClassVar[int]
    STATUS_PENDING_DOWNLOAD_WINDOW: ClassVar[int]
    STATUS_PENDING_REPAIR: ClassVar[int]
    STATUS_UNKNOWN: ClassVar[int]
    def addProgressListener(self, p0: DownloadRequest, p1: Executor, p2: DownloadProgressListener) -> None: ...
    def addServiceAnnouncement(self, p0: Any) -> None: ...
    def addStatusListener(self, p0: DownloadRequest, p1: Executor, p2: DownloadStatusListener) -> None: ...
    def cancelDownload(self, p0: DownloadRequest) -> None: ...
    @staticmethod
    def getMaximumServiceAnnouncementSize() -> int: ...
    def getTempFileRootDirectory(self) -> File: ...
    def listPendingDownloads(self) -> list: ...
    def removeProgressListener(self, p0: DownloadRequest, p1: DownloadProgressListener) -> None: ...
    def removeStatusListener(self, p0: DownloadRequest, p1: DownloadStatusListener) -> None: ...
    def requestDownloadState(self, p0: DownloadRequest, p1: FileInfo) -> None: ...
    def requestUpdateFileServices(self, p0: list) -> None: ...
    def resetDownloadKnowledge(self, p0: DownloadRequest) -> None: ...
    def setTempFileRootDirectory(self, p0: File) -> None: ...
    def close(self) -> None: ...
    @overload
    @staticmethod
    def create(p0: Context, p1: Executor, p2: MbmsDownloadSessionCallback) -> "MbmsDownloadSession": ...
    @overload
    @staticmethod
    def create(p0: Context, p1: Executor, p2: int, p3: MbmsDownloadSessionCallback) -> "MbmsDownloadSession": ...
    def download(self, p0: DownloadRequest) -> None: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class TelephonyDisplayInfo:
    CREATOR: ClassVar[Any]
    OVERRIDE_NETWORK_TYPE_LTE_ADVANCED_PRO: ClassVar[int]
    OVERRIDE_NETWORK_TYPE_LTE_CA: ClassVar[int]
    OVERRIDE_NETWORK_TYPE_NONE: ClassVar[int]
    OVERRIDE_NETWORK_TYPE_NR_ADVANCED: ClassVar[int]
    OVERRIDE_NETWORK_TYPE_NR_NSA: ClassVar[int]
    OVERRIDE_NETWORK_TYPE_NR_NSA_MMWAVE: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getNetworkType(self) -> int: ...
    def getOverrideNetworkType(self) -> int: ...
    def isRoaming(self) -> bool: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class AvailableNetworkInfo:
    CREATOR: ClassVar[Any]
    PRIORITY_HIGH: ClassVar[int]
    PRIORITY_LOW: ClassVar[int]
    PRIORITY_MED: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def __init__(self, p0: int, p1: int, p2: list, p3: list) -> None: ...
    def getBands(self) -> list: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def getPriority(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def getRadioAccessSpecifiers(self) -> list: ...
    def getMccMncs(self) -> list: ...
    def getSubId(self) -> int: ...

    class Builder:
        def __init__(self, p0: int) -> None: ...
        def build(self) -> "AvailableNetworkInfo": ...
        def setPriority(self, p0: int) -> Any: ...
        def setMccMncs(self, p0: list) -> Any: ...
        def setRadioAccessSpecifiers(self, p0: list) -> Any: ...

from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.content.Intent import Intent
from android.text.Editable import Editable
from android.text.Spannable import Spannable
from android.text.style.TtsSpan import TtsSpan
from java.util.Locale import Locale

class PhoneNumberUtils:
    BCD_EXTENDED_TYPE_CALLED_PARTY: ClassVar[int]
    BCD_EXTENDED_TYPE_EF_ADN: ClassVar[int]
    FORMAT_JAPAN: ClassVar[int]
    FORMAT_NANP: ClassVar[int]
    FORMAT_UNKNOWN: ClassVar[int]
    PAUSE: ClassVar[str]
    TOA_International: ClassVar[int]
    TOA_Unknown: ClassVar[int]
    WAIT: ClassVar[str]
    WILD: ClassVar[str]
    def __init__(self) -> None: ...
    @staticmethod
    def isEmergencyNumber(p0: str) -> bool: ...
    @overload
    @staticmethod
    def compare(p0: Context, p1: str, p2: str) -> bool: ...
    @overload
    @staticmethod
    def compare(p0: str, p1: str) -> bool: ...
    @staticmethod
    def addTtsSpan(p0: Spannable, p1: int, p2: int) -> None: ...
    @staticmethod
    def areSamePhoneNumber(p0: str, p1: str, p2: str) -> bool: ...
    @overload
    @staticmethod
    def calledPartyBCDFragmentToString(p0: Any, p1: int, p2: int) -> str: ...
    @overload
    @staticmethod
    def calledPartyBCDFragmentToString(p0: Any, p1: int, p2: int, p3: int) -> str: ...
    @overload
    @staticmethod
    def calledPartyBCDToString(p0: Any, p1: int, p2: int, p3: int) -> str: ...
    @overload
    @staticmethod
    def calledPartyBCDToString(p0: Any, p1: int, p2: int) -> str: ...
    @staticmethod
    def convertKeypadLettersToDigits(p0: str) -> str: ...
    @staticmethod
    def createTtsSpan(p0: str) -> TtsSpan: ...
    @staticmethod
    def createTtsSpannable(p0: str) -> str: ...
    @staticmethod
    def extractNetworkPortion(p0: str) -> str: ...
    @staticmethod
    def extractPostDialPortion(p0: str) -> str: ...
    @staticmethod
    def formatJapaneseNumber(p0: Editable) -> None: ...
    @staticmethod
    def formatNanpNumber(p0: Editable) -> None: ...
    @overload
    @staticmethod
    def formatNumber(p0: str, p1: str, p2: str) -> str: ...
    @overload
    @staticmethod
    def formatNumber(p0: str, p1: str) -> str: ...
    @overload
    @staticmethod
    def formatNumber(p0: str) -> str: ...
    @overload
    @staticmethod
    def formatNumber(p0: Editable, p1: int) -> None: ...
    @staticmethod
    def formatNumberToE164(p0: str, p1: str) -> str: ...
    @staticmethod
    def formatNumberToRFC3966(p0: str, p1: str) -> str: ...
    @staticmethod
    def getFormatTypeForLocale(p0: Locale) -> int: ...
    @staticmethod
    def getNumberFromIntent(p0: Intent, p1: Context) -> str: ...
    @staticmethod
    def getStrippedReversed(p0: str) -> str: ...
    @staticmethod
    def is12Key(p0: str) -> bool: ...
    @staticmethod
    def isDialable(p0: str) -> bool: ...
    @staticmethod
    def isGlobalPhoneNumber(p0: str) -> bool: ...
    @staticmethod
    def isISODigit(p0: str) -> bool: ...
    @staticmethod
    def isLocalEmergencyNumber(p0: Context, p1: str) -> bool: ...
    @staticmethod
    def isNonSeparator(p0: str) -> bool: ...
    @staticmethod
    def isReallyDialable(p0: str) -> bool: ...
    @staticmethod
    def isStartsPostDial(p0: str) -> bool: ...
    @staticmethod
    def isVoiceMailNumber(p0: str) -> bool: ...
    @staticmethod
    def isWellFormedSmsAddress(p0: str) -> bool: ...
    @staticmethod
    def isWpsCallNumber(p0: str) -> bool: ...
    @staticmethod
    def networkPortionToCalledPartyBCD(p0: str) -> Any: ...
    @staticmethod
    def networkPortionToCalledPartyBCDWithLength(p0: str) -> Any: ...
    @staticmethod
    def normalizeNumber(p0: str) -> str: ...
    @overload
    @staticmethod
    def numberToCalledPartyBCD(p0: str, p1: int) -> Any: ...
    @overload
    @staticmethod
    def numberToCalledPartyBCD(p0: str) -> Any: ...
    @staticmethod
    def replaceUnicodeDigits(p0: str) -> str: ...
    @staticmethod
    def stringFromStringAndTOA(p0: str, p1: int) -> str: ...
    @staticmethod
    def stripSeparators(p0: str) -> str: ...
    @staticmethod
    def toCallerIDMinMatch(p0: str) -> str: ...
    @staticmethod
    def toaFromString(p0: str) -> int: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel
from android.telephony.CellIdentity import CellIdentity

class NetworkRegistrationInfo:
    CREATOR: ClassVar[Any]
    DOMAIN_CS: ClassVar[int]
    DOMAIN_CS_PS: ClassVar[int]
    DOMAIN_PS: ClassVar[int]
    DOMAIN_UNKNOWN: ClassVar[int]
    NR_STATE_CONNECTED: ClassVar[int]
    NR_STATE_NONE: ClassVar[int]
    NR_STATE_NOT_RESTRICTED: ClassVar[int]
    NR_STATE_RESTRICTED: ClassVar[int]
    SERVICE_TYPE_DATA: ClassVar[int]
    SERVICE_TYPE_EMERGENCY: ClassVar[int]
    SERVICE_TYPE_MMS: ClassVar[int]
    SERVICE_TYPE_SMS: ClassVar[int]
    SERVICE_TYPE_UNKNOWN: ClassVar[int]
    SERVICE_TYPE_VIDEO: ClassVar[int]
    SERVICE_TYPE_VOICE: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getTransportType(self) -> int: ...
    def isSearching(self) -> bool: ...
    def getCellIdentity(self) -> CellIdentity: ...
    def isNetworkRoaming(self) -> bool: ...
    def isRoaming(self) -> bool: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def isRegistered(self) -> bool: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def getAccessNetworkTechnology(self) -> int: ...
    def getAvailableServices(self) -> list: ...
    def getDomain(self) -> int: ...
    def getRegisteredPlmn(self) -> str: ...
    def getRejectCause(self) -> int: ...
    def isNetworkRegistered(self) -> bool: ...
    def isNetworkSearching(self) -> bool: ...
    def isNonTerrestrialNetwork(self) -> bool: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class BarringInfo:
    BARRING_SERVICE_TYPE_CS_FALLBACK: ClassVar[int]
    BARRING_SERVICE_TYPE_CS_SERVICE: ClassVar[int]
    BARRING_SERVICE_TYPE_CS_VOICE: ClassVar[int]
    BARRING_SERVICE_TYPE_EMERGENCY: ClassVar[int]
    BARRING_SERVICE_TYPE_MMTEL_VIDEO: ClassVar[int]
    BARRING_SERVICE_TYPE_MMTEL_VOICE: ClassVar[int]
    BARRING_SERVICE_TYPE_MO_DATA: ClassVar[int]
    BARRING_SERVICE_TYPE_MO_SIGNALLING: ClassVar[int]
    BARRING_SERVICE_TYPE_PS_SERVICE: ClassVar[int]
    BARRING_SERVICE_TYPE_SMS: ClassVar[int]
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getBarringServiceInfo(self, p0: int) -> Any: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

    class BarringServiceInfo:
        BARRING_TYPE_CONDITIONAL: ClassVar[int]
        BARRING_TYPE_NONE: ClassVar[int]
        BARRING_TYPE_UNCONDITIONAL: ClassVar[int]
        BARRING_TYPE_UNKNOWN: ClassVar[int]
        CREATOR: ClassVar[Any]
        CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
        PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
        def getBarringType(self) -> int: ...
        def getConditionalBarringFactor(self) -> int: ...
        def getConditionalBarringTimeSeconds(self) -> int: ...
        def isBarred(self) -> bool: ...
        def isConditionallyBarred(self) -> bool: ...
        def equals(self, p0: Any) -> bool: ...
        def toString(self) -> str: ...
        def hashCode(self) -> int: ...
        def describeContents(self) -> int: ...
        def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload

class AccessNetworkConstants:
    TRANSPORT_TYPE_WLAN: ClassVar[int]
    TRANSPORT_TYPE_WWAN: ClassVar[int]

    class UtranBand:
        BAND_1: ClassVar[int]
        BAND_10: ClassVar[int]
        BAND_11: ClassVar[int]
        BAND_12: ClassVar[int]
        BAND_13: ClassVar[int]
        BAND_14: ClassVar[int]
        BAND_19: ClassVar[int]
        BAND_2: ClassVar[int]
        BAND_20: ClassVar[int]
        BAND_21: ClassVar[int]
        BAND_22: ClassVar[int]
        BAND_25: ClassVar[int]
        BAND_26: ClassVar[int]
        BAND_3: ClassVar[int]
        BAND_4: ClassVar[int]
        BAND_5: ClassVar[int]
        BAND_6: ClassVar[int]
        BAND_7: ClassVar[int]
        BAND_8: ClassVar[int]
        BAND_9: ClassVar[int]
        BAND_A: ClassVar[int]
        BAND_B: ClassVar[int]
        BAND_C: ClassVar[int]
        BAND_D: ClassVar[int]
        BAND_E: ClassVar[int]
        BAND_F: ClassVar[int]

    class NgranBands:
        BAND_1: ClassVar[int]
        BAND_12: ClassVar[int]
        BAND_14: ClassVar[int]
        BAND_18: ClassVar[int]
        BAND_2: ClassVar[int]
        BAND_20: ClassVar[int]
        BAND_25: ClassVar[int]
        BAND_257: ClassVar[int]
        BAND_258: ClassVar[int]
        BAND_26: ClassVar[int]
        BAND_260: ClassVar[int]
        BAND_261: ClassVar[int]
        BAND_28: ClassVar[int]
        BAND_29: ClassVar[int]
        BAND_3: ClassVar[int]
        BAND_30: ClassVar[int]
        BAND_34: ClassVar[int]
        BAND_38: ClassVar[int]
        BAND_39: ClassVar[int]
        BAND_40: ClassVar[int]
        BAND_41: ClassVar[int]
        BAND_46: ClassVar[int]
        BAND_48: ClassVar[int]
        BAND_5: ClassVar[int]
        BAND_50: ClassVar[int]
        BAND_51: ClassVar[int]
        BAND_53: ClassVar[int]
        BAND_65: ClassVar[int]
        BAND_66: ClassVar[int]
        BAND_7: ClassVar[int]
        BAND_70: ClassVar[int]
        BAND_71: ClassVar[int]
        BAND_74: ClassVar[int]
        BAND_75: ClassVar[int]
        BAND_76: ClassVar[int]
        BAND_77: ClassVar[int]
        BAND_78: ClassVar[int]
        BAND_79: ClassVar[int]
        BAND_8: ClassVar[int]
        BAND_80: ClassVar[int]
        BAND_81: ClassVar[int]
        BAND_82: ClassVar[int]
        BAND_83: ClassVar[int]
        BAND_84: ClassVar[int]
        BAND_86: ClassVar[int]
        BAND_89: ClassVar[int]
        BAND_90: ClassVar[int]
        BAND_91: ClassVar[int]
        BAND_92: ClassVar[int]
        BAND_93: ClassVar[int]
        BAND_94: ClassVar[int]
        BAND_95: ClassVar[int]
        BAND_96: ClassVar[int]

    class GeranBand:
        BAND_450: ClassVar[int]
        BAND_480: ClassVar[int]
        BAND_710: ClassVar[int]
        BAND_750: ClassVar[int]
        BAND_850: ClassVar[int]
        BAND_DCS1800: ClassVar[int]
        BAND_E900: ClassVar[int]
        BAND_ER900: ClassVar[int]
        BAND_P900: ClassVar[int]
        BAND_PCS1900: ClassVar[int]
        BAND_R900: ClassVar[int]
        BAND_T380: ClassVar[int]
        BAND_T410: ClassVar[int]
        BAND_T810: ClassVar[int]

    class EutranBand:
        BAND_1: ClassVar[int]
        BAND_10: ClassVar[int]
        BAND_11: ClassVar[int]
        BAND_12: ClassVar[int]
        BAND_13: ClassVar[int]
        BAND_14: ClassVar[int]
        BAND_17: ClassVar[int]
        BAND_18: ClassVar[int]
        BAND_19: ClassVar[int]
        BAND_2: ClassVar[int]
        BAND_20: ClassVar[int]
        BAND_21: ClassVar[int]
        BAND_22: ClassVar[int]
        BAND_23: ClassVar[int]
        BAND_24: ClassVar[int]
        BAND_25: ClassVar[int]
        BAND_26: ClassVar[int]
        BAND_27: ClassVar[int]
        BAND_28: ClassVar[int]
        BAND_3: ClassVar[int]
        BAND_30: ClassVar[int]
        BAND_31: ClassVar[int]
        BAND_33: ClassVar[int]
        BAND_34: ClassVar[int]
        BAND_35: ClassVar[int]
        BAND_36: ClassVar[int]
        BAND_37: ClassVar[int]
        BAND_38: ClassVar[int]
        BAND_39: ClassVar[int]
        BAND_4: ClassVar[int]
        BAND_40: ClassVar[int]
        BAND_41: ClassVar[int]
        BAND_42: ClassVar[int]
        BAND_43: ClassVar[int]
        BAND_44: ClassVar[int]
        BAND_45: ClassVar[int]
        BAND_46: ClassVar[int]
        BAND_47: ClassVar[int]
        BAND_48: ClassVar[int]
        BAND_49: ClassVar[int]
        BAND_5: ClassVar[int]
        BAND_50: ClassVar[int]
        BAND_51: ClassVar[int]
        BAND_52: ClassVar[int]
        BAND_53: ClassVar[int]
        BAND_6: ClassVar[int]
        BAND_65: ClassVar[int]
        BAND_66: ClassVar[int]
        BAND_68: ClassVar[int]
        BAND_7: ClassVar[int]
        BAND_70: ClassVar[int]
        BAND_71: ClassVar[int]
        BAND_72: ClassVar[int]
        BAND_73: ClassVar[int]
        BAND_74: ClassVar[int]
        BAND_8: ClassVar[int]
        BAND_85: ClassVar[int]
        BAND_87: ClassVar[int]
        BAND_88: ClassVar[int]
        BAND_9: ClassVar[int]

    class AccessNetworkType:
        CDMA2000: ClassVar[int]
        EUTRAN: ClassVar[int]
        GERAN: ClassVar[int]
        IWLAN: ClassVar[int]
        NGRAN: ClassVar[int]
        UNKNOWN: ClassVar[int]
        UTRAN: ClassVar[int]

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel
from android.telephony.ClosedSubscriberGroupInfo import ClosedSubscriberGroupInfo

class CellIdentityWcdma:
    CREATOR: ClassVar[Any]
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getMcc(self) -> int: ...
    def getMnc(self) -> int: ...
    def getPsc(self) -> int: ...
    def getCid(self) -> int: ...
    def getLac(self) -> int: ...
    def getClosedSubscriberGroupInfo(self) -> ClosedSubscriberGroupInfo: ...
    def getAdditionalPlmns(self) -> set: ...
    def getMccString(self) -> str: ...
    def getMncString(self) -> str: ...
    def getMobileNetworkOperator(self) -> str: ...
    def getUarfcn(self) -> int: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.graphics.Bitmap import Bitmap
from android.os.Parcel import Parcel
from android.os.ParcelUuid import ParcelUuid

class SubscriptionInfo:
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getSimSlotIndex(self) -> int: ...
    def getCarrierId(self) -> int: ...
    def getMcc(self) -> int: ...
    def getMnc(self) -> int: ...
    def getSubscriptionId(self) -> int: ...
    def getCardId(self) -> int: ...
    def getCountryIso(self) -> str: ...
    def getDataRoaming(self) -> int: ...
    def getGroupUuid(self) -> ParcelUuid: ...
    def getIccId(self) -> str: ...
    def createIconBitmap(self, p0: Context) -> Bitmap: ...
    def getCarrierName(self) -> str: ...
    def getIconTint(self) -> int: ...
    def getPortIndex(self) -> int: ...
    def getServiceCapabilities(self) -> set: ...
    def getSubscriptionType(self) -> int: ...
    def getUsageSetting(self) -> int: ...
    def isEmbedded(self) -> bool: ...
    def isOnlyNonTerrestrialNetwork(self) -> bool: ...
    def isOpportunistic(self) -> bool: ...
    def getMccString(self) -> str: ...
    def getMncString(self) -> str: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def getDisplayName(self) -> str: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def getNumber(self) -> str: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel
from android.telephony.CellIdentity import CellIdentity
from android.telephony.CellSignalStrength import CellSignalStrength

class CellInfo:
    CONNECTION_NONE: ClassVar[int]
    CONNECTION_PRIMARY_SERVING: ClassVar[int]
    CONNECTION_SECONDARY_SERVING: ClassVar[int]
    CONNECTION_UNKNOWN: ClassVar[int]
    CREATOR: ClassVar[Any]
    UNAVAILABLE: ClassVar[int]
    UNAVAILABLE_LONG: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getCellConnectionStatus(self) -> int: ...
    def getTimeStamp(self) -> int: ...
    def getCellSignalStrength(self) -> CellSignalStrength: ...
    def getCellIdentity(self) -> CellIdentity: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def isRegistered(self) -> bool: ...
    def getTimestampMillis(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

