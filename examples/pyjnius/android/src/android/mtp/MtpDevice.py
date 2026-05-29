from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MtpDevice"]

class MtpDevice(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/mtp/MtpDevice"
    __javaconstructor__ = [("(Landroid/hardware/usb/UsbDevice;)V", False)]
    getStorageInfo = JavaMethod("(I)Landroid/mtp/MtpStorageInfo;")
    sendObjectInfo = JavaMethod("(Landroid/mtp/MtpObjectInfo;)Landroid/mtp/MtpObjectInfo;")
    readEvent = JavaMethod("(Landroid/os/CancellationSignal;)Landroid/mtp/MtpEvent;")
    getStorageId = JavaMethod("(I)J")
    getPartialObject64 = JavaMethod("(IJJ[B)J")
    sendObject = JavaMethod("(IJLandroid/os/ParcelFileDescriptor;)Z")
    getPartialObject = JavaMethod("(IJJ[B)J")
    getObject = JavaMethod("(II)[B")
    getDeviceInfo = JavaMethod("()Landroid/mtp/MtpDeviceInfo;")
    getObjectHandles = JavaMethod("(III)[I")
    getObjectInfo = JavaMethod("(I)Landroid/mtp/MtpObjectInfo;")
    deleteObject = JavaMethod("(I)Z")
    importFile = JavaMultipleMethod([("(ILjava/lang/String;)Z", False, False), ("(ILandroid/os/ParcelFileDescriptor;)Z", False, False)])
    getStorageIds = JavaMethod("()[I")
    toString = JavaMethod("()Ljava/lang/String;")
    close = JavaMethod("()V")
    getParent = JavaMethod("(I)J")
    open = JavaMethod("(Landroid/hardware/usb/UsbDeviceConnection;)Z")
    getDeviceName = JavaMethod("()Ljava/lang/String;")
    getDeviceId = JavaMethod("()I")
    getThumbnail = JavaMethod("(I)[B")