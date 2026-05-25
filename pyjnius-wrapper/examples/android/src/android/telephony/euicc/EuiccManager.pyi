from typing import Any, ClassVar, overload
from android.app.Activity import Activity
from android.app.PendingIntent import PendingIntent
from android.content.Intent import Intent
from android.telephony.euicc.DownloadableSubscription import DownloadableSubscription
from android.telephony.euicc.EuiccInfo import EuiccInfo

class EuiccManager:
    ACTION_MANAGE_EMBEDDED_SUBSCRIPTIONS: ClassVar[str]
    ACTION_NOTIFY_CARRIER_SETUP_INCOMPLETE: ClassVar[str]
    ACTION_START_EUICC_ACTIVATION: ClassVar[str]
    EMBEDDED_SUBSCRIPTION_RESULT_ERROR: ClassVar[int]
    EMBEDDED_SUBSCRIPTION_RESULT_OK: ClassVar[int]
    EMBEDDED_SUBSCRIPTION_RESULT_RESOLVABLE_ERROR: ClassVar[int]
    ERROR_ADDRESS_MISSING: ClassVar[int]
    ERROR_CARRIER_LOCKED: ClassVar[int]
    ERROR_CERTIFICATE_ERROR: ClassVar[int]
    ERROR_CONNECTION_ERROR: ClassVar[int]
    ERROR_DISALLOWED_BY_PPR: ClassVar[int]
    ERROR_EUICC_INSUFFICIENT_MEMORY: ClassVar[int]
    ERROR_EUICC_MISSING: ClassVar[int]
    ERROR_INCOMPATIBLE_CARRIER: ClassVar[int]
    ERROR_INSTALL_PROFILE: ClassVar[int]
    ERROR_INVALID_ACTIVATION_CODE: ClassVar[int]
    ERROR_INVALID_CONFIRMATION_CODE: ClassVar[int]
    ERROR_INVALID_PORT: ClassVar[int]
    ERROR_INVALID_RESPONSE: ClassVar[int]
    ERROR_NO_PROFILES_AVAILABLE: ClassVar[int]
    ERROR_OPERATION_BUSY: ClassVar[int]
    ERROR_SIM_MISSING: ClassVar[int]
    ERROR_TIME_OUT: ClassVar[int]
    ERROR_UNSUPPORTED_VERSION: ClassVar[int]
    EUICC_MEMORY_FIELD_UNAVAILABLE: ClassVar[int]
    EXTRA_EMBEDDED_SUBSCRIPTION_DETAILED_CODE: ClassVar[str]
    EXTRA_EMBEDDED_SUBSCRIPTION_DOWNLOADABLE_SUBSCRIPTION: ClassVar[str]
    EXTRA_EMBEDDED_SUBSCRIPTION_ERROR_CODE: ClassVar[str]
    EXTRA_EMBEDDED_SUBSCRIPTION_OPERATION_CODE: ClassVar[str]
    EXTRA_EMBEDDED_SUBSCRIPTION_SMDX_REASON_CODE: ClassVar[str]
    EXTRA_EMBEDDED_SUBSCRIPTION_SMDX_SUBJECT_CODE: ClassVar[str]
    EXTRA_USE_QR_SCANNER: ClassVar[str]
    META_DATA_CARRIER_ICON: ClassVar[str]
    OPERATION_APDU: ClassVar[int]
    OPERATION_DOWNLOAD: ClassVar[int]
    OPERATION_EUICC_CARD: ClassVar[int]
    OPERATION_EUICC_GSMA: ClassVar[int]
    OPERATION_HTTP: ClassVar[int]
    OPERATION_METADATA: ClassVar[int]
    OPERATION_SIM_SLOT: ClassVar[int]
    OPERATION_SMDX: ClassVar[int]
    OPERATION_SMDX_SUBJECT_REASON_CODE: ClassVar[int]
    OPERATION_SWITCH: ClassVar[int]
    OPERATION_SYSTEM: ClassVar[int]
    def createForCardId(self, arg0: int) -> "EuiccManager": ...
    def isEnabled(self) -> bool: ...
    def getEid(self) -> str: ...
    def getAvailableMemoryInBytes(self) -> int: ...
    def downloadSubscription(self, arg0: DownloadableSubscription, arg1: bool, arg2: PendingIntent) -> None: ...
    def startResolutionActivity(self, arg0: Activity, arg1: int, arg2: Intent, arg3: PendingIntent) -> None: ...
    def getEuiccInfo(self) -> EuiccInfo: ...
    def deleteSubscription(self, arg0: int, arg1: PendingIntent) -> None: ...
    @overload
    def switchToSubscription(self, arg0: int, arg1: PendingIntent) -> None: ...
    @overload
    def switchToSubscription(self, arg0: int, arg1: int, arg2: PendingIntent) -> None: ...
    def updateSubscriptionNickname(self, arg0: int, arg1: str, arg2: PendingIntent) -> None: ...
    def isSimPortAvailable(self, arg0: int) -> bool: ...
