from typing import Any, ClassVar, overload
from android.os.Bundle import Bundle
from android.view.textservice.SpellCheckerInfo import SpellCheckerInfo
from android.view.textservice.SpellCheckerSession import SpellCheckerSession
from java.util.Locale import Locale
from java.util.concurrent.Executor import Executor

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class SpellCheckerSessionListener:
    """Forward declaration for ``android.view.textservice.SpellCheckerSession.SpellCheckerSessionListener``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.view.textservice.SpellCheckerSession.SpellCheckerSessionListener')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/view/textservice/SpellCheckerSession/SpellCheckerSessionListener
    """
    ...
class SpellCheckerSessionParams:
    """Forward declaration for ``android.view.textservice.SpellCheckerSession.SpellCheckerSessionParams``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.view.textservice.SpellCheckerSession.SpellCheckerSessionParams')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/view/textservice/SpellCheckerSession/SpellCheckerSessionParams
    """
    ...

class TextServicesManager:
    @overload
    def newSpellCheckerSession(self, arg0: Bundle, arg1: Locale, arg2: SpellCheckerSessionListener, arg3: bool) -> SpellCheckerSession: ...
    @overload
    def newSpellCheckerSession(self, arg0: SpellCheckerSessionParams, arg1: Executor, arg2: SpellCheckerSessionListener) -> SpellCheckerSession: ...
    def getEnabledSpellCheckerInfos(self) -> list: ...
    def getCurrentSpellCheckerInfo(self) -> SpellCheckerInfo: ...
    def isSpellCheckerEnabled(self) -> bool: ...
