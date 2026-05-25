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
    sPhoneNumberMatchFilter: ClassVar["MatchFilter"]
    sPhoneNumberTransformFilter: ClassVar["TransformFilter"]
    sUrlMatchFilter: ClassVar["MatchFilter"]
    def __init__(self) -> None: ...
    @overload
    @staticmethod
    def addLinks(arg0: Spannable, arg1: int) -> bool: ...
    @overload
    @staticmethod
    def addLinks(arg0: Spannable, arg1: int, arg2: Function) -> bool: ...
    @overload
    @staticmethod
    def addLinks(arg0: TextView, arg1: int) -> bool: ...
    @overload
    @staticmethod
    def addLinks(arg0: TextView, arg1: Pattern, arg2: str) -> None: ...
    @overload
    @staticmethod
    def addLinks(arg0: TextView, arg1: Pattern, arg2: str, arg3: "MatchFilter", arg4: "TransformFilter") -> None: ...
    @overload
    @staticmethod
    def addLinks(arg0: TextView, arg1: Pattern, arg2: str, arg3: list[str], arg4: "MatchFilter", arg5: "TransformFilter") -> None: ...
    @overload
    @staticmethod
    def addLinks(arg0: Spannable, arg1: Pattern, arg2: str) -> bool: ...
    @overload
    @staticmethod
    def addLinks(arg0: Spannable, arg1: Pattern, arg2: str, arg3: "MatchFilter", arg4: "TransformFilter") -> bool: ...
    @overload
    @staticmethod
    def addLinks(arg0: Spannable, arg1: Pattern, arg2: str, arg3: list[str], arg4: "MatchFilter", arg5: "TransformFilter") -> bool: ...
    @overload
    @staticmethod
    def addLinks(arg0: Spannable, arg1: Pattern, arg2: str, arg3: list[str], arg4: "MatchFilter", arg5: "TransformFilter", arg6: Function) -> bool: ...

    class MatchFilter:
        def acceptMatch(self, arg0: str, arg1: int, arg2: int) -> bool: ...

    class TransformFilter:
        def transformUrl(self, arg0: Matcher, arg1: str) -> str: ...
