from typing import Any, ClassVar, overload

class InterruptibleChannel:
    def close(self) -> None: ...
