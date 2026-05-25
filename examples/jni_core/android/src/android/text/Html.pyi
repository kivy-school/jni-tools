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
    def toHtml(p0: Spanned, p1: int) -> str: ...
    @overload
    @staticmethod
    def toHtml(p0: Spanned) -> str: ...
    @overload
    @staticmethod
    def fromHtml(p0: str, p1: int, p2: Any, p3: Any) -> Spanned: ...
    @overload
    @staticmethod
    def fromHtml(p0: str, p1: Any, p2: Any) -> Spanned: ...
    @overload
    @staticmethod
    def fromHtml(p0: str, p1: int) -> Spanned: ...
    @overload
    @staticmethod
    def fromHtml(p0: str) -> Spanned: ...
    @staticmethod
    def escapeHtml(p0: str) -> str: ...

    class TagHandler:
        def handleTag(self, p0: bool, p1: str, p2: Editable, p3: XMLReader) -> None: ...

    class ImageGetter:
        def getDrawable(self, p0: str) -> Drawable: ...
