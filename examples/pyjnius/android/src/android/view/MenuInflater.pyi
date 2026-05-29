from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.view.Menu import Menu

class MenuInflater:
    def __init__(self, p0: Context) -> None: ...
    def inflate(self, p0: int, p1: Menu) -> None: ...
