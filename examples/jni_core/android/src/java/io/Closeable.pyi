from typing import Any, ClassVar, overload

class Closeable:
    def close(self) -> None: ...
