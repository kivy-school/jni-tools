from typing import Any, ClassVar, overload
from android.service.quickaccesswallet.GetWalletCardsError import GetWalletCardsError
from android.service.quickaccesswallet.GetWalletCardsResponse import GetWalletCardsResponse

class GetWalletCardsCallback:
    def onSuccess(self, arg0: GetWalletCardsResponse) -> None: ...
    def onFailure(self, arg0: GetWalletCardsError) -> None: ...
