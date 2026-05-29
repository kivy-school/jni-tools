from typing import Any, ClassVar, overload
from android.text.Spannable import Spannable
from android.widget.TextView import TextView
from java.util.function.Function import Function
from java.util.regex.Matcher import Matcher
from java.util.regex.Pattern import Pattern

class Linkify:
    ALL: ClassVar[int]
    EMAIL_ADDRESSES: ClassVar[int]
    MAP_ADDRESSES: ClassVar[int]
    PHONE_NUMBERS: ClassVar[int]
    WEB_URLS: ClassVar[int]
    sPhoneNumberMatchFilter: ClassVar[Any]
    sPhoneNumberTransformFilter: ClassVar[Any]
    sUrlMatchFilter: ClassVar[Any]
    def __init__(self) -> None: ...
    @overload
    @staticmethod
    def addLinks(p0: TextView, p1: int) -> bool: ...
    @overload
    @staticmethod
    def addLinks(p0: TextView, p1: Pattern, p2: str) -> None: ...
    @overload
    @staticmethod
    def addLinks(p0: TextView, p1: Pattern, p2: str, p3: Any, p4: Any) -> None: ...
    @overload
    @staticmethod
    def addLinks(p0: TextView, p1: Pattern, p2: str, p3: Any, p4: Any, p5: Any) -> None: ...
    @overload
    @staticmethod
    def addLinks(p0: Spannable, p1: Pattern, p2: str, p3: Any, p4: Any, p5: Any, p6: Function) -> bool: ...
    @overload
    @staticmethod
    def addLinks(p0: Spannable, p1: int, p2: Function) -> bool: ...
    @overload
    @staticmethod
    def addLinks(p0: Spannable, p1: Pattern, p2: str) -> bool: ...
    @overload
    @staticmethod
    def addLinks(p0: Spannable, p1: Pattern, p2: str, p3: Any, p4: Any) -> bool: ...
    @overload
    @staticmethod
    def addLinks(p0: Spannable, p1: Pattern, p2: str, p3: Any, p4: Any, p5: Any) -> bool: ...
    @overload
    @staticmethod
    def addLinks(p0: Spannable, p1: int) -> bool: ...

    class MatchFilter:
        def acceptMatch(self, p0: str, p1: int, p2: int) -> bool: ...

    class TransformFilter:
        def transformUrl(self, p0: Matcher, p1: str) -> str: ...
