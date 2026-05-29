from typing import Any, ClassVar, overload
from org.w3c.dom.Node import Node

class UserDataHandler:
    NODE_CLONED: ClassVar[int]
    NODE_IMPORTED: ClassVar[int]
    NODE_DELETED: ClassVar[int]
    NODE_RENAMED: ClassVar[int]
    NODE_ADOPTED: ClassVar[int]
    def handle(self, p0: int, p1: str, p2: Any, p3: Node, p4: Node) -> None: ...
