from typing import Any, ClassVar, overload
from android.app.appsearch.observer.DocumentChangeInfo import DocumentChangeInfo
from android.app.appsearch.observer.SchemaChangeInfo import SchemaChangeInfo

class ObserverCallback:
    def onDocumentChanged(self, p0: DocumentChangeInfo) -> None: ...
    def onSchemaChanged(self, p0: SchemaChangeInfo) -> None: ...
