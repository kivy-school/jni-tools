from typing import Any, ClassVar, overload
from java.io.InputStream import InputStream
from java.net.URL import URL
from java.security.Permission import Permission

class HttpURLConnection:
    HTTP_ACCEPTED: ClassVar[int]
    HTTP_BAD_GATEWAY: ClassVar[int]
    HTTP_BAD_METHOD: ClassVar[int]
    HTTP_BAD_REQUEST: ClassVar[int]
    HTTP_CLIENT_TIMEOUT: ClassVar[int]
    HTTP_CONFLICT: ClassVar[int]
    HTTP_CREATED: ClassVar[int]
    HTTP_ENTITY_TOO_LARGE: ClassVar[int]
    HTTP_FORBIDDEN: ClassVar[int]
    HTTP_GATEWAY_TIMEOUT: ClassVar[int]
    HTTP_GONE: ClassVar[int]
    HTTP_INTERNAL_ERROR: ClassVar[int]
    HTTP_LENGTH_REQUIRED: ClassVar[int]
    HTTP_MOVED_PERM: ClassVar[int]
    HTTP_MOVED_TEMP: ClassVar[int]
    HTTP_MULT_CHOICE: ClassVar[int]
    HTTP_NOT_ACCEPTABLE: ClassVar[int]
    HTTP_NOT_AUTHORITATIVE: ClassVar[int]
    HTTP_NOT_FOUND: ClassVar[int]
    HTTP_NOT_IMPLEMENTED: ClassVar[int]
    HTTP_NOT_MODIFIED: ClassVar[int]
    HTTP_NO_CONTENT: ClassVar[int]
    HTTP_OK: ClassVar[int]
    HTTP_PARTIAL: ClassVar[int]
    HTTP_PAYMENT_REQUIRED: ClassVar[int]
    HTTP_PRECON_FAILED: ClassVar[int]
    HTTP_PROXY_AUTH: ClassVar[int]
    HTTP_REQ_TOO_LONG: ClassVar[int]
    HTTP_RESET: ClassVar[int]
    HTTP_SEE_OTHER: ClassVar[int]
    HTTP_SERVER_ERROR: ClassVar[int]
    HTTP_UNAUTHORIZED: ClassVar[int]
    HTTP_UNAVAILABLE: ClassVar[int]
    HTTP_UNSUPPORTED_TYPE: ClassVar[int]
    HTTP_USE_PROXY: ClassVar[int]
    HTTP_VERSION: ClassVar[int]
    chunkLength: int
    fixedContentLength: int
    fixedContentLengthLong: int
    instanceFollowRedirects: bool
    method: str
    responseCode: int
    responseMessage: str
    def __init__(self, arg0: URL) -> None: ...
    def getHeaderFieldKey(self, arg0: int) -> str: ...
    @overload
    def setFixedLengthStreamingMode(self, arg0: int) -> None: ...
    @overload
    def setFixedLengthStreamingMode(self, arg0: int) -> None: ...
    def setChunkedStreamingMode(self, arg0: int) -> None: ...
    def getHeaderField(self, arg0: int) -> str: ...
    @staticmethod
    def setFollowRedirects(arg0: bool) -> None: ...
    @staticmethod
    def getFollowRedirects() -> bool: ...
    def setInstanceFollowRedirects(self, arg0: bool) -> None: ...
    def getInstanceFollowRedirects(self) -> bool: ...
    def setRequestMethod(self, arg0: str) -> None: ...
    def getRequestMethod(self) -> str: ...
    def getResponseCode(self) -> int: ...
    def getResponseMessage(self) -> str: ...
    def getHeaderFieldDate(self, arg0: str, arg1: int) -> int: ...
    def disconnect(self) -> None: ...
    def usingProxy(self) -> bool: ...
    def getPermission(self) -> Permission: ...
    def getErrorStream(self) -> InputStream: ...
