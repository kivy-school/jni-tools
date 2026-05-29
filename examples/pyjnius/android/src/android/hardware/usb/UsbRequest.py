from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UsbRequest"]

class UsbRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/usb/UsbRequest"
    __javaconstructor__ = [("()V", False)]
    getClientData = JavaMethod("()Ljava/lang/Object;")
    setClientData = JavaMethod("(Ljava/lang/Object;)V")
    getEndpoint = JavaMethod("()Landroid/hardware/usb/UsbEndpoint;")
    initialize = JavaMethod("(Landroid/hardware/usb/UsbDeviceConnection;Landroid/hardware/usb/UsbEndpoint;)Z")
    close = JavaMethod("()V")
    queue = JavaMultipleMethod([("(Ljava/nio/ByteBuffer;I)Z", False, False), ("(Ljava/nio/ByteBuffer;)Z", False, False)])
    cancel = JavaMethod("()Z")