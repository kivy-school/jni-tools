from typing import Any, ClassVar, overload
from java.net.ContentHandler import ContentHandler

class ContentHandlerFactory:
    def createContentHandler(self, arg0: str) -> ContentHandler: ...
