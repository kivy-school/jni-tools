from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.gms.ads.OnAdInspectorClosedListener import OnAdInspectorClosedListener
from android.gms.ads.RequestConfiguration import RequestConfiguration
from android.gms.ads.VersionInfo import VersionInfo
from android.gms.ads.initialization.InitializationStatus import InitializationStatus
from android.gms.ads.initialization.OnInitializationCompleteListener import OnInitializationCompleteListener
from android.gms.ads.preload.PreloadCallback import PreloadCallback
from android.webkit.WebView import WebView

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class CustomTabsClient:
    """Forward declaration for ``androidx.browser.customtabs.CustomTabsClient``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('androidx.browser.customtabs.CustomTabsClient')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/androidx/browser/customtabs/CustomTabsClient
    """
    ...
class CustomTabsCallback:
    """Forward declaration for ``androidx.browser.customtabs.CustomTabsCallback``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('androidx.browser.customtabs.CustomTabsCallback')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/androidx/browser/customtabs/CustomTabsCallback
    """
    ...
class CustomTabsSession:
    """Forward declaration for ``androidx.browser.customtabs.CustomTabsSession``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('androidx.browser.customtabs.CustomTabsSession')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/androidx/browser/customtabs/CustomTabsSession
    """
    ...

class MobileAds:
    ERROR_DOMAIN: ClassVar[str]
    @overload
    @staticmethod
    def initialize(arg0: Context) -> None: ...
    @overload
    @staticmethod
    def initialize(arg0: Context, arg1: OnInitializationCompleteListener) -> None: ...
    @staticmethod
    def setAppVolume(arg0: float) -> None: ...
    @staticmethod
    def setAppMuted(arg0: bool) -> None: ...
    @staticmethod
    def openDebugMenu(arg0: Context, arg1: str) -> None: ...
    @staticmethod
    def registerRtbAdapter(arg0: type) -> None: ...
    @staticmethod
    def getInitializationStatus() -> InitializationStatus: ...
    @staticmethod
    def getRequestConfiguration() -> RequestConfiguration: ...
    @staticmethod
    def setRequestConfiguration(arg0: RequestConfiguration) -> None: ...
    @staticmethod
    def disableMediationAdapterInitialization(arg0: Context) -> None: ...
    @staticmethod
    def openAdInspector(arg0: Context, arg1: OnAdInspectorClosedListener) -> None: ...
    @staticmethod
    def getVersion() -> VersionInfo: ...
    @staticmethod
    def registerWebView(arg0: WebView) -> None: ...
    @staticmethod
    def putPublisherFirstPartyIdEnabled(arg0: bool) -> bool: ...
    @staticmethod
    def registerCustomTabsSession(arg0: Context, arg1: CustomTabsClient, arg2: str, arg3: CustomTabsCallback) -> CustomTabsSession: ...
    @staticmethod
    def startPreload(arg0: Context, arg1: list, arg2: PreloadCallback) -> None: ...
