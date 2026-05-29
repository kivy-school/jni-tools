from typing import Any, ClassVar, overload

class AutoCloseable:
    def close(self) -> None: ...
