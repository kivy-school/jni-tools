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
    @staticmethod
    def getDefaultSmsSubscriptionId() -> int: ...
    def createForSubscriptionId(self, p0: int) -> "SmsManager": ...
    @overload
    def sendTextMessage(self, p0: str, p1: str, p2: str, p3: PendingIntent, p4: PendingIntent, p5: int) -> None: ...
    @overload
    def sendTextMessage(self, p0: str, p1: str, p2: str, p3: PendingIntent, p4: PendingIntent) -> None: ...
    def divideMessage(self, p0: str) -> list: ...
    @overload
    def sendMultipartTextMessage(self, p0: str, p1: str, p2: list, p3: list, p4: list, p5: int) -> None: ...
    @overload
    def sendMultipartTextMessage(self, p0: str, p1: str, p2: list, p3: list, p4: list) -> None: ...
    @overload
    def sendMultipartTextMessage(self, p0: str, p1: str, p2: list, p3: list, p4: list, p5: str, p6: str) -> None: ...
    def sendDataMessage(self, p0: str, p1: str, p2: int, p3: Any, p4: PendingIntent, p5: PendingIntent) -> None: ...
    def injectSmsPdu(self, p0: Any, p1: str, p2: PendingIntent) -> None: ...
    def sendTextMessageWithoutPersisting(self, p0: str, p1: str, p2: str, p3: PendingIntent, p4: PendingIntent) -> None: ...
    @staticmethod
    def getSmsManagerForSubscriptionId(p0: int) -> "SmsManager": ...
    def getSmsCapacityOnIcc(self) -> int: ...
    @overload
    def sendMultimediaMessage(self, p0: Context, p1: Uri, p2: str, p3: Bundle, p4: PendingIntent) -> None: ...
    @overload
    def sendMultimediaMessage(self, p0: Context, p1: Uri, p2: str, p3: Bundle, p4: PendingIntent, p5: int) -> None: ...
    @overload
    def downloadMultimediaMessage(self, p0: Context, p1: str, p2: Uri, p3: Bundle, p4: PendingIntent) -> None: ...
    @overload
    def downloadMultimediaMessage(self, p0: Context, p1: str, p2: Uri, p3: Bundle, p4: PendingIntent, p5: int) -> None: ...
    def getCarrierConfigValues(self) -> Bundle: ...
    def createAppSpecificSmsToken(self, p0: PendingIntent) -> str: ...
    def getSmsMessagesForFinancialApp(self, p0: Bundle, p1: Executor, p2: Any) -> None: ...
    def createAppSpecificSmsTokenWithPackageInfo(self, p0: str, p1: PendingIntent) -> str: ...
    def getSmscAddress(self) -> str: ...
    def setSmscAddress(self, p0: str) -> bool: ...
    def getSubscriptionId(self) -> int: ...
    @staticmethod
    def getDefault() -> "SmsManager": ...

    class FinancialSmsCallback:
        def __init__(self) -> None: ...
        def onFinancialSmsMessages(self, p0: CursorWindow) -> None: ...
