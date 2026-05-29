from typing import Any, ClassVar, overload

class DriverPropertyInfo:
    name: str
    description: str
    required: bool
    value: str
    choices: Any
    def __init__(self, p0: str, p1: str) -> None: ...
