from typing import Any, ClassVar, overload
from java.io.InputStream import InputStream
from java.net.Authenticator import Authenticator
from java.security.Permission import Permission

class HttpURLConnection:
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
    def disconnect(self) -> None: ...
    def setAuthenticator(self, p0: Authenticator) -> None: ...
    @overload
    def setFixedLengthStreamingMode(self, p0: int) -> None: ...
    @overload
    def setFixedLengthStreamingMode(self, p0: int) -> None: ...
    def setChunkedStreamingMode(self, p0: int) -> None: ...
    @staticmethod
    def setFollowRedirects(p0: bool) -> None: ...
    @staticmethod
    def getFollowRedirects() -> bool: ...
    def setInstanceFollowRedirects(self, p0: bool) -> None: ...
    def getInstanceFollowRedirects(self) -> bool: ...
    def getRequestMethod(self) -> str: ...
    def getResponseMessage(self) -> str: ...
    def usingProxy(self) -> bool: ...
    def getErrorStream(self) -> InputStream: ...
    def getHeaderField(self, p0: int) -> str: ...
    def getHeaderFieldDate(self, p0: str, p1: int) -> int: ...
    def getHeaderFieldKey(self, p0: int) -> str: ...
    def getPermission(self) -> Permission: ...
    def setRequestMethod(self, p0: str) -> None: ...
    def getResponseCode(self) -> int: ...
