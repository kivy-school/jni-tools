from typing import Any, ClassVar, overload
from javax.security.auth.callback.Callback import Callback

class CallbackHandler:
    def handle(self, arg0: list[Callback]) -> None: ...
