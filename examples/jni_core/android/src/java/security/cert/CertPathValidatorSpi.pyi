from typing import Any, ClassVar, overload
from java.security.cert.CertPath import CertPath
from java.security.cert.CertPathChecker import CertPathChecker
from java.security.cert.CertPathParameters import CertPathParameters
from java.security.cert.CertPathValidatorResult import CertPathValidatorResult

class CertPathValidatorSpi:
    def __init__(self) -> None: ...
    def engineGetRevocationChecker(self) -> CertPathChecker: ...
    def engineValidate(self, p0: CertPath, p1: CertPathParameters) -> CertPathValidatorResult: ...
