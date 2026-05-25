from typing import Any, ClassVar, overload
from android.content.ComponentName import ComponentName
from android.print.PrintAttributes import PrintAttributes
from android.print.PrintDocumentAdapter import PrintDocumentAdapter
from android.print.PrintJob import PrintJob

class PrintManager:
    def getPrintJobs(self) -> list: ...
    def print(self, arg0: str, arg1: PrintDocumentAdapter, arg2: PrintAttributes) -> PrintJob: ...
    def isPrintServiceEnabled(self, arg0: ComponentName) -> bool: ...
