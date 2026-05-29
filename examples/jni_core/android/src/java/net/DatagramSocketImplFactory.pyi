from typing import Any, ClassVar, overload
from java.net.DatagramSocketImpl import DatagramSocketImpl

class DatagramSocketImplFactory:
    def createDatagramSocketImpl(self) -> DatagramSocketImpl: ...
