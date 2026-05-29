from typing import Any, ClassVar, overload
from android.accounts.AccountManagerFuture import AccountManagerFuture

class AccountManagerCallback:
    def run(self, arg0: AccountManagerFuture) -> None: ...
