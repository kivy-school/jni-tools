from typing import Any, ClassVar, overload
from java.security.cert.X509Certificate import X509Certificate
from javax.net.ssl.SSLSession import SSLSession
from javax.net.ssl.SSLSocket import SSLSocket

class X509HostnameVerifier:
    @overload
    def verify(self, arg0: str, arg1: SSLSession) -> bool: ...
    @overload
    def verify(self, arg0: str, arg1: SSLSocket) -> None: ...
    @overload
    def verify(self, arg0: str, arg1: X509Certificate) -> None: ...
    @overload
    def verify(self, arg0: str, arg1: list[str], arg2: list[str]) -> None: ...
