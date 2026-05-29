from typing import Any, ClassVar, overload

class SocketException:
    @overload
    def __init__(self, arg0: str) -> None: ...
    @overload
    def __init__(self) -> None: ...
