from typing import Any, ClassVar, overload
from android.app.Activity import Activity
from android.app.PendingIntent import PendingIntent
from android.content.Context import Context
from android.content.IntentFilter import IntentFilter
from android.net.Uri import Uri
from android.nfc.NdefMessage import NdefMessage
from android.nfc.NfcAntennaInfo import NfcAntennaInfo
from android.nfc.NfcEvent import NfcEvent
from android.nfc.Tag import Tag
from android.os.Bundle import Bundle
from android.os.Handler import Handler

class NfcAdapter:
    ACTION_ADAPTER_STATE_CHANGED: ClassVar[str]
    ACTION_NDEF_DISCOVERED: ClassVar[str]
    ACTION_PREFERRED_PAYMENT_CHANGED: ClassVar[str]
    ACTION_TAG_DISCOVERED: ClassVar[str]
    ACTION_TECH_DISCOVERED: ClassVar[str]
    ACTION_TRANSACTION_DETECTED: ClassVar[str]
    EXTRA_ADAPTER_STATE: ClassVar[str]
    EXTRA_AID: ClassVar[str]
    EXTRA_DATA: ClassVar[str]
    EXTRA_ID: ClassVar[str]
    EXTRA_NDEF_MESSAGES: ClassVar[str]
    EXTRA_PREFERRED_PAYMENT_CHANGED_REASON: ClassVar[str]
    EXTRA_READER_PRESENCE_CHECK_DELAY: ClassVar[str]
    EXTRA_SECURE_ELEMENT_NAME: ClassVar[str]
    EXTRA_TAG: ClassVar[str]
    FLAG_LISTEN_DISABLE: ClassVar[int]
    FLAG_LISTEN_KEEP: ClassVar[int]
    FLAG_LISTEN_NFC_PASSIVE_A: ClassVar[int]
    FLAG_LISTEN_NFC_PASSIVE_B: ClassVar[int]
    FLAG_LISTEN_NFC_PASSIVE_F: ClassVar[int]
    FLAG_READER_DISABLE: ClassVar[int]
    FLAG_READER_KEEP: ClassVar[int]
    FLAG_READER_NFC_A: ClassVar[int]
    FLAG_READER_NFC_B: ClassVar[int]
    FLAG_READER_NFC_BARCODE: ClassVar[int]
    FLAG_READER_NFC_F: ClassVar[int]
    FLAG_READER_NFC_V: ClassVar[int]
    FLAG_READER_NO_PLATFORM_SOUNDS: ClassVar[int]
    FLAG_READER_SKIP_NDEF_CHECK: ClassVar[int]
    PREFERRED_PAYMENT_CHANGED: ClassVar[int]
    PREFERRED_PAYMENT_LOADED: ClassVar[int]
    PREFERRED_PAYMENT_UPDATED: ClassVar[int]
    STATE_OFF: ClassVar[int]
    STATE_ON: ClassVar[int]
    STATE_TURNING_OFF: ClassVar[int]
    STATE_TURNING_ON: ClassVar[int]
    @staticmethod
    def getDefaultAdapter(arg0: Context) -> "NfcAdapter": ...
    def isEnabled(self) -> bool: ...
    def isObserveModeSupported(self) -> bool: ...
    def isObserveModeEnabled(self) -> bool: ...
    def setObserveModeEnabled(self, arg0: bool) -> bool: ...
    def enableForegroundDispatch(self, arg0: Activity, arg1: PendingIntent, arg2: list[IntentFilter], arg3: list[list[str]]) -> None: ...
    def disableForegroundDispatch(self, arg0: Activity) -> None: ...
    def enableReaderMode(self, arg0: Activity, arg1: "ReaderCallback", arg2: int, arg3: Bundle) -> None: ...
    def disableReaderMode(self, arg0: Activity) -> None: ...
    def setDiscoveryTechnology(self, arg0: Activity, arg1: int, arg2: int) -> None: ...
    def resetDiscoveryTechnology(self, arg0: Activity) -> None: ...
    def isSecureNfcSupported(self) -> bool: ...
    def getNfcAntennaInfo(self) -> NfcAntennaInfo: ...
    def isSecureNfcEnabled(self) -> bool: ...
    def isReaderOptionSupported(self) -> bool: ...
    def isReaderOptionEnabled(self) -> bool: ...
    def ignore(self, arg0: Tag, arg1: int, arg2: "OnTagRemovedListener", arg3: Handler) -> bool: ...

    class CreateBeamUrisCallback:
        def createBeamUris(self, arg0: NfcEvent) -> list[Uri]: ...

    class CreateNdefMessageCallback:
        def createNdefMessage(self, arg0: NfcEvent) -> NdefMessage: ...

    class OnNdefPushCompleteCallback:
        def onNdefPushComplete(self, arg0: NfcEvent) -> None: ...

    class OnTagRemovedListener:
        def onTagRemoved(self) -> None: ...

    class ReaderCallback:
        def onTagDiscovered(self, arg0: Tag) -> None: ...
