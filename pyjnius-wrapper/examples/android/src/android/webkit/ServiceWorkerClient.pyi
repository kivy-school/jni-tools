from typing import Any, ClassVar, overload
from android.webkit.WebResourceRequest import WebResourceRequest
from android.webkit.WebResourceResponse import WebResourceResponse

class ServiceWorkerClient:
    def __init__(self) -> None: ...
    def shouldInterceptRequest(self, arg0: WebResourceRequest) -> WebResourceResponse: ...
