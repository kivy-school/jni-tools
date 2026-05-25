from typing import Any, ClassVar, overload
from android.graphics.drawable.Drawable import Drawable
from android.text.Editable import Editable
from android.text.Spanned import Spanned
from org.xml.sax.XMLReader import XMLReader

class Html:
    FROM_HTML_MODE_COMPACT: ClassVar[int]
    FROM_HTML_MODE_LEGACY: ClassVar[int]
    FROM_HTML_OPTION_USE_CSS_COLORS: ClassVar[int]
    FROM_HTML_SEPARATOR_LINE_BREAK_BLOCKQUOTE: ClassVar[int]
    FROM_HTML_SEPARATOR_LINE_BREAK_DIV: ClassVar[int]
    FROM_HTML_SEPARATOR_LINE_BREAK_HEADING: ClassVar[int]
    FROM_HTML_SEPARATOR_LINE_BREAK_LIST: ClassVar[int]
    FROM_HTML_SEPARATOR_LINE_BREAK_LIST_ITEM: ClassVar[int]
    FROM_HTML_SEPARATOR_LINE_BREAK_PARAGRAPH: ClassVar[int]
    TO_HTML_PARAGRAPH_LINES_CONSECUTIVE: ClassVar[int]
    TO_HTML_PARAGRAPH_LINES_INDIVIDUAL: ClassVar[int]
    @overload
    @staticmethod
    def fromHtml(arg0: str) -> Spanned: ...
    @overload
    @staticmethod
    def fromHtml(arg0: str, arg1: int) -> Spanned: ...
    @overload
    @staticmethod
    def fromHtml(arg0: str, arg1: "ImageGetter", arg2: "TagHandler") -> Spanned: ...
    @overload
    @staticmethod
    def fromHtml(arg0: str, arg1: int, arg2: "ImageGetter", arg3: "TagHandler") -> Spanned: ...
    @overload
    @staticmethod
    def toHtml(arg0: Spanned) -> str: ...
    @overload
    @staticmethod
    def toHtml(arg0: Spanned, arg1: int) -> str: ...
    @staticmethod
    def escapeHtml(arg0: str) -> str: ...

    class ImageGetter:
        def getDrawable(self, arg0: str) -> Drawable: ...

    class TagHandler:
        def handleTag(self, arg0: bool, arg1: str, arg2: Editable, arg3: XMLReader) -> None: ...
