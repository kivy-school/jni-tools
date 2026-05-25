from typing import Any, ClassVar, overload
from android.content.Intent import Intent
from android.os.CancellationSignal import CancellationSignal
from android.os.IBinder import IBinder
from android.os.OutcomeReceiver import OutcomeReceiver
from android.service.credentials.BeginCreateCredentialRequest import BeginCreateCredentialRequest
from android.service.credentials.BeginGetCredentialRequest import BeginGetCredentialRequest
from android.service.credentials.ClearCredentialStateRequest import ClearCredentialStateRequest

class CredentialProviderService:
    EXTRA_BEGIN_GET_CREDENTIAL_REQUEST: ClassVar[str]
    EXTRA_BEGIN_GET_CREDENTIAL_RESPONSE: ClassVar[str]
    EXTRA_CREATE_CREDENTIAL_EXCEPTION: ClassVar[str]
    EXTRA_CREATE_CREDENTIAL_REQUEST: ClassVar[str]
    EXTRA_CREATE_CREDENTIAL_RESPONSE: ClassVar[str]
    EXTRA_GET_CREDENTIAL_EXCEPTION: ClassVar[str]
    EXTRA_GET_CREDENTIAL_REQUEST: ClassVar[str]
    EXTRA_GET_CREDENTIAL_RESPONSE: ClassVar[str]
    SERVICE_INTERFACE: ClassVar[str]
    SERVICE_META_DATA: ClassVar[str]
    def __init__(self) -> None: ...
    def onCreate(self) -> None: ...
    def onBind(self, arg0: Intent) -> IBinder: ...
    def onBeginGetCredential(self, arg0: BeginGetCredentialRequest, arg1: CancellationSignal, arg2: OutcomeReceiver) -> None: ...
    def onBeginCreateCredential(self, arg0: BeginCreateCredentialRequest, arg1: CancellationSignal, arg2: OutcomeReceiver) -> None: ...
    def onClearCredentialState(self, arg0: ClearCredentialStateRequest, arg1: CancellationSignal, arg2: OutcomeReceiver) -> None: ...
