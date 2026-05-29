from typing import Any, ClassVar, overload
from android.app.appsearch.GenericDocument import GenericDocument

class DocumentIdUtil:
    @overload
    @staticmethod
    def createQualifiedId(arg0: str, arg1: str, arg2: GenericDocument) -> str: ...
    @overload
    @staticmethod
    def createQualifiedId(arg0: str, arg1: str, arg2: str, arg3: str) -> str: ...
