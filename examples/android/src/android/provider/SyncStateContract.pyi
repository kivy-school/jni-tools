from typing import Any, ClassVar, overload
from android.accounts.Account import Account
from android.content.ContentProviderClient import ContentProviderClient
from android.content.ContentProviderOperation import ContentProviderOperation
from android.net.Uri import Uri
from android.util.Pair import Pair

class SyncStateContract:
    def __init__(self) -> None: ...

    class Columns:
        ACCOUNT_NAME: ClassVar[str]
        ACCOUNT_TYPE: ClassVar[str]
        DATA: ClassVar[str]

    class Constants:
        CONTENT_DIRECTORY: ClassVar[str]
        def __init__(self) -> None: ...

    class Helpers:
        def __init__(self) -> None: ...
        @staticmethod
        def get(arg0: ContentProviderClient, arg1: Uri, arg2: Account) -> list[int]: ...
        @staticmethod
        def set(arg0: ContentProviderClient, arg1: Uri, arg2: Account, arg3: list[int]) -> None: ...
        @staticmethod
        def insert(arg0: ContentProviderClient, arg1: Uri, arg2: Account, arg3: list[int]) -> Uri: ...
        @staticmethod
        def update(arg0: ContentProviderClient, arg1: Uri, arg2: list[int]) -> None: ...
        @staticmethod
        def getWithUri(arg0: ContentProviderClient, arg1: Uri, arg2: Account) -> Pair: ...
        @staticmethod
        def newSetOperation(arg0: Uri, arg1: Account, arg2: list[int]) -> ContentProviderOperation: ...
        @staticmethod
        def newUpdateOperation(arg0: Uri, arg1: list[int]) -> ContentProviderOperation: ...
