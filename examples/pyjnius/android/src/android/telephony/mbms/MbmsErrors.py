from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MbmsErrors"]

class MbmsErrors(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/mbms/MbmsErrors"
    ERROR_MIDDLEWARE_LOST = JavaStaticField("I")
    ERROR_MIDDLEWARE_NOT_BOUND = JavaStaticField("I")
    ERROR_NO_UNIQUE_MIDDLEWARE = JavaStaticField("I")
    SUCCESS = JavaStaticField("I")
    UNKNOWN = JavaStaticField("I")

    class StreamingErrors(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/mbms/MbmsErrors$StreamingErrors"
        ERROR_CONCURRENT_SERVICE_LIMIT_REACHED = JavaStaticField("I")
        ERROR_DUPLICATE_START_STREAM = JavaStaticField("I")
        ERROR_UNABLE_TO_START_SERVICE = JavaStaticField("I")

    class InitializationErrors(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/mbms/MbmsErrors$InitializationErrors"
        ERROR_APP_PERMISSIONS_NOT_GRANTED = JavaStaticField("I")
        ERROR_DUPLICATE_INITIALIZE = JavaStaticField("I")
        ERROR_UNABLE_TO_INITIALIZE = JavaStaticField("I")

    class GroupCallErrors(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/mbms/MbmsErrors$GroupCallErrors"
        ERROR_DUPLICATE_START_GROUP_CALL = JavaStaticField("I")
        ERROR_UNABLE_TO_START_SERVICE = JavaStaticField("I")

    class GeneralErrors(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/mbms/MbmsErrors$GeneralErrors"
        ERROR_CARRIER_CHANGE_NOT_ALLOWED = JavaStaticField("I")
        ERROR_IN_E911 = JavaStaticField("I")
        ERROR_MIDDLEWARE_NOT_YET_READY = JavaStaticField("I")
        ERROR_MIDDLEWARE_TEMPORARILY_UNAVAILABLE = JavaStaticField("I")
        ERROR_NOT_CONNECTED_TO_HOME_CARRIER_LTE = JavaStaticField("I")
        ERROR_OUT_OF_MEMORY = JavaStaticField("I")
        ERROR_UNABLE_TO_READ_SIM = JavaStaticField("I")

    class DownloadErrors(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/mbms/MbmsErrors$DownloadErrors"
        ERROR_CANNOT_CHANGE_TEMP_FILE_ROOT = JavaStaticField("I")
        ERROR_MALFORMED_SERVICE_ANNOUNCEMENT = JavaStaticField("I")
        ERROR_UNKNOWN_DOWNLOAD_REQUEST = JavaStaticField("I")
        ERROR_UNKNOWN_FILE_INFO = JavaStaticField("I")