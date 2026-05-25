from typing import Any, ClassVar, overload
from android.content.ComponentName import ComponentName
from android.content.Context import Context
from android.credentials.ClearCredentialStateRequest import ClearCredentialStateRequest
from android.credentials.CreateCredentialRequest import CreateCredentialRequest
from android.credentials.GetCredentialRequest import GetCredentialRequest
from android.credentials.RegisterCredentialDescriptionRequest import RegisterCredentialDescriptionRequest
from android.credentials.UnregisterCredentialDescriptionRequest import UnregisterCredentialDescriptionRequest
from android.os.CancellationSignal import CancellationSignal
from android.os.OutcomeReceiver import OutcomeReceiver
from java.util.concurrent.Executor import Executor

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class PendingGetCredentialHandle:
    """Forward declaration for ``android.credentials.PrepareGetCredentialResponse.PendingGetCredentialHandle``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.credentials.PrepareGetCredentialResponse.PendingGetCredentialHandle')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/credentials/PrepareGetCredentialResponse/PendingGetCredentialHandle
    """
    ...

class CredentialManager:
    @overload
    def getCredential(self, arg0: Context, arg1: GetCredentialRequest, arg2: CancellationSignal, arg3: Executor, arg4: OutcomeReceiver) -> None: ...
    @overload
    def getCredential(self, arg0: Context, arg1: PendingGetCredentialHandle, arg2: CancellationSignal, arg3: Executor, arg4: OutcomeReceiver) -> None: ...
    def prepareGetCredential(self, arg0: GetCredentialRequest, arg1: CancellationSignal, arg2: Executor, arg3: OutcomeReceiver) -> None: ...
    def createCredential(self, arg0: Context, arg1: CreateCredentialRequest, arg2: CancellationSignal, arg3: Executor, arg4: OutcomeReceiver) -> None: ...
    def clearCredentialState(self, arg0: ClearCredentialStateRequest, arg1: CancellationSignal, arg2: Executor, arg3: OutcomeReceiver) -> None: ...
    def isEnabledCredentialProviderService(self, arg0: ComponentName) -> bool: ...
    def registerCredentialDescription(self, arg0: RegisterCredentialDescriptionRequest) -> None: ...
    def unregisterCredentialDescription(self, arg0: UnregisterCredentialDescriptionRequest) -> None: ...
