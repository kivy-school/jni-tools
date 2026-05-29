from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MtpDevice"]

class MtpDevice(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/mtp/MtpDevice"
    __javaconstructor__ = [("(Landroid/hardware/usb/UsbDevice;)V", False)]
    open = JavaMethod("(Landroid/hardware/usb/UsbDeviceConnection;)Z")
    close = JavaMethod("()V")
    finalize = JavaMethod("()V")
    getDeviceName = JavaMethod("()Ljava/lang/String;")
    getDeviceId = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    getDeviceInfo = JavaMethod("()Landroid/mtp/MtpDeviceInfo;")
    getStorageIds = JavaMethod("()[I")
    getObjectHandles = JavaMethod("(III)[I")
    getObject = JavaMethod("(II)[B")
    getPartialObject = JavaMethod("(IJJ[B)J")
    getPartialObject64 = JavaMethod("(IJJ[B)J")
    getThumbnail = JavaMethod("(I)[B")
    getStorageInfo = JavaMethod("(I)Landroid/mtp/MtpStorageInfo;")
    getObjectInfo = JavaMethod("(I)Landroid/mtp/MtpObjectInfo;")
    deleteObject = JavaMethod("(I)Z")
    getParent = JavaMethod("(I)J")
    getStorageId = JavaMethod("(I)J")
    importFile = JavaMultipleMethod([("(ILjava/lang/String;)Z", False, False), ("(ILandroid/os/ParcelFileDescriptor;)Z", False, False)])
    sendObject = JavaMethod("(IJLandroid/os/ParcelFileDescriptor;)Z")
    sendObjectInfo = JavaMethod("(Landroid/mtp/MtpObjectInfo;)Landroid/mtp/MtpObjectInfo;")
    readEvent = JavaMethod("(Landroid/os/CancellationSignal;)Landroid/mtp/MtpEvent;")