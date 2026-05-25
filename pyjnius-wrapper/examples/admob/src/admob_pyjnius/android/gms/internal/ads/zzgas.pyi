from typing import Any, ClassVar, overload
from android.gms.internal.ads.zzgai import zzgai
from android.net.Network import Network

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class URL:
    """Forward declaration for ``java.net.URL``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.net.URL')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/net/URL.html
    """
    ...
class URLConnection:
    """Forward declaration for ``java.net.URLConnection``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.net.URLConnection')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/net/URLConnection.html
    """
    ...
class HttpURLConnection:
    """Forward declaration for ``java.net.HttpURLConnection``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.net.HttpURLConnection')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/net/HttpURLConnection.html
    """
    ...

class zzgas:
    def zzf(self, arg0: URL, arg1: int) -> URLConnection: ...
    def zzg(self, arg0: Network, arg1: URL, arg2: int, arg3: int) -> HttpURLConnection: ...
    def zzh(self, arg0: zzgai, arg1: int, arg2: int) -> HttpURLConnection: ...
    @staticmethod
    def zzi(arg0: HttpURLConnection) -> None: ...
    def zzj(self) -> HttpURLConnection: ...
    def close(self) -> None: ...
