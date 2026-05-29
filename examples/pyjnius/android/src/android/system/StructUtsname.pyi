from typing import Any, ClassVar, overload

class StructUtsname:
    machine: str
    nodename: str
    release: str
    sysname: str
    version: str
    def __init__(self, p0: str, p1: str, p2: str, p3: str, p4: str) -> None: ...
    def toString(self) -> str: ...
