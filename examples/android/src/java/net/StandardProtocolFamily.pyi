from typing import Any, ClassVar, overload

class StandardProtocolFamily:
    INET: ClassVar["StandardProtocolFamily"]
    INET6: ClassVar["StandardProtocolFamily"]
    UNIX: ClassVar["StandardProtocolFamily"]
    @staticmethod
    def values() -> list["StandardProtocolFamily"]: ...
    @staticmethod
    def valueOf(arg0: str) -> "StandardProtocolFamily": ...
