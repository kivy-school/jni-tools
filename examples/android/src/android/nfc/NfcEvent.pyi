from typing import Any, ClassVar, overload
from android.nfc.NfcAdapter import NfcAdapter

class NfcEvent:
    nfcAdapter: NfcAdapter
    peerLlcpMajorVersion: int
    peerLlcpMinorVersion: int
