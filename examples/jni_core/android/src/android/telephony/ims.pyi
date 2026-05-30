from typing import Any, ClassVar, overload
from android.telephony.ims.ImsStateCallback import ImsStateCallback
from java.util.concurrent.Executor import Executor
from java.util.function.Consumer import Consumer

class ImsMmTelManager:
    WIFI_MODE_CELLULAR_PREFERRED: ClassVar[int]
    WIFI_MODE_WIFI_ONLY: ClassVar[int]
    WIFI_MODE_WIFI_PREFERRED: ClassVar[int]
    REGISTRATION_STATE_NOT_REGISTERED: ClassVar[int]
    REGISTRATION_STATE_REGISTERED: ClassVar[int]
    REGISTRATION_STATE_REGISTERING: ClassVar[int]
    def isTtyOverVolteEnabled(self) -> bool: ...
    def isVoWiFiRoamingSettingEnabled(self) -> bool: ...
    def isVoWiFiSettingEnabled(self) -> bool: ...
    def isVtSettingEnabled(self) -> bool: ...
    def registerImsRegistrationCallback(self, p0: Executor, p1: Any) -> None: ...
    def getRegistrationState(self, p0: Executor, p1: Consumer) -> None: ...
    def getRegistrationTransportType(self, p0: Executor, p1: Consumer) -> None: ...
    def getVoWiFiModeSetting(self) -> int: ...
    def isAdvancedCallingSettingEnabled(self) -> bool: ...
    def isCrossSimCallingEnabled(self) -> bool: ...
    def registerImsStateCallback(self, p0: Executor, p1: ImsStateCallback) -> None: ...
    def registerMmTelCapabilityCallback(self, p0: Executor, p1: Any) -> None: ...
    def unregisterImsRegistrationCallback(self, p0: Any) -> None: ...
    def unregisterImsStateCallback(self, p0: ImsStateCallback) -> None: ...
    def unregisterMmTelCapabilityCallback(self, p0: Any) -> None: ...

    class CapabilityCallback:
        def __init__(self) -> None: ...
        def onCapabilitiesStatusChanged(self, p0: Any) -> None: ...

from typing import Any, ClassVar, overload

class RcsUceAdapter:
    def isUceSettingEnabled(self) -> bool: ...

from typing import Any, ClassVar, overload
from android.telephony.ims.ImsStateCallback import ImsStateCallback
from android.telephony.ims.RcsUceAdapter import RcsUceAdapter
from java.util.concurrent.Executor import Executor
from java.util.function.Consumer import Consumer

class ImsRcsManager:
    ACTION_SHOW_CAPABILITY_DISCOVERY_OPT_IN: ClassVar[str]
    CAPABILITY_TYPE_NONE: ClassVar[int]
    CAPABILITY_TYPE_OPTIONS_UCE: ClassVar[int]
    CAPABILITY_TYPE_PRESENCE_UCE: ClassVar[int]
    def registerImsRegistrationCallback(self, p0: Executor, p1: Any) -> None: ...
    def getRegistrationState(self, p0: Executor, p1: Consumer) -> None: ...
    def getRegistrationTransportType(self, p0: Executor, p1: Consumer) -> None: ...
    def registerImsStateCallback(self, p0: Executor, p1: ImsStateCallback) -> None: ...
    def unregisterImsRegistrationCallback(self, p0: Any) -> None: ...
    def unregisterImsStateCallback(self, p0: ImsStateCallback) -> None: ...
    def getUceAdapter(self) -> RcsUceAdapter: ...

from typing import Any, ClassVar, overload
from android.telephony.ims.ImsReasonInfo import ImsReasonInfo
from android.telephony.ims.ImsRegistrationAttributes import ImsRegistrationAttributes
from java.util.concurrent.Executor import Executor
from java.util.function.Consumer import Consumer

