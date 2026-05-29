from typing import Any, ClassVar, overload
from java.util.SequencedCollection import SequencedCollection

class SequencedSet:
    @overload
    def reversed(self) -> "SequencedSet": ...
    @overload
    def reversed(self) -> SequencedCollection: ...
