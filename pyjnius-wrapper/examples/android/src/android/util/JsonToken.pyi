from typing import Any, ClassVar, overload

class JsonToken:
    BEGIN_ARRAY: ClassVar["JsonToken"]
    END_ARRAY: ClassVar["JsonToken"]
    BEGIN_OBJECT: ClassVar["JsonToken"]
    END_OBJECT: ClassVar["JsonToken"]
    NAME: ClassVar["JsonToken"]
    STRING: ClassVar["JsonToken"]
    NUMBER: ClassVar["JsonToken"]
    BOOLEAN: ClassVar["JsonToken"]
    NULL: ClassVar["JsonToken"]
    END_DOCUMENT: ClassVar["JsonToken"]
    @staticmethod
    def values() -> list["JsonToken"]: ...
    @staticmethod
    def valueOf(arg0: str) -> "JsonToken": ...