class RegistrationManager:
    REGISTRATION_STATE_NOT_REGISTERED: ClassVar[int]
    REGISTRATION_STATE_REGISTERED: ClassVar[int]
    REGISTRATION_STATE_REGISTERING: ClassVar[int]
    def registerImsRegistrationCallback(self, p0: Executor, p1: Any) -> None: ...
    def getRegistrationState(self, p0: Executor, p1: Consumer) -> None: ...
    def getRegistrationTransportType(self, p0: Executor, p1: Consumer) -> None: ...
    def unregisterImsRegistrationCallback(self, p0: Any) -> None: ...

    class RegistrationCallback:
        def __init__(self) -> None: ...
        @overload
        def onRegistered(self, p0: int) -> None: ...
        @overload
        def onRegistered(self, p0: ImsRegistrationAttributes) -> None: ...
        def onTechnologyChangeFailed(self, p0: int, p1: ImsReasonInfo) -> None: ...
        @overload
        def onRegistering(self, p0: int) -> None: ...
        @overload
        def onRegistering(self, p0: ImsRegistrationAttributes) -> None: ...
        def onUnregistered(self, p0: ImsReasonInfo) -> None: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel
from android.telephony.ims.SipDetails import SipDetails

class ImsRegistrationAttributes:
    ATTR_EPDG_OVER_CELL_INTERNET: ClassVar[int]
    CREATOR: ClassVar[Any]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getTransportType(self) -> int: ...
    def getFeatureTags(self) -> set: ...
    def getAttributeFlags(self) -> int: ...
    def getSipDetails(self) -> SipDetails: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload

class ImsException:
    CODE_ERROR_INVALID_SUBSCRIPTION: ClassVar[int]
    CODE_ERROR_SERVICE_UNAVAILABLE: ClassVar[int]
    CODE_ERROR_UNSPECIFIED: ClassVar[int]
    CODE_ERROR_UNSUPPORTED_OPERATION: ClassVar[int]
    def getCode(self) -> int: ...

from typing import Any, ClassVar, overload
from android.telephony.ims.ImsMmTelManager import ImsMmTelManager
from android.telephony.ims.ImsRcsManager import ImsRcsManager
from android.telephony.ims.ProvisioningManager import ProvisioningManager

class ImsManager:
    ACTION_WFC_IMS_REGISTRATION_ERROR: ClassVar[str]
    EXTRA_WFC_REGISTRATION_FAILURE_MESSAGE: ClassVar[str]
    EXTRA_WFC_REGISTRATION_FAILURE_TITLE: ClassVar[str]
    def getImsMmTelManager(self, p0: int) -> ImsMmTelManager: ...
    def getImsRcsManager(self, p0: int) -> ImsRcsManager: ...
    def getProvisioningManager(self, p0: int) -> ProvisioningManager: ...

from typing import Any, ClassVar, overload

