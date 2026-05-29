from typing import Any, ClassVar, overload
from android.telephony.ims.ImsMmTelManager import ImsMmTelManager
from android.telephony.ims.ImsRcsManager import ImsRcsManager
from android.telephony.ims.ProvisioningManager import ProvisioningManager

class ImsManager:
    ACTION_WFC_IMS_REGISTRATION_ERROR: ClassVar[str]
    EXTRA_WFC_REGISTRATION_FAILURE_MESSAGE: ClassVar[str]
    EXTRA_WFC_REGISTRATION_FAILURE_TITLE: ClassVar[str]
    def getImsMmTelManager(self, p0: int) -> ImsMmTelManager: ...
    def getImsRcsManager(self, p0: int) -> ImsRcsManager: ...
    def getProvisioningManager(self, p0: int) -> ProvisioningManager: ...
