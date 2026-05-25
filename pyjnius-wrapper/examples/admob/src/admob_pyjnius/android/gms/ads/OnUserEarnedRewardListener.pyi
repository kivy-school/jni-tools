from typing import Any, ClassVar, overload
from android.gms.ads.rewarded.RewardItem import RewardItem

class OnUserEarnedRewardListener:
    def onUserEarnedReward(self, arg0: RewardItem) -> None: ...
