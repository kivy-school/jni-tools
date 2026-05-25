from typing import Any, ClassVar, overload
from android.app.appsearch.observer.DocumentChangeInfo import DocumentChangeInfo
from android.app.appsearch.observer.SchemaChangeInfo import SchemaChangeInfo

class ObserverCallback:
    def onSchemaChanged(self, arg0: SchemaChangeInfo) -> None: ...
    def onDocumentChanged(self, arg0: DocumentChangeInfo) -> None: ...
