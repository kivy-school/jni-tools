from typing import Any, ClassVar, overload
from org.w3c.dom.Node import Node

class UserDataHandler:
    NODE_ADOPTED: ClassVar[int]
    NODE_CLONED: ClassVar[int]
    NODE_DELETED: ClassVar[int]
    NODE_IMPORTED: ClassVar[int]
    NODE_RENAMED: ClassVar[int]
    def handle(self, arg0: int, arg1: str, arg2: Any, arg3: Node, arg4: Node) -> None: ...
