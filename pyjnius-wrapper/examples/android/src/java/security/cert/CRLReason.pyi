from typing import Any, ClassVar, overload

class CRLReason:
    UNSPECIFIED: ClassVar["CRLReason"]
    KEY_COMPROMISE: ClassVar["CRLReason"]
    CA_COMPROMISE: ClassVar["CRLReason"]
    AFFILIATION_CHANGED: ClassVar["CRLReason"]
    SUPERSEDED: ClassVar["CRLReason"]
    CESSATION_OF_OPERATION: ClassVar["CRLReason"]
    CERTIFICATE_HOLD: ClassVar["CRLReason"]
    UNUSED: ClassVar["CRLReason"]
    REMOVE_FROM_CRL: ClassVar["CRLReason"]
    PRIVILEGE_WITHDRAWN: ClassVar["CRLReason"]
    AA_COMPROMISE: ClassVar["CRLReason"]
    @staticmethod
    def values() -> list["CRLReason"]: ...
    @staticmethod
    def valueOf(arg0: str) -> "CRLReason": ...
