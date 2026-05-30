from typing import Any, ClassVar, overload

class ServiceConnectionLeakedViolation:
    ...

from typing import Any, ClassVar, overload

class InstanceCountViolation:
    def getNumberOfInstances(self) -> int: ...

from typing import Any, ClassVar, overload
from java.lang.Throwable import Throwable

class Violation:
    def fillInStackTrace(self) -> Throwable: ...
    def initCause(self, p0: Throwable) -> Throwable: ...
    def hashCode(self) -> int: ...
    def setStackTrace(self, p0: Any) -> None: ...

from typing import Any, ClassVar, overload

class CleartextNetworkViolation:
    ...

from typing import Any, ClassVar, overload

class NetworkViolation:
    ...

from typing import Any, ClassVar, overload

class ResourceMismatchViolation:
    ...

from typing import Any, ClassVar, overload

class DiskReadViolation:
    ...

from typing import Any, ClassVar, overload

class UntaggedSocketViolation:
    ...

from typing import Any, ClassVar, overload

class IntentReceiverLeakedViolation:
    ...

from typing import Any, ClassVar, overload

class FileUriExposedViolation:
    ...

from typing import Any, ClassVar, overload

class ContentUriWithoutPermissionViolation:
    ...

from typing import Any, ClassVar, overload

class ExplicitGcViolation:
    ...

from typing import Any, ClassVar, overload

class SqliteObjectLeakedViolation:
    ...

from typing import Any, ClassVar, overload

class CustomViolation:
    ...

from typing import Any, ClassVar, overload

class DiskWriteViolation:
    ...

from typing import Any, ClassVar, overload

class ImplicitDirectBootViolation:
    ...

from typing import Any, ClassVar, overload

class NonSdkApiUsedViolation:
    ...

from typing import Any, ClassVar, overload
from java.lang.Throwable import Throwable

class IncorrectContextUseViolation:
    def __init__(self, p0: str, p1: Throwable) -> None: ...

from typing import Any, ClassVar, overload

class UnbufferedIoViolation:
    ...

from typing import Any, ClassVar, overload

class CredentialProtectedWhileLockedViolation:
    ...

from typing import Any, ClassVar, overload
from android.content.Intent import Intent

class UnsafeIntentLaunchViolation:
    def __init__(self, p0: Intent) -> None: ...
    def getIntent(self) -> Intent: ...

from typing import Any, ClassVar, overload

class LeakedClosableViolation:
    ...

from typing import Any, ClassVar, overload

class WebViewMethodCalledOnWrongThreadViolation:
    ...

