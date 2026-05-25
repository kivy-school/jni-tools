from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.graphics.Rect import Rect
from android.print.PrintAttributes import PrintAttributes

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Page:
    """Forward declaration for ``android.graphics.pdf.PdfDocument.Page``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.graphics.pdf.PdfDocument.Page')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/graphics/pdf/PdfDocument/Page
    """
    ...

class PrintedPdfDocument:
    def __init__(self, arg0: Context, arg1: PrintAttributes) -> None: ...
    def startPage(self, arg0: int) -> Page: ...
    def getPageWidth(self) -> int: ...
    def getPageHeight(self) -> int: ...
    def getPageContentRect(self) -> Rect: ...
