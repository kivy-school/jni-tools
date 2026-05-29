from typing import Any, ClassVar, overload
from android.content.Intent import Intent
from android.os.Bundle import Bundle
from android.os.PersistableBundle import PersistableBundle

class RestrictionsManager:
    ACTION_PERMISSION_RESPONSE_RECEIVED: ClassVar[str]
    ACTION_REQUEST_LOCAL_APPROVAL: ClassVar[str]
    ACTION_REQUEST_PERMISSION: ClassVar[str]
    EXTRA_PACKAGE_NAME: ClassVar[str]
    EXTRA_REQUEST_BUNDLE: ClassVar[str]
    EXTRA_REQUEST_ID: ClassVar[str]
    EXTRA_REQUEST_TYPE: ClassVar[str]
    EXTRA_RESPONSE_BUNDLE: ClassVar[str]
    META_DATA_APP_RESTRICTIONS: ClassVar[str]
    REQUEST_KEY_APPROVE_LABEL: ClassVar[str]
    REQUEST_KEY_DATA: ClassVar[str]
    REQUEST_KEY_DENY_LABEL: ClassVar[str]
    REQUEST_KEY_ICON: ClassVar[str]
    REQUEST_KEY_ID: ClassVar[str]
    REQUEST_KEY_MESSAGE: ClassVar[str]
    REQUEST_KEY_NEW_REQUEST: ClassVar[str]
    REQUEST_KEY_TITLE: ClassVar[str]
    REQUEST_TYPE_APPROVAL: ClassVar[str]
    RESPONSE_KEY_ERROR_CODE: ClassVar[str]
    RESPONSE_KEY_MESSAGE: ClassVar[str]
    RESPONSE_KEY_RESPONSE_TIMESTAMP: ClassVar[str]
    RESPONSE_KEY_RESULT: ClassVar[str]
    RESULT_APPROVED: ClassVar[int]
    RESULT_DENIED: ClassVar[int]
    RESULT_ERROR: ClassVar[int]
    RESULT_ERROR_BAD_REQUEST: ClassVar[int]
    RESULT_ERROR_INTERNAL: ClassVar[int]
    RESULT_ERROR_NETWORK: ClassVar[int]
    RESULT_NO_RESPONSE: ClassVar[int]
    RESULT_UNKNOWN_REQUEST: ClassVar[int]
    @staticmethod
    def convertRestrictionsToBundle(p0: list) -> Bundle: ...
    def createLocalApprovalIntent(self) -> Intent: ...
    def getApplicationRestrictions(self) -> Bundle: ...
    def getApplicationRestrictionsPerAdmin(self) -> list: ...
    def getManifestRestrictions(self, p0: str) -> list: ...
    def hasRestrictionsProvider(self) -> bool: ...
    def notifyPermissionResponse(self, p0: str, p1: PersistableBundle) -> None: ...
    def requestPermission(self, p0: str, p1: str, p2: PersistableBundle) -> None: ...
