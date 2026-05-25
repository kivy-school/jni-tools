from typing import Any, ClassVar, overload
from android.os.ParcelFileDescriptor import ParcelFileDescriptor
from android.print.PrintDocumentInfo import PrintDocumentInfo

class PrintDocument:
    def getInfo(self) -> PrintDocumentInfo: ...
    def getData(self) -> ParcelFileDescriptor: ...
