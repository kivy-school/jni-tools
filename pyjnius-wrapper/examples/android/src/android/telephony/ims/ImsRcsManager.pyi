from typing import Any, ClassVar, overload
from android.telephony.ims.ImsStateCallback import ImsStateCallback
from android.telephony.ims.RcsUceAdapter import RcsUceAdapter
from java.util.concurrent.Executor import Executor
from java.util.function.Consumer import Consumer

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class RegistrationCallback:
    """Forward declaration for ``android.telephony.ims.RegistrationManager.RegistrationCallback``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.telephony.ims.RegistrationManager.RegistrationCallback')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/telephony/ims/RegistrationManager/RegistrationCallback
    """
    ...

class ImsRcsManager:
    ACTION_SHOW_CAPABILITY_DISCOVERY_OPT_IN: ClassVar[str]
    CAPABILITY_TYPE_NONE: ClassVar[int]
    CAPABILITY_TYPE_OPTIONS_UCE: ClassVar[int]
    CAPABILITY_TYPE_PRESENCE_UCE: ClassVar[int]
    def getUceAdapter(self) -> RcsUceAdapter: ...
    def registerImsRegistrationCallback(self, arg0: Executor, arg1: RegistrationCallback) -> None: ...
    def unregisterImsRegistrationCallback(self, arg0: RegistrationCallback) -> None: ...
    def getRegistrationState(self, arg0: Executor, arg1: Consumer) -> None: ...
    def getRegistrationTransportType(self, arg0: Executor, arg1: Consumer) -> None: ...
    def registerImsStateCallback(self, arg0: Executor, arg1: ImsStateCallback) -> None: ...
    def unregisterImsStateCallback(self, arg0: ImsStateCallback) -> None: ...
