from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UsbManager"]

class UsbManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/usb/UsbManager"
    ACTION_USB_ACCESSORY_ATTACHED = JavaStaticField("Ljava/lang/String;")
    ACTION_USB_ACCESSORY_DETACHED = JavaStaticField("Ljava/lang/String;")
    ACTION_USB_DEVICE_ATTACHED = JavaStaticField("Ljava/lang/String;")
    ACTION_USB_DEVICE_DETACHED = JavaStaticField("Ljava/lang/String;")
    EXTRA_ACCESSORY = JavaStaticField("Ljava/lang/String;")
    EXTRA_DEVICE = JavaStaticField("Ljava/lang/String;")
    EXTRA_PERMISSION_GRANTED = JavaStaticField("Ljava/lang/String;")
    getDeviceList = JavaMethod("()Ljava/util/HashMap;")
    getAccessoryList = JavaMethod("()[Landroid/hardware/usb/UsbAccessory;")
    hasPermission = JavaMultipleMethod([("(Landroid/hardware/usb/UsbDevice;)Z", False, False), ("(Landroid/hardware/usb/UsbAccessory;)Z", False, False)])
    openAccessory = JavaMethod("(Landroid/hardware/usb/UsbAccessory;)Landroid/os/ParcelFileDescriptor;")
    openAccessoryInputStream = JavaMethod("(Landroid/hardware/usb/UsbAccessory;)Ljava/io/InputStream;")
    openAccessoryOutputStream = JavaMethod("(Landroid/hardware/usb/UsbAccessory;)Ljava/io/OutputStream;")
    openDevice = JavaMethod("(Landroid/hardware/usb/UsbDevice;)Landroid/hardware/usb/UsbDeviceConnection;")
    requestPermission = JavaMultipleMethod([("(Landroid/hardware/usb/UsbAccessory;Landroid/app/PendingIntent;)V", False, False), ("(Landroid/hardware/usb/UsbDevice;Landroid/app/PendingIntent;)V", False, False)])