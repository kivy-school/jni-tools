from typing import Any, ClassVar, overload

class InputQueue:

    class Callback:
        def onInputQueueCreated(self, p0: "InputQueue") -> None: ...
        def onInputQueueDestroyed(self, p0: "InputQueue") -> None: ...
