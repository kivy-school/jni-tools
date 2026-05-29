from typing import Any, ClassVar, overload
from android.service.quickaccesswallet.GetWalletCardsError import GetWalletCardsError
from android.service.quickaccesswallet.GetWalletCardsResponse import GetWalletCardsResponse

class GetWalletCardsCallback:
    def onFailure(self, p0: GetWalletCardsError) -> None: ...
    def onSuccess(self, p0: GetWalletCardsResponse) -> None: ...
