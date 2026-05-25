from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.net.IpSecAlgorithm import IpSecAlgorithm
from android.os.OutcomeReceiver import OutcomeReceiver
from java.net.InetAddress import InetAddress
from java.util.concurrent.Executor import Executor

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class UdpEncapsulationSocket:
    """Forward declaration for ``android.net.IpSecManager.UdpEncapsulationSocket``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.net.IpSecManager.UdpEncapsulationSocket')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/net/IpSecManager/UdpEncapsulationSocket
    """
    ...
class SecurityParameterIndex:
    """Forward declaration for ``android.net.IpSecManager.SecurityParameterIndex``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.net.IpSecManager.SecurityParameterIndex')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/net/IpSecManager/SecurityParameterIndex
    """
    ...

class IpSecTransform:
    def equals(self, arg0: Any) -> bool: ...
    def close(self) -> None: ...
    def finalize(self) -> None: ...
    def requestIpSecTransformState(self, arg0: Executor, arg1: OutcomeReceiver) -> None: ...
    def toString(self) -> str: ...

    class Builder:
        def __init__(self, arg0: Context) -> None: ...
        def setEncryption(self, arg0: IpSecAlgorithm) -> "Builder": ...
        def setAuthentication(self, arg0: IpSecAlgorithm) -> "Builder": ...
        def setAuthenticatedEncryption(self, arg0: IpSecAlgorithm) -> "Builder": ...
        def setIpv4Encapsulation(self, arg0: UdpEncapsulationSocket, arg1: int) -> "Builder": ...
        def buildTransportModeTransform(self, arg0: InetAddress, arg1: SecurityParameterIndex) -> "IpSecTransform": ...
