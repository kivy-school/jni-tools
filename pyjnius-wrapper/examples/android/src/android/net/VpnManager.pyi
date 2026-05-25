from typing import Any, ClassVar, overload
from android.content.Intent import Intent
from android.net.PlatformVpnProfile import PlatformVpnProfile
from android.net.VpnProfileState import VpnProfileState

class VpnManager:
    ACTION_VPN_MANAGER_EVENT: ClassVar[str]
    CATEGORY_EVENT_ALWAYS_ON_STATE_CHANGED: ClassVar[str]
    CATEGORY_EVENT_DEACTIVATED_BY_USER: ClassVar[str]
    CATEGORY_EVENT_IKE_ERROR: ClassVar[str]
    CATEGORY_EVENT_NETWORK_ERROR: ClassVar[str]
    ERROR_CLASS_NOT_RECOVERABLE: ClassVar[int]
    ERROR_CLASS_RECOVERABLE: ClassVar[int]
    ERROR_CODE_NETWORK_IO: ClassVar[int]
    ERROR_CODE_NETWORK_LOST: ClassVar[int]
    ERROR_CODE_NETWORK_PROTOCOL_TIMEOUT: ClassVar[int]
    ERROR_CODE_NETWORK_UNKNOWN_HOST: ClassVar[int]
    EXTRA_ERROR_CLASS: ClassVar[str]
    EXTRA_ERROR_CODE: ClassVar[str]
    EXTRA_SESSION_KEY: ClassVar[str]
    EXTRA_TIMESTAMP_MILLIS: ClassVar[str]
    EXTRA_UNDERLYING_LINK_PROPERTIES: ClassVar[str]
    EXTRA_UNDERLYING_NETWORK: ClassVar[str]
    EXTRA_UNDERLYING_NETWORK_CAPABILITIES: ClassVar[str]
    EXTRA_VPN_PROFILE_STATE: ClassVar[str]
    def provisionVpnProfile(self, arg0: PlatformVpnProfile) -> Intent: ...
    def deleteProvisionedVpnProfile(self) -> None: ...
    def startProvisionedVpnProfileSession(self) -> str: ...
    def startProvisionedVpnProfile(self) -> None: ...
    def stopProvisionedVpnProfile(self) -> None: ...
    def getProvisionedVpnProfileState(self) -> VpnProfileState: ...
