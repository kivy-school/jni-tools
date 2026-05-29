from typing import Any, ClassVar, overload

class JsonToken:
    BEGIN_ARRAY: ClassVar["JsonToken"]
    BEGIN_OBJECT: ClassVar["JsonToken"]
    BOOLEAN: ClassVar["JsonToken"]
    END_ARRAY: ClassVar["JsonToken"]
    END_DOCUMENT: ClassVar["JsonToken"]
    END_OBJECT: ClassVar["JsonToken"]
    NAME: ClassVar["JsonToken"]
    NULL: ClassVar["JsonToken"]
    NUMBER: ClassVar["JsonToken"]
    STRING: ClassVar["JsonToken"]
    BEGIN_ARRAY: ClassVar["JsonToken"]
    BEGIN_OBJECT: ClassVar["JsonToken"]
    BOOLEAN: ClassVar["JsonToken"]
    END_ARRAY: ClassVar["JsonToken"]
    END_DOCUMENT: ClassVar["JsonToken"]
    END_OBJECT: ClassVar["JsonToken"]
    NAME: ClassVar["JsonToken"]
    NULL: ClassVar["JsonToken"]
    NUMBER: ClassVar["JsonToken"]
    STRING: ClassVar["JsonToken"]
    @staticmethod
    def values() -> Any: ...
    @staticmethod
    def valueOf(p0: str) -> "JsonToken": ...
