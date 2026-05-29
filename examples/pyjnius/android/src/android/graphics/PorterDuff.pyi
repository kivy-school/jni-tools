from typing import Any, ClassVar, overload

class PorterDuff:
    def __init__(self) -> None: ...

    class Mode:
        ADD: ClassVar["Mode"]
        CLEAR: ClassVar["Mode"]
        DARKEN: ClassVar["Mode"]
        DST: ClassVar["Mode"]
        DST_ATOP: ClassVar["Mode"]
        DST_IN: ClassVar["Mode"]
        DST_OUT: ClassVar["Mode"]
        DST_OVER: ClassVar["Mode"]
        LIGHTEN: ClassVar["Mode"]
        MULTIPLY: ClassVar["Mode"]
        OVERLAY: ClassVar["Mode"]
        SCREEN: ClassVar["Mode"]
        SRC: ClassVar["Mode"]
        SRC_ATOP: ClassVar["Mode"]
        SRC_IN: ClassVar["Mode"]
        SRC_OUT: ClassVar["Mode"]
        SRC_OVER: ClassVar["Mode"]
        XOR: ClassVar["Mode"]
        ADD: ClassVar[Any]
        CLEAR: ClassVar[Any]
        DARKEN: ClassVar[Any]
        DST: ClassVar[Any]
        DST_ATOP: ClassVar[Any]
        DST_IN: ClassVar[Any]
        DST_OUT: ClassVar[Any]
        DST_OVER: ClassVar[Any]
        LIGHTEN: ClassVar[Any]
        MULTIPLY: ClassVar[Any]
        OVERLAY: ClassVar[Any]
        SCREEN: ClassVar[Any]
        SRC: ClassVar[Any]
        SRC_ATOP: ClassVar[Any]
        SRC_IN: ClassVar[Any]
        SRC_OUT: ClassVar[Any]
        SRC_OVER: ClassVar[Any]
        XOR: ClassVar[Any]
        @staticmethod
        def values() -> Any: ...
        @staticmethod
        def valueOf(p0: str) -> Any: ...
