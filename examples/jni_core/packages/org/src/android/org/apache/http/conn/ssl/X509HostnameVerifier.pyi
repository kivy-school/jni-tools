from typing import Any, ClassVar, overload
from java.security.cert.X509Certificate import X509Certificate
from javax.net.ssl.SSLSession import SSLSession
from javax.net.ssl.SSLSocket import SSLSocket

class X509HostnameVerifier:
    @overload
    def verify(self, p0: str, p1: SSLSocket) -> None: ...
    @overload
    def verify(self, p0: str, p1: SSLSession) -> bool: ...
    @overload
    def verify(self, p0: str, p1: X509Certificate) -> None: ...
    @overload
    def verify(self, p0: str, p1: Any, p2: Any) -> None: ...
