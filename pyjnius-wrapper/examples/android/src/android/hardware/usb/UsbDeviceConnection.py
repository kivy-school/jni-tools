from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UsbDeviceConnection"]

class UsbDeviceConnection(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/usb/UsbDeviceConnection"
    close = JavaMethod("()V")
    getFileDescriptor = JavaMethod("()I")
    getRawDescriptors = JavaMethod("()[B")
    claimInterface = JavaMethod("(Landroid/hardware/usb/UsbInterface;Z)Z")
    releaseInterface = JavaMethod("(Landroid/hardware/usb/UsbInterface;)Z")
    setInterface = JavaMethod("(Landroid/hardware/usb/UsbInterface;)Z")
    setConfiguration = JavaMethod("(Landroid/hardware/usb/UsbConfiguration;)Z")
    controlTransfer = JavaMultipleMethod([("(IIII[BII)I", False, False), ("(IIII[BIII)I", False, False)])
    bulkTransfer = JavaMultipleMethod([("(Landroid/hardware/usb/UsbEndpoint;[BII)I", False, False), ("(Landroid/hardware/usb/UsbEndpoint;[BIII)I", False, False)])
    requestWait = JavaMultipleMethod([("()Landroid/hardware/usb/UsbRequest;", False, False), ("(J)Landroid/hardware/usb/UsbRequest;", False, False)])
    getSerial = JavaMethod("()Ljava/lang/String;")
    finalize = JavaMethod("()V")