from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.net.Uri import Uri
from java.util.Locale import Locale

class UserDictionary:
    AUTHORITY: ClassVar[str]
    CONTENT_URI: ClassVar[Uri]
    def __init__(self) -> None: ...

    class Words:
        APP_ID: ClassVar[str]
        CONTENT_ITEM_TYPE: ClassVar[str]
        CONTENT_TYPE: ClassVar[str]
        CONTENT_URI: ClassVar[Uri]
        DEFAULT_SORT_ORDER: ClassVar[str]
        FREQUENCY: ClassVar[str]
        LOCALE: ClassVar[str]
        LOCALE_TYPE_ALL: ClassVar[int]
        LOCALE_TYPE_CURRENT: ClassVar[int]
        SHORTCUT: ClassVar[str]
        WORD: ClassVar[str]
        _ID: ClassVar[str]
        def __init__(self) -> None: ...
        @overload
        @staticmethod
        def addWord(arg0: Context, arg1: str, arg2: int, arg3: int) -> None: ...
        @overload
        @staticmethod
        def addWord(arg0: Context, arg1: str, arg2: int, arg3: str, arg4: Locale) -> None: ...
