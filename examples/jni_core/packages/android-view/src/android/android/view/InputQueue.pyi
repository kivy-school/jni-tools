from typing import Any, ClassVar, overload

class InputQueue:

    class Callback:
        def onInputQueueDestroyed(self, p0: "InputQueue") -> None: ...
        def onInputQueueCreated(self, p0: "InputQueue") -> None: ...
