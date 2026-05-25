from typing import Any, ClassVar, overload

class StructUtsname:
    machine: str
    nodename: str
    release: str
    sysname: str
    version: str
    def __init__(self, arg0: str, arg1: str, arg2: str, arg3: str, arg4: str) -> None: ...
    def toString(self) -> str: ...
