from typing import Any, ClassVar, overload
from javax.net.ssl.SSLSession import SSLSession

class HostnameVerifier:
    def verify(self, arg0: str, arg1: SSLSession) -> bool: ...
