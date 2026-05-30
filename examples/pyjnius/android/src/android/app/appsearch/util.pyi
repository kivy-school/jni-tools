from typing import Any, ClassVar, overload
from android.app.appsearch.GenericDocument import GenericDocument

class DocumentIdUtil:
    @overload
    @staticmethod
    def createQualifiedId(p0: str, p1: str, p2: GenericDocument) -> str: ...
    @overload
    @staticmethod
    def createQualifiedId(p0: str, p1: str, p2: str, p3: str) -> str: ...

