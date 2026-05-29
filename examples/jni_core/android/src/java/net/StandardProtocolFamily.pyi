from typing import Any, ClassVar, overload

class StandardProtocolFamily:
    INET: ClassVar["StandardProtocolFamily"]
    INET6: ClassVar["StandardProtocolFamily"]
    UNIX: ClassVar["StandardProtocolFamily"]
    INET: ClassVar["StandardProtocolFamily"]
    INET6: ClassVar["StandardProtocolFamily"]
    UNIX: ClassVar["StandardProtocolFamily"]
    @staticmethod
    def values() -> Any: ...
    @staticmethod
    def valueOf(p0: str) -> "StandardProtocolFamily": ...
