from typing import Any, ClassVar, overload
from OSLogger import OSLogger
from OSSharedPreferences import OSSharedPreferences
from OSTime import OSTime
from influence.data.OSChannelTracker import OSChannelTracker

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class InfluenceParams:
    """Forward declaration for ``com.onesignal.OneSignalRemoteParams.InfluenceParams``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.onesignal.OneSignalRemoteParams.InfluenceParams')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
    """
    ...
class JSONObject:
    """Forward declaration for ``org.json.JSONObject``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('org.json.JSONObject')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
    """
    ...
class AppEntryAction:
    """Forward declaration for ``com.onesignal.OneSignal.AppEntryAction``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.onesignal.OneSignal.AppEntryAction')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
    """
    ...

class OSTrackerFactory:
    def __init__(self, arg0: OSSharedPreferences, arg1: OSLogger, arg2: OSTime) -> None: ...
    def getInfluences(self) -> list: ...
    def getSessionInfluences(self) -> list: ...
    def getIAMChannelTracker(self) -> OSChannelTracker: ...
    def getNotificationChannelTracker(self) -> OSChannelTracker: ...
    def getChannels(self) -> list: ...
    def initFromCache(self) -> None: ...
    def saveInfluenceParams(self, arg0: InfluenceParams) -> None: ...
    def addSessionData(self, arg0: JSONObject, arg1: list) -> None: ...
    def getChannelByEntryAction(self, arg0: AppEntryAction) -> OSChannelTracker: ...
    def getChannelsToResetByEntryAction(self, arg0: AppEntryAction) -> list: ...

    class WhenMappings:
        ...
