from typing import Any, ClassVar, overload

class PorterDuff:
    def __init__(self) -> None: ...

    class Mode:
        CLEAR: ClassVar["Mode"]
        SRC: ClassVar["Mode"]
        DST: ClassVar["Mode"]
        SRC_OVER: ClassVar["Mode"]
        DST_OVER: ClassVar["Mode"]
        SRC_IN: ClassVar["Mode"]
        DST_IN: ClassVar["Mode"]
        SRC_OUT: ClassVar["Mode"]
        DST_OUT: ClassVar["Mode"]
        SRC_ATOP: ClassVar["Mode"]
        DST_ATOP: ClassVar["Mode"]
        XOR: ClassVar["Mode"]
        DARKEN: ClassVar["Mode"]
        LIGHTEN: ClassVar["Mode"]
        MULTIPLY: ClassVar["Mode"]
        SCREEN: ClassVar["Mode"]
        ADD: ClassVar["Mode"]
        OVERLAY: ClassVar["Mode"]
        CLEAR: ClassVar[Any]
        SRC: ClassVar[Any]
        DST: ClassVar[Any]
        SRC_OVER: ClassVar[Any]
        DST_OVER: ClassVar[Any]
        SRC_IN: ClassVar[Any]
        DST_IN: ClassVar[Any]
        SRC_OUT: ClassVar[Any]
        DST_OUT: ClassVar[Any]
        SRC_ATOP: ClassVar[Any]
        DST_ATOP: ClassVar[Any]
        XOR: ClassVar[Any]
        DARKEN: ClassVar[Any]
        LIGHTEN: ClassVar[Any]
        MULTIPLY: ClassVar[Any]
        SCREEN: ClassVar[Any]
        ADD: ClassVar[Any]
        OVERLAY: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...