class ImsStateCallback:
    REASON_IMS_SERVICE_DISCONNECTED: ClassVar[int]
    REASON_IMS_SERVICE_NOT_READY: ClassVar[int]
    REASON_NO_IMS_SERVICE_CONFIGURED: ClassVar[int]
    REASON_SUBSCRIPTION_INACTIVE: ClassVar[int]
    REASON_UNKNOWN_PERMANENT_ERROR: ClassVar[int]
    REASON_UNKNOWN_TEMPORARY_ERROR: ClassVar[int]
    def __init__(self) -> None: ...
    def onAvailable(self) -> None: ...
    def onUnavailable(self, p0: int) -> None: ...
    def onError(self) -> None: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class SipDetails:
    CREATOR: ClassVar[Any]
    METHOD_PUBLISH: ClassVar[int]
    METHOD_REGISTER: ClassVar[int]
    METHOD_SUBSCRIBE: ClassVar[int]
    METHOD_UNKNOWN: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getCSeq(self) -> int: ...
    def getCallId(self) -> str: ...
    def getReasonHeaderCause(self) -> int: ...
    def getReasonHeaderText(self) -> str: ...
    def getResponsePhrase(self) -> str: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def getMethod(self) -> int: ...
    def getResponseCode(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

class ImsReasonInfo:
    CODE_ACCESS_CLASS_BLOCKED: ClassVar[int]
    CODE_ANSWERED_ELSEWHERE: ClassVar[int]
    CODE_BLACKLISTED_CALL_ID: ClassVar[int]
    CODE_CALL_BARRED: ClassVar[int]
    CODE_CALL_DROP_IWLAN_TO_LTE_UNAVAILABLE: ClassVar[int]
    CODE_CALL_END_CAUSE_CALL_PULL: ClassVar[int]
    CODE_CALL_PULL_OUT_OF_SYNC: ClassVar[int]
    CODE_DATA_DISABLED: ClassVar[int]
    CODE_DATA_LIMIT_REACHED: ClassVar[int]
    CODE_DIAL_MODIFIED_TO_DIAL: ClassVar[int]
    CODE_DIAL_MODIFIED_TO_DIAL_VIDEO: ClassVar[int]
    CODE_DIAL_MODIFIED_TO_SS: ClassVar[int]
    CODE_DIAL_MODIFIED_TO_USSD: ClassVar[int]
    CODE_DIAL_VIDEO_MODIFIED_TO_DIAL: ClassVar[int]
    CODE_DIAL_VIDEO_MODIFIED_TO_DIAL_VIDEO: ClassVar[int]
    CODE_DIAL_VIDEO_MODIFIED_TO_SS: ClassVar[int]
    CODE_DIAL_VIDEO_MODIFIED_TO_USSD: ClassVar[int]
    CODE_ECBM_NOT_SUPPORTED: ClassVar[int]
    CODE_EMERGENCY_PERM_FAILURE: ClassVar[int]
    CODE_EMERGENCY_TEMP_FAILURE: ClassVar[int]
    CODE_EPDG_TUNNEL_ESTABLISH_FAILURE: ClassVar[int]
    CODE_EPDG_TUNNEL_LOST_CONNECTION: ClassVar[int]
    CODE_EPDG_TUNNEL_REKEY_FAILURE: ClassVar[int]
    CODE_FDN_BLOCKED: ClassVar[int]
    CODE_IKEV2_AUTH_FAILURE: ClassVar[int]
    CODE_IMEI_NOT_ACCEPTED: ClassVar[int]
    CODE_IWLAN_DPD_FAILURE: ClassVar[int]
    CODE_LOCAL_CALL_BUSY: ClassVar[int]
    CODE_LOCAL_CALL_CS_RETRY_REQUIRED: ClassVar[int]
    CODE_LOCAL_CALL_DECLINE: ClassVar[int]
    CODE_LOCAL_CALL_EXCEEDED: ClassVar[int]
    CODE_LOCAL_CALL_RESOURCE_RESERVATION_FAILED: ClassVar[int]
    CODE_LOCAL_CALL_TERMINATED: ClassVar[int]
    CODE_LOCAL_CALL_VCC_ON_PROGRESSING: ClassVar[int]
    CODE_LOCAL_CALL_VOLTE_RETRY_REQUIRED: ClassVar[int]
    CODE_LOCAL_ENDED_BY_CONFERENCE_MERGE: ClassVar[int]
    CODE_LOCAL_HO_NOT_FEASIBLE: ClassVar[int]
    CODE_LOCAL_ILLEGAL_ARGUMENT: ClassVar[int]
    CODE_LOCAL_ILLEGAL_STATE: ClassVar[int]
    CODE_LOCAL_IMS_SERVICE_DOWN: ClassVar[int]
    CODE_LOCAL_INTERNAL_ERROR: ClassVar[int]
    CODE_LOCAL_LOW_BATTERY: ClassVar[int]
    CODE_LOCAL_NETWORK_IP_CHANGED: ClassVar[int]
    CODE_LOCAL_NETWORK_NO_LTE_COVERAGE: ClassVar[int]
    CODE_LOCAL_NETWORK_NO_SERVICE: ClassVar[int]
    CODE_LOCAL_NETWORK_ROAMING: ClassVar[int]
    CODE_LOCAL_NOT_REGISTERED: ClassVar[int]
    CODE_LOCAL_NO_PENDING_CALL: ClassVar[int]
    CODE_LOCAL_POWER_OFF: ClassVar[int]
    CODE_LOCAL_SERVICE_UNAVAILABLE: ClassVar[int]
    CODE_LOW_BATTERY: ClassVar[int]
    CODE_MAXIMUM_NUMBER_OF_CALLS_REACHED: ClassVar[int]
    CODE_MEDIA_INIT_FAILED: ClassVar[int]
    CODE_MEDIA_NOT_ACCEPTABLE: ClassVar[int]
    CODE_MEDIA_NO_DATA: ClassVar[int]
    CODE_MEDIA_UNSPECIFIED: ClassVar[int]
    CODE_MULTIENDPOINT_NOT_SUPPORTED: ClassVar[int]
    CODE_NETWORK_CONGESTION: ClassVar[int]
    CODE_NETWORK_DETACH: ClassVar[int]
    CODE_NETWORK_REJECT: ClassVar[int]
    CODE_NETWORK_RESP_TIMEOUT: ClassVar[int]
    CODE_NO_CSFB_IN_CS_ROAM: ClassVar[int]
    CODE_NO_VALID_SIM: ClassVar[int]
    CODE_OEM_CAUSE_1: ClassVar[int]
    CODE_OEM_CAUSE_10: ClassVar[int]
    CODE_OEM_CAUSE_11: ClassVar[int]
    CODE_OEM_CAUSE_12: ClassVar[int]
    CODE_OEM_CAUSE_13: ClassVar[int]
    CODE_OEM_CAUSE_14: ClassVar[int]
    CODE_OEM_CAUSE_15: ClassVar[int]
    CODE_OEM_CAUSE_2: ClassVar[int]
    CODE_OEM_CAUSE_3: ClassVar[int]
    CODE_OEM_CAUSE_4: ClassVar[int]
    CODE_OEM_CAUSE_5: ClassVar[int]
    CODE_OEM_CAUSE_6: ClassVar[int]
    CODE_OEM_CAUSE_7: ClassVar[int]
    CODE_OEM_CAUSE_8: ClassVar[int]
    CODE_OEM_CAUSE_9: ClassVar[int]
    CODE_RADIO_ACCESS_FAILURE: ClassVar[int]
    CODE_RADIO_INTERNAL_ERROR: ClassVar[int]
    CODE_RADIO_LINK_FAILURE: ClassVar[int]
    CODE_RADIO_LINK_LOST: ClassVar[int]
    CODE_RADIO_OFF: ClassVar[int]
    CODE_RADIO_RELEASE_ABNORMAL: ClassVar[int]
    CODE_RADIO_RELEASE_NORMAL: ClassVar[int]
    CODE_RADIO_SETUP_FAILURE: ClassVar[int]
    CODE_RADIO_UPLINK_FAILURE: ClassVar[int]
    CODE_REGISTRATION_ERROR: ClassVar[int]
    CODE_REJECTED_ELSEWHERE: ClassVar[int]
    CODE_REJECT_1X_COLLISION: ClassVar[int]
    CODE_REJECT_CALL_ON_OTHER_SUB: ClassVar[int]
    CODE_REJECT_CALL_TYPE_NOT_ALLOWED: ClassVar[int]
    CODE_REJECT_CONFERENCE_TTY_NOT_ALLOWED: ClassVar[int]
    CODE_REJECT_INTERNAL_ERROR: ClassVar[int]
    CODE_REJECT_MAX_CALL_LIMIT_REACHED: ClassVar[int]
    CODE_REJECT_ONGOING_CALL_SETUP: ClassVar[int]
    CODE_REJECT_ONGOING_CALL_TRANSFER: ClassVar[int]
    CODE_REJECT_ONGOING_CALL_UPGRADE: ClassVar[int]
    CODE_REJECT_ONGOING_CALL_WAITING_DISABLED: ClassVar[int]
    CODE_REJECT_ONGOING_CONFERENCE_CALL: ClassVar[int]
    CODE_REJECT_ONGOING_CS_CALL: ClassVar[int]
    CODE_REJECT_ONGOING_E911_CALL: ClassVar[int]
    CODE_REJECT_ONGOING_ENCRYPTED_CALL: ClassVar[int]
    CODE_REJECT_ONGOING_HANDOVER: ClassVar[int]
    CODE_REJECT_QOS_FAILURE: ClassVar[int]
    CODE_REJECT_SERVICE_NOT_REGISTERED: ClassVar[int]
    CODE_REJECT_UNKNOWN: ClassVar[int]
    CODE_REJECT_UNSUPPORTED_SDP_HEADERS: ClassVar[int]
    CODE_REJECT_UNSUPPORTED_SIP_HEADERS: ClassVar[int]
    CODE_REJECT_VT_AVPF_NOT_ALLOWED: ClassVar[int]
    CODE_REJECT_VT_TTY_NOT_ALLOWED: ClassVar[int]
    CODE_REMOTE_CALL_DECLINE: ClassVar[int]
    CODE_SESSION_MODIFICATION_FAILED: ClassVar[int]
    CODE_SIP_ALTERNATE_EMERGENCY_CALL: ClassVar[int]
    CODE_SIP_AMBIGUOUS: ClassVar[int]
    CODE_SIP_BAD_ADDRESS: ClassVar[int]
    CODE_SIP_BAD_REQUEST: ClassVar[int]
    CODE_SIP_BUSY: ClassVar[int]
    CODE_SIP_CALL_OR_TRANS_DOES_NOT_EXIST: ClassVar[int]
    CODE_SIP_CLIENT_ERROR: ClassVar[int]
    CODE_SIP_EXTENSION_REQUIRED: ClassVar[int]
    CODE_SIP_FORBIDDEN: ClassVar[int]
    CODE_SIP_GLOBAL_ERROR: ClassVar[int]
    CODE_SIP_INTERVAL_TOO_BRIEF: ClassVar[int]
    CODE_SIP_LOOP_DETECTED: ClassVar[int]
    CODE_SIP_METHOD_NOT_ALLOWED: ClassVar[int]
    CODE_SIP_NOT_ACCEPTABLE: ClassVar[int]
    CODE_SIP_NOT_FOUND: ClassVar[int]
    CODE_SIP_NOT_REACHABLE: ClassVar[int]
    CODE_SIP_NOT_SUPPORTED: ClassVar[int]
    CODE_SIP_PROXY_AUTHENTICATION_REQUIRED: ClassVar[int]
    CODE_SIP_REDIRECTED: ClassVar[int]
    CODE_SIP_REQUEST_CANCELLED: ClassVar[int]
    CODE_SIP_REQUEST_ENTITY_TOO_LARGE: ClassVar[int]
    CODE_SIP_REQUEST_PENDING: ClassVar[int]
    CODE_SIP_REQUEST_TIMEOUT: ClassVar[int]
    CODE_SIP_REQUEST_URI_TOO_LARGE: ClassVar[int]
    CODE_SIP_SERVER_ERROR: ClassVar[int]
    CODE_SIP_SERVER_INTERNAL_ERROR: ClassVar[int]
    CODE_SIP_SERVER_TIMEOUT: ClassVar[int]
    CODE_SIP_SERVICE_UNAVAILABLE: ClassVar[int]
    CODE_SIP_TEMPRARILY_UNAVAILABLE: ClassVar[int]
    CODE_SIP_TOO_MANY_HOPS: ClassVar[int]
    CODE_SIP_TRANSACTION_DOES_NOT_EXIST: ClassVar[int]
    CODE_SIP_UNDECIPHERABLE: ClassVar[int]
    CODE_SIP_USER_MARKED_UNWANTED: ClassVar[int]
    CODE_SIP_USER_REJECTED: ClassVar[int]
    CODE_SUPP_SVC_CANCELLED: ClassVar[int]
    CODE_SUPP_SVC_FAILED: ClassVar[int]
    CODE_SUPP_SVC_REINVITE_COLLISION: ClassVar[int]
    CODE_TIMEOUT_1XX_WAITING: ClassVar[int]
    CODE_TIMEOUT_NO_ANSWER: ClassVar[int]
    CODE_TIMEOUT_NO_ANSWER_CALL_UPDATE: ClassVar[int]
    CODE_UNSPECIFIED: ClassVar[int]
    CODE_USER_CANCELLED_SESSION_MODIFICATION: ClassVar[int]
    CODE_USER_DECLINE: ClassVar[int]
    CODE_USER_IGNORE: ClassVar[int]
    CODE_USER_NOANSWER: ClassVar[int]
    CODE_USER_REJECTED_SESSION_MODIFICATION: ClassVar[int]
    CODE_USER_TERMINATED: ClassVar[int]
    CODE_USER_TERMINATED_BY_REMOTE: ClassVar[int]
    CODE_UT_CB_PASSWORD_MISMATCH: ClassVar[int]
    CODE_UT_NETWORK_ERROR: ClassVar[int]
    CODE_UT_NOT_SUPPORTED: ClassVar[int]
    CODE_UT_OPERATION_NOT_ALLOWED: ClassVar[int]
    CODE_UT_SERVICE_UNAVAILABLE: ClassVar[int]
    CODE_UT_SS_MODIFIED_TO_DIAL: ClassVar[int]
    CODE_UT_SS_MODIFIED_TO_DIAL_VIDEO: ClassVar[int]
    CODE_UT_SS_MODIFIED_TO_SS: ClassVar[int]
    CODE_UT_SS_MODIFIED_TO_USSD: ClassVar[int]
    CODE_WIFI_LOST: ClassVar[int]
    CREATOR: ClassVar[Any]
    EXTRA_CODE_CALL_RETRY_BY_SETTINGS: ClassVar[int]
    EXTRA_CODE_CALL_RETRY_EMERGENCY: ClassVar[int]
    EXTRA_CODE_CALL_RETRY_NORMAL: ClassVar[int]
    EXTRA_CODE_CALL_RETRY_SILENT_REDIAL: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def __init__(self, p0: int, p1: int, p2: str) -> None: ...
    def getExtraCode(self) -> int: ...
    def getExtraMessage(self) -> str: ...
    def toString(self) -> str: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def getCode(self) -> int: ...

from typing import Any, ClassVar, overload
from java.util.concurrent.Executor import Executor

class ProvisioningManager:
    def getProvisioningStatusForCapability(self, p0: int, p1: int) -> bool: ...
    def getRcsProvisioningStatusForCapability(self, p0: int, p1: int) -> bool: ...
    def isProvisioningRequiredForCapability(self, p0: int, p1: int) -> bool: ...
    def isRcsProvisioningRequiredForCapability(self, p0: int, p1: int) -> bool: ...
    def registerFeatureProvisioningChangedCallback(self, p0: Executor, p1: Any) -> None: ...
    def setProvisioningStatusForCapability(self, p0: int, p1: int, p2: bool) -> None: ...
    def setRcsProvisioningStatusForCapability(self, p0: int, p1: int, p2: bool) -> None: ...
    def unregisterFeatureProvisioningChangedCallback(self, p0: Any) -> None: ...

    class FeatureProvisioningCallback:
        def __init__(self) -> None: ...
        def onRcsFeatureProvisioningChanged(self, p0: int, p1: int, p2: bool) -> None: ...
        def onFeatureProvisioningChanged(self, p0: int, p1: int, p2: bool) -> None: ...

