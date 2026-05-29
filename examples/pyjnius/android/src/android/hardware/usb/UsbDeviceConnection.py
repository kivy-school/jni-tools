from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UsbDeviceConnection"]

class UsbDeviceConnection(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/usb/UsbDeviceConnection"
    getSerial = JavaMethod("()Ljava/lang/String;")
    bulkTransfer = JavaMultipleMethod([("(Landroid/hardware/usb/UsbEndpoint;[BIII)I", False, False), ("(Landroid/hardware/usb/UsbEndpoint;[BII)I", False, False)])
    claimInterface = JavaMethod("(Landroid/hardware/usb/UsbInterface;Z)Z")
    controlTransfer = JavaMultipleMethod([("(IIII[BII)I", False, False), ("(IIII[BIII)I", False, False)])
    getRawDescriptors = JavaMethod("()[B")
    releaseInterface = JavaMethod("(Landroid/hardware/usb/UsbInterface;)Z")
    requestWait = JavaMultipleMethod([("(J)Landroid/hardware/usb/UsbRequest;", False, False), ("()Landroid/hardware/usb/UsbRequest;", False, False)])
    setConfiguration = JavaMethod("(Landroid/hardware/usb/UsbConfiguration;)Z")
    setInterface = JavaMethod("(Landroid/hardware/usb/UsbInterface;)Z")
    close = JavaMethod("()V")
    getFileDescriptor = JavaMethod("()I")