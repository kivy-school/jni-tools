from typing import Any, ClassVar, overload
from android.app.SearchableInfo import SearchableInfo
from android.content.ComponentName import ComponentName
from android.content.DialogInterface import DialogInterface
from android.os.Bundle import Bundle

class SearchManager:
    ACTION_KEY: ClassVar[str]
    ACTION_MSG: ClassVar[str]
    APP_DATA: ClassVar[str]
    CURSOR_EXTRA_KEY_IN_PROGRESS: ClassVar[str]
    EXTRA_DATA_KEY: ClassVar[str]
    EXTRA_NEW_SEARCH: ClassVar[str]
    EXTRA_SELECT_QUERY: ClassVar[str]
    EXTRA_WEB_SEARCH_PENDINGINTENT: ClassVar[str]
    FLAG_QUERY_REFINEMENT: ClassVar[int]
    INTENT_ACTION_GLOBAL_SEARCH: ClassVar[str]
    INTENT_ACTION_SEARCHABLES_CHANGED: ClassVar[str]
    INTENT_ACTION_SEARCH_SETTINGS: ClassVar[str]
    INTENT_ACTION_SEARCH_SETTINGS_CHANGED: ClassVar[str]
    INTENT_ACTION_WEB_SEARCH_SETTINGS: ClassVar[str]
    INTENT_GLOBAL_SEARCH_ACTIVITY_CHANGED: ClassVar[str]
    MENU_KEY: ClassVar[str]
    MENU_KEYCODE: ClassVar[int]
    QUERY: ClassVar[str]
    SHORTCUT_MIME_TYPE: ClassVar[str]
    SUGGEST_COLUMN_AUDIO_CHANNEL_CONFIG: ClassVar[str]
    SUGGEST_COLUMN_CONTENT_TYPE: ClassVar[str]
    SUGGEST_COLUMN_DURATION: ClassVar[str]
    SUGGEST_COLUMN_FLAGS: ClassVar[str]
    SUGGEST_COLUMN_FORMAT: ClassVar[str]
    SUGGEST_COLUMN_ICON_1: ClassVar[str]
    SUGGEST_COLUMN_ICON_2: ClassVar[str]
    SUGGEST_COLUMN_INTENT_ACTION: ClassVar[str]
    SUGGEST_COLUMN_INTENT_DATA: ClassVar[str]
    SUGGEST_COLUMN_INTENT_DATA_ID: ClassVar[str]
    SUGGEST_COLUMN_INTENT_EXTRA_DATA: ClassVar[str]
    SUGGEST_COLUMN_IS_LIVE: ClassVar[str]
    SUGGEST_COLUMN_LAST_ACCESS_HINT: ClassVar[str]
    SUGGEST_COLUMN_PRODUCTION_YEAR: ClassVar[str]
    SUGGEST_COLUMN_PURCHASE_PRICE: ClassVar[str]
    SUGGEST_COLUMN_QUERY: ClassVar[str]
    SUGGEST_COLUMN_RATING_SCORE: ClassVar[str]
    SUGGEST_COLUMN_RATING_STYLE: ClassVar[str]
    SUGGEST_COLUMN_RENTAL_PRICE: ClassVar[str]
    SUGGEST_COLUMN_RESULT_CARD_IMAGE: ClassVar[str]
    SUGGEST_COLUMN_SHORTCUT_ID: ClassVar[str]
    SUGGEST_COLUMN_SPINNER_WHILE_REFRESHING: ClassVar[str]
    SUGGEST_COLUMN_TEXT_1: ClassVar[str]
    SUGGEST_COLUMN_TEXT_2: ClassVar[str]
    SUGGEST_COLUMN_TEXT_2_URL: ClassVar[str]
    SUGGEST_COLUMN_VIDEO_HEIGHT: ClassVar[str]
    SUGGEST_COLUMN_VIDEO_WIDTH: ClassVar[str]
    SUGGEST_MIME_TYPE: ClassVar[str]
    SUGGEST_NEVER_MAKE_SHORTCUT: ClassVar[str]
    SUGGEST_PARAMETER_LIMIT: ClassVar[str]
    SUGGEST_URI_PATH_QUERY: ClassVar[str]
    SUGGEST_URI_PATH_SHORTCUT: ClassVar[str]
    USER_QUERY: ClassVar[str]
    def startSearch(self, p0: str, p1: bool, p2: ComponentName, p3: Bundle, p4: bool) -> None: ...
    def triggerSearch(self, p0: str, p1: ComponentName, p2: Bundle) -> None: ...
    def setOnCancelListener(self, p0: Any) -> None: ...
    def onCancel(self, p0: DialogInterface) -> None: ...
    def onDismiss(self, p0: DialogInterface) -> None: ...
    def setOnDismissListener(self, p0: Any) -> None: ...
    def getGlobalSearchActivity(self) -> ComponentName: ...
    def getSearchableInfo(self, p0: ComponentName) -> SearchableInfo: ...
    def getSearchablesInGlobalSearch(self) -> list: ...
    def stopSearch(self) -> None: ...

    class OnDismissListener:
        def onDismiss(self) -> None: ...

    class OnCancelListener:
        def onCancel(self) -> None: ...
