from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.gms.ads.AdSize import AdSize

class MediationUtils:
    def __init__(self) -> None: ...
    @staticmethod
    def findClosestSize(arg0: Context, arg1: AdSize, arg2: list) -> AdSize: ...
