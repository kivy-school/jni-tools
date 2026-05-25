from typing import Any, ClassVar, overload
from android.app.Activity import Activity
from android.content.Context import Context
from android.content.Intent import Intent
from android.net.Uri import Uri
from android.security.AppUriAuthenticationPolicy import AppUriAuthenticationPolicy
from android.security.KeyChainAliasCallback import KeyChainAliasCallback
from java.security.Principal import Principal
from java.security.PrivateKey import PrivateKey
from java.security.cert.X509Certificate import X509Certificate

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
    @staticmethod
    def createInstallIntent() -> Intent: ...
    @staticmethod
    def createManageCredentialsIntent(arg0: AppUriAuthenticationPolicy) -> Intent: ...
    @overload
    @staticmethod
    def choosePrivateKeyAlias(arg0: Activity, arg1: KeyChainAliasCallback, arg2: list[str], arg3: list[Principal], arg4: str, arg5: int, arg6: str) -> None: ...
    @overload
    @staticmethod
    def choosePrivateKeyAlias(arg0: Activity, arg1: KeyChainAliasCallback, arg2: list[str], arg3: list[Principal], arg4: Uri, arg5: str) -> None: ...
    @staticmethod
    def isCredentialManagementApp(arg0: Context) -> bool: ...
    @staticmethod
    def getCredentialManagementAppPolicy(arg0: Context) -> AppUriAuthenticationPolicy: ...
    @staticmethod
    def removeCredentialManagementApp(arg0: Context) -> bool: ...
    @staticmethod
    def getPrivateKey(arg0: Context, arg1: str) -> PrivateKey: ...
    @staticmethod
    def getCertificateChain(arg0: Context, arg1: str) -> list[X509Certificate]: ...
    @staticmethod
    def isKeyAlgorithmSupported(arg0: str) -> bool: ...
    @staticmethod
    def isBoundKeyAlgorithm(arg0: str) -> bool: ...
