from typing import Any, ClassVar, overload
from android.net.Network import Network
from android.os.CancellationSignal import CancellationSignal
from java.lang.Throwable import Throwable
from java.util.concurrent.Executor import Executor

class DnsResolver:
    CLASS_IN: ClassVar[int]
    ERROR_PARSE: ClassVar[int]
    ERROR_SYSTEM: ClassVar[int]
    FLAG_EMPTY: ClassVar[int]
    FLAG_NO_CACHE_LOOKUP: ClassVar[int]
    FLAG_NO_CACHE_STORE: ClassVar[int]
    FLAG_NO_RETRY: ClassVar[int]
    TYPE_A: ClassVar[int]
    TYPE_AAAA: ClassVar[int]
    @staticmethod
    def getInstance() -> "DnsResolver": ...
    @overload
    def rawQuery(self, arg0: Network, arg1: list[int], arg2: int, arg3: Executor, arg4: CancellationSignal, arg5: "Callback") -> None: ...
    @overload
    def rawQuery(self, arg0: Network, arg1: str, arg2: int, arg3: int, arg4: int, arg5: Executor, arg6: CancellationSignal, arg7: "Callback") -> None: ...
    @overload
    def query(self, arg0: Network, arg1: str, arg2: int, arg3: Executor, arg4: CancellationSignal, arg5: "Callback") -> None: ...
    @overload
    def query(self, arg0: Network, arg1: str, arg2: int, arg3: int, arg4: Executor, arg5: CancellationSignal, arg6: "Callback") -> None: ...

    class Callback:
        def onAnswer(self, arg0: Any, arg1: int) -> None: ...
        def onError(self, arg0: "DnsException") -> None: ...

    class DnsException:
        code: int
        def __init__(self, arg0: int, arg1: Throwable) -> None: ...
