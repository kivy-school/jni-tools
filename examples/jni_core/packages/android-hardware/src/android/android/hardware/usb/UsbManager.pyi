from typing import Any, ClassVar, overload
from android.app.PendingIntent import PendingIntent
from android.hardware.usb.UsbAccessory import UsbAccessory
from android.hardware.usb.UsbDevice import UsbDevice
from android.hardware.usb.UsbDeviceConnection import UsbDeviceConnection
from android.os.ParcelFileDescriptor import ParcelFileDescriptor

class UsbManager:
    ACTION_USB_ACCESSORY_ATTACHED: ClassVar[str]
    ACTION_USB_ACCESSORY_DETACHED: ClassVar[str]
    ACTION_USB_DEVICE_ATTACHED: ClassVar[str]
    ACTION_USB_DEVICE_DETACHED: ClassVar[str]
    EXTRA_ACCESSORY: ClassVar[str]
    EXTRA_DEVICE: ClassVar[str]
    EXTRA_PERMISSION_GRANTED: ClassVar[str]
    def getDeviceList(self) -> dict: ...
    def openDevice(self, p0: UsbDevice) -> UsbDeviceConnection: ...
    def getAccessoryList(self) -> Any: ...
    def openAccessory(self, p0: UsbAccessory) -> ParcelFileDescriptor: ...
    @overload
    def hasPermission(self, p0: UsbAccessory) -> bool: ...
    @overload
    def hasPermission(self, p0: UsbDevice) -> bool: ...
    @overload
    def requestPermission(self, p0: UsbDevice, p1: PendingIntent) -> None: ...
    @overload
    def requestPermission(self, p0: UsbAccessory, p1: PendingIntent) -> None: ...
