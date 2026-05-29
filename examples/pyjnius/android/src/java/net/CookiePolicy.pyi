from typing import Any, ClassVar, overload
from java.net.HttpCookie import HttpCookie
from java.net.URI import URI

class CookiePolicy:
    ACCEPT_ALL: ClassVar["CookiePolicy"]
    ACCEPT_NONE: ClassVar["CookiePolicy"]
    ACCEPT_ORIGINAL_SERVER: ClassVar["CookiePolicy"]
    def shouldAccept(self, arg0: URI, arg1: HttpCookie) -> bool: ...
