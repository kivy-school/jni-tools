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
    def openDevice(self, arg0: UsbDevice) -> UsbDeviceConnection: ...
    def getAccessoryList(self) -> list[UsbAccessory]: ...
    def openAccessory(self, arg0: UsbAccessory) -> ParcelFileDescriptor: ...
    @overload
    def hasPermission(self, arg0: UsbDevice) -> bool: ...
    @overload
    def hasPermission(self, arg0: UsbAccessory) -> bool: ...
    @overload
    def requestPermission(self, arg0: UsbDevice, arg1: PendingIntent) -> None: ...
    @overload
    def requestPermission(self, arg0: UsbAccessory, arg1: PendingIntent) -> None: ...
