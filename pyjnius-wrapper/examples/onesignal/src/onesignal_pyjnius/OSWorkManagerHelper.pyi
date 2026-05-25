from typing import Any, ClassVar, overload
from android.content.Context import Context

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class WorkManager:
    """Forward declaration for ``androidx.work.WorkManager``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('androidx.work.WorkManager')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/androidx/work/WorkManager
    """
    ...

class OSWorkManagerHelper:
    INSTANCE: ClassVar["OSWorkManagerHelper"]
    @staticmethod
    def getInstance(arg0: Context) -> WorkManager: ...
