from typing import Any, ClassVar, overload
from android.content.ComponentName import ComponentName
from android.print.PrintAttributes import PrintAttributes
from android.print.PrintDocumentAdapter import PrintDocumentAdapter
from android.print.PrintJob import PrintJob

class PrintManager:
    def isPrintServiceEnabled(self, p0: ComponentName) -> bool: ...
    def getPrintJobs(self) -> list: ...
    def print(self, p0: str, p1: PrintDocumentAdapter, p2: PrintAttributes) -> PrintJob: ...
