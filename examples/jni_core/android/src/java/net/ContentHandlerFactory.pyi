from typing import Any, ClassVar, overload
from java.net.ContentHandler import ContentHandler

class ContentHandlerFactory:
    def createContentHandler(self, p0: str) -> ContentHandler: ...
