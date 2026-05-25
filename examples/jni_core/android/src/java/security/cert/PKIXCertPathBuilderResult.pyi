from typing import Any, ClassVar, overload
from java.security.PublicKey import PublicKey
from java.security.cert.CertPath import CertPath
from java.security.cert.PolicyNode import PolicyNode
from java.security.cert.TrustAnchor import TrustAnchor

class PKIXCertPathBuilderResult:
    def __init__(self, p0: CertPath, p1: TrustAnchor, p2: PolicyNode, p3: PublicKey) -> None: ...
    def getCertPath(self) -> CertPath: ...
    def toString(self) -> str: ...
