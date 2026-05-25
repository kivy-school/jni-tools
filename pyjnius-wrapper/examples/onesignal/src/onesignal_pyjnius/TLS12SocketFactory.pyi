from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class SSLSocketFactory:
    """Forward declaration for ``javax.net.ssl.SSLSocketFactory``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('javax.net.ssl.SSLSocketFactory')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/javax/net/ssl/SSLSocketFactory.html
    """
    ...
class Socket:
    """Forward declaration for ``java.net.Socket``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.net.Socket')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/net/Socket.html
    """
    ...
class InetAddress:
    """Forward declaration for ``java.net.InetAddress``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('java.net.InetAddress')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://docs.oracle.com/javase/8/docs/api/java/net/InetAddress.html
    """
    ...

class TLS12SocketFactory:
    def __init__(self, arg0: SSLSocketFactory) -> None: ...
    def getDefaultCipherSuites(self) -> list[str]: ...
    def getSupportedCipherSuites(self) -> list[str]: ...
    @overload
    def createSocket(self) -> Socket: ...
    @overload
    def createSocket(self, arg0: Socket, arg1: str, arg2: int, arg3: bool) -> Socket: ...
    @overload
    def createSocket(self, arg0: str, arg1: int) -> Socket: ...
    @overload
    def createSocket(self, arg0: str, arg1: int, arg2: InetAddress, arg3: int) -> Socket: ...
    @overload
    def createSocket(self, arg0: InetAddress, arg1: int) -> Socket: ...
    @overload
    def createSocket(self, arg0: InetAddress, arg1: int, arg2: InetAddress, arg3: int) -> Socket: ...
