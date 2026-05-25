from typing import Any, ClassVar, overload

class MbmsErrors:
    ERROR_MIDDLEWARE_LOST: ClassVar[int]
    ERROR_MIDDLEWARE_NOT_BOUND: ClassVar[int]
    ERROR_NO_UNIQUE_MIDDLEWARE: ClassVar[int]
    SUCCESS: ClassVar[int]
    UNKNOWN: ClassVar[int]

    class DownloadErrors:
        ERROR_CANNOT_CHANGE_TEMP_FILE_ROOT: ClassVar[int]
        ERROR_MALFORMED_SERVICE_ANNOUNCEMENT: ClassVar[int]
        ERROR_UNKNOWN_DOWNLOAD_REQUEST: ClassVar[int]
        ERROR_UNKNOWN_FILE_INFO: ClassVar[int]

    class GeneralErrors:
        ERROR_CARRIER_CHANGE_NOT_ALLOWED: ClassVar[int]
        ERROR_IN_E911: ClassVar[int]
        ERROR_MIDDLEWARE_NOT_YET_READY: ClassVar[int]
        ERROR_MIDDLEWARE_TEMPORARILY_UNAVAILABLE: ClassVar[int]
        ERROR_NOT_CONNECTED_TO_HOME_CARRIER_LTE: ClassVar[int]
        ERROR_OUT_OF_MEMORY: ClassVar[int]
        ERROR_UNABLE_TO_READ_SIM: ClassVar[int]

    class GroupCallErrors:
        ERROR_DUPLICATE_START_GROUP_CALL: ClassVar[int]
        ERROR_UNABLE_TO_START_SERVICE: ClassVar[int]

    class InitializationErrors:
        ERROR_APP_PERMISSIONS_NOT_GRANTED: ClassVar[int]
        ERROR_DUPLICATE_INITIALIZE: ClassVar[int]
        ERROR_UNABLE_TO_INITIALIZE: ClassVar[int]

    class StreamingErrors:
        ERROR_CONCURRENT_SERVICE_LIMIT_REACHED: ClassVar[int]
        ERROR_DUPLICATE_START_STREAM: ClassVar[int]
        ERROR_UNABLE_TO_START_SERVICE: ClassVar[int]
