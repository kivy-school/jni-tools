from typing import Any, ClassVar, overload
from javax.net.ssl.SSLSession import SSLSession

class HostnameVerifier:
    def verify(self, p0: str, p1: SSLSession) -> bool: ...
