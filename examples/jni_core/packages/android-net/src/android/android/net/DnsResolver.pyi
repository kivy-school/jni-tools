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
    def query(self, p0: Network, p1: str, p2: int, p3: int, p4: Executor, p5: CancellationSignal, p6: Any) -> None: ...
    @overload
    def query(self, p0: Network, p1: str, p2: int, p3: Executor, p4: CancellationSignal, p5: Any) -> None: ...
    @overload
    def rawQuery(self, p0: Network, p1: Any, p2: int, p3: Executor, p4: CancellationSignal, p5: Any) -> None: ...
    @overload
    def rawQuery(self, p0: Network, p1: str, p2: int, p3: int, p4: int, p5: Executor, p6: CancellationSignal, p7: Any) -> None: ...

    class DnsException:
        code: int
        def __init__(self, p0: int, p1: Throwable) -> None: ...

    class Callback:
        def onAnswer(self, p0: Any, p1: int) -> None: ...
        def onError(self, p0: Any) -> None: ...
