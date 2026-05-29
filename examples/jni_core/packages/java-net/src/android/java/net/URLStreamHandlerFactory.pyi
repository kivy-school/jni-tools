from typing import Any, ClassVar, overload
from java.net.URLStreamHandler import URLStreamHandler

class URLStreamHandlerFactory:
    def createURLStreamHandler(self, p0: str) -> URLStreamHandler: ...
