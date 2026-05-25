from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BrailleDisplayController"]

class BrailleDisplayController(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/accessibilityservice/BrailleDisplayController"
    connect = JavaMultipleMethod([("(Landroid/bluetooth/BluetoothDevice;Landroid/accessibilityservice/BrailleDisplayController$BrailleDisplayCallback;)V", False, False), ("(Landroid/bluetooth/BluetoothDevice;Ljava/util/concurrent/Executor;Landroid/accessibilityservice/BrailleDisplayController$BrailleDisplayCallback;)V", False, False), ("(Landroid/hardware/usb/UsbDevice;Landroid/accessibilityservice/BrailleDisplayController$BrailleDisplayCallback;)V", False, False), ("(Landroid/hardware/usb/UsbDevice;Ljava/util/concurrent/Executor;Landroid/accessibilityservice/BrailleDisplayController$BrailleDisplayCallback;)V", False, False)])
    isConnected = JavaMethod("()Z")
    write = JavaMethod("([B)V")
    disconnect = JavaMethod("()V")

    class BrailleDisplayCallback(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/accessibilityservice/BrailleDisplayController/BrailleDisplayCallback"
        FLAG_ERROR_BRAILLE_DISPLAY_NOT_FOUND = JavaStaticField("I")
        FLAG_ERROR_CANNOT_ACCESS = JavaStaticField("I")
        onConnected = JavaMethod("([B)V")
        onConnectionFailed = JavaMethod("(I)V")
        onInput = JavaMethod("([B)V")
        onDisconnected = JavaMethod("()V")