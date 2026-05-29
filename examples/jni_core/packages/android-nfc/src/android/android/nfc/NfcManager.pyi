from typing import Any, ClassVar, overload
from android.nfc.NfcAdapter import NfcAdapter

class NfcManager:
    def getDefaultAdapter(self) -> NfcAdapter: ...
