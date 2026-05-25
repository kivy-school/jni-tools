from typing import Any, ClassVar, overload

class DriverPropertyInfo:
    choices: list[str]
    description: str
    name: str
    required: bool
    value: str
    def __init__(self, arg0: str, arg1: str) -> None: ...
