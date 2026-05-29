from typing import Any, ClassVar, overload
from android.content.Context import Context

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class WorkerParameters:
    """Forward declaration for ``androidx.work.WorkerParameters``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('androidx.work.WorkerParameters')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/androidx/work/WorkerParameters
    """
    ...
class Result:
    """Forward declaration for ``androidx.work.ListenableWorker.Result``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('androidx.work.ListenableWorker.Result')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/androidx/work/ListenableWorker/Result
    """
    ...

class OfflinePingSender:
    def __init__(self, arg0: Context, arg1: WorkerParameters) -> None: ...
    def doWork(self) -> Result: ...
