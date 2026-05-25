from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VirtualDeviceManager"]

class VirtualDeviceManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/companion/virtual/VirtualDeviceManager"
    getVirtualDevices = JavaMethod("()Ljava/util/List;")
    getVirtualDevice = JavaMethod("(I)Landroid/companion/virtual/VirtualDevice;")
    registerVirtualDeviceListener = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/companion/virtual/VirtualDeviceManager$VirtualDeviceListener;)V")
    unregisterVirtualDeviceListener = JavaMethod("(Landroid/companion/virtual/VirtualDeviceManager$VirtualDeviceListener;)V")

    class VirtualDeviceListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/companion/virtual/VirtualDeviceManager/VirtualDeviceListener"
        onVirtualDeviceCreated = JavaMethod("(I)V")
        onVirtualDeviceClosed = JavaMethod("(I)V")