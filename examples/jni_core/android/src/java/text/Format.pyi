from typing import Any, ClassVar, overload
from java.lang.StringBuffer import StringBuffer
from java.text.AttributedCharacterIterator import AttributedCharacterIterator
from java.text.FieldPosition import FieldPosition
from java.text.ParsePosition import ParsePosition

class Format:
    @overload
    def parseObject(self, p0: str, p1: ParsePosition) -> Any: ...
    @overload
    def parseObject(self, p0: str) -> Any: ...
    def formatToCharacterIterator(self, p0: Any) -> AttributedCharacterIterator: ...
    def clone(self) -> Any: ...
    @overload
    def format(self, p0: Any) -> str: ...
    @overload
    def format(self, p0: Any, p1: StringBuffer, p2: FieldPosition) -> StringBuffer: ...

    class Field:
        LANGUAGE: ClassVar[Any]
        READING: ClassVar[Any]
        INPUT_METHOD_SEGMENT: ClassVar[Any]
