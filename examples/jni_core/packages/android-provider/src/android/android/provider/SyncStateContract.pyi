from typing import Any, ClassVar, overload
from android.accounts.Account import Account
from android.content.ContentProviderClient import ContentProviderClient
from android.content.ContentProviderOperation import ContentProviderOperation
from android.net.Uri import Uri
from android.util.Pair import Pair

class SyncStateContract:
    def __init__(self) -> None: ...

    class Helpers:
        def __init__(self) -> None: ...
        @staticmethod
        def newUpdateOperation(p0: Uri, p1: Any) -> ContentProviderOperation: ...
        @staticmethod
        def getWithUri(p0: ContentProviderClient, p1: Uri, p2: Account) -> Pair: ...
        @staticmethod
        def newSetOperation(p0: Uri, p1: Account, p2: Any) -> ContentProviderOperation: ...
        @staticmethod
        def get(p0: ContentProviderClient, p1: Uri, p2: Account) -> Any: ...
        @staticmethod
        def update(p0: ContentProviderClient, p1: Uri, p2: Any) -> None: ...
        @staticmethod
        def insert(p0: ContentProviderClient, p1: Uri, p2: Account, p3: Any) -> Uri: ...
        @staticmethod
        def set(p0: ContentProviderClient, p1: Uri, p2: Account, p3: Any) -> None: ...

    class Constants:
        CONTENT_DIRECTORY: ClassVar[str]
        ACCOUNT_NAME: ClassVar[str]
        ACCOUNT_TYPE: ClassVar[str]
        DATA: ClassVar[str]
        _COUNT: ClassVar[str]
        _ID: ClassVar[str]
        def __init__(self) -> None: ...

    class Columns:
        ACCOUNT_NAME: ClassVar[str]
        ACCOUNT_TYPE: ClassVar[str]
        DATA: ClassVar[str]
        _COUNT: ClassVar[str]
        _ID: ClassVar[str]
