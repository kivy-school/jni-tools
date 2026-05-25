from typing import Any, ClassVar, overload
from java.util.Iterator import Iterator

class DirectoryStream:
    def iterator(self) -> Iterator: ...

    class Filter:
        def accept(self, arg0: Any) -> bool: ...
