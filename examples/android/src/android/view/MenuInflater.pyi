from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.view.Menu import Menu

class MenuInflater:
    def __init__(self, arg0: Context) -> None: ...
    def inflate(self, arg0: int, arg1: Menu) -> None: ...
