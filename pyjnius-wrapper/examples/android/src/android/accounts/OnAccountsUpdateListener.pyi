from typing import Any, ClassVar, overload
from android.accounts.Account import Account

class OnAccountsUpdateListener:
    def onAccountsUpdated(self, arg0: list[Account]) -> None: ...
