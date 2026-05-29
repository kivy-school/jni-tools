from typing import Any, ClassVar, overload
from android.app.Activity import Activity
from android.content.Context import Context
from android.content.Intent import Intent
from android.net.Uri import Uri
from android.security.AppUriAuthenticationPolicy import AppUriAuthenticationPolicy
from android.security.KeyChainAliasCallback import KeyChainAliasCallback
from java.security.PrivateKey import PrivateKey

class KeyChain:
    ACTION_KEYCHAIN_CHANGED: ClassVar[str]
    ACTION_KEY_ACCESS_CHANGED: ClassVar[str]
    ACTION_STORAGE_CHANGED: ClassVar[str]
    ACTION_TRUST_STORE_CHANGED: ClassVar[str]
    EXTRA_CERTIFICATE: ClassVar[str]
    EXTRA_KEY_ACCESSIBLE: ClassVar[str]
    EXTRA_KEY_ALIAS: ClassVar[str]
    EXTRA_NAME: ClassVar[str]
    EXTRA_PKCS12: ClassVar[str]
    KEY_ALIAS_SELECTION_DENIED: ClassVar[str]
    def __init__(self) -> None: ...
    @overload
    @staticmethod
    def choosePrivateKeyAlias(p0: Activity, p1: KeyChainAliasCallback, p2: Any, p3: Any, p4: str, p5: int, p6: str) -> None: ...
    @overload
    @staticmethod
    def choosePrivateKeyAlias(p0: Activity, p1: KeyChainAliasCallback, p2: Any, p3: Any, p4: Uri, p5: str) -> None: ...
    @staticmethod
    def createInstallIntent() -> Intent: ...
    @staticmethod
    def createManageCredentialsIntent(p0: AppUriAuthenticationPolicy) -> Intent: ...
    @staticmethod
    def getCredentialManagementAppPolicy(p0: Context) -> AppUriAuthenticationPolicy: ...
    @staticmethod
    def getPrivateKey(p0: Context, p1: str) -> PrivateKey: ...
    @staticmethod
    def isBoundKeyAlgorithm(p0: str) -> bool: ...
    @staticmethod
    def isCredentialManagementApp(p0: Context) -> bool: ...
    @staticmethod
    def isKeyAlgorithmSupported(p0: str) -> bool: ...
    @staticmethod
    def removeCredentialManagementApp(p0: Context) -> bool: ...
    @staticmethod
    def getCertificateChain(p0: Context, p1: str) -> Any: ...
