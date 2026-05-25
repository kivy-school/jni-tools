from typing import Any, ClassVar, overload
from javax.xml.validation.SchemaFactory import SchemaFactory

class SchemaFactoryLoader:
    def newFactory(self, p0: str) -> SchemaFactory: ...
