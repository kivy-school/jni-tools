from typing import Any, ClassVar, overload
from java.security.Principal import Principal
from java.util.Optional import Optional
from javax.net.ssl.HostnameVerifier import HostnameVerifier
from javax.net.ssl.SSLSocketFactory import SSLSocketFactory

class HttpsURLConnection:
    HTTP_OK: ClassVar[int]
    HTTP_CREATED: ClassVar[int]
    HTTP_ACCEPTED: ClassVar[int]
    HTTP_NOT_AUTHORITATIVE: ClassVar[int]
    HTTP_NO_CONTENT: ClassVar[int]
    HTTP_RESET: ClassVar[int]
    HTTP_PARTIAL: ClassVar[int]
    HTTP_MULT_CHOICE: ClassVar[int]
    HTTP_MOVED_PERM: ClassVar[int]
    HTTP_MOVED_TEMP: ClassVar[int]
    HTTP_SEE_OTHER: ClassVar[int]
    HTTP_NOT_MODIFIED: ClassVar[int]
    HTTP_USE_PROXY: ClassVar[int]
    HTTP_BAD_REQUEST: ClassVar[int]
    HTTP_UNAUTHORIZED: ClassVar[int]
    HTTP_PAYMENT_REQUIRED: ClassVar[int]
    HTTP_FORBIDDEN: ClassVar[int]
    HTTP_NOT_FOUND: ClassVar[int]
    HTTP_BAD_METHOD: ClassVar[int]
    HTTP_NOT_ACCEPTABLE: ClassVar[int]
    HTTP_PROXY_AUTH: ClassVar[int]
    HTTP_CLIENT_TIMEOUT: ClassVar[int]
    HTTP_CONFLICT: ClassVar[int]
    HTTP_GONE: ClassVar[int]
    HTTP_LENGTH_REQUIRED: ClassVar[int]
    HTTP_PRECON_FAILED: ClassVar[int]
    HTTP_ENTITY_TOO_LARGE: ClassVar[int]
    HTTP_REQ_TOO_LONG: ClassVar[int]
    HTTP_UNSUPPORTED_TYPE: ClassVar[int]
    HTTP_SERVER_ERROR: ClassVar[int]
    HTTP_INTERNAL_ERROR: ClassVar[int]
    HTTP_NOT_IMPLEMENTED: ClassVar[int]
    HTTP_BAD_GATEWAY: ClassVar[int]
    HTTP_UNAVAILABLE: ClassVar[int]
    HTTP_GATEWAY_TIMEOUT: ClassVar[int]
    HTTP_VERSION: ClassVar[int]
    def getCipherSuite(self) -> str: ...
    @staticmethod
    def getDefaultSSLSocketFactory() -> SSLSocketFactory: ...
    def getServerCertificates(self) -> Any: ...
    def setHostnameVerifier(self, p0: HostnameVerifier) -> None: ...
    @staticmethod
    def setDefaultHostnameVerifier(p0: HostnameVerifier) -> None: ...
    @staticmethod
    def getDefaultHostnameVerifier() -> HostnameVerifier: ...
    def getHostnameVerifier(self) -> HostnameVerifier: ...
    @staticmethod
    def setDefaultSSLSocketFactory(p0: SSLSocketFactory) -> None: ...
    def setSSLSocketFactory(self, p0: SSLSocketFactory) -> None: ...
    def getSSLSocketFactory(self) -> SSLSocketFactory: ...
    def getPeerPrincipal(self) -> Principal: ...
    def getLocalPrincipal(self) -> Principal: ...
    def getSSLSession(self) -> Optional: ...
    def getLocalCertificates(self) -> Any: ...
