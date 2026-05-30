from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class VirtualDeviceManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/companion/virtual/VirtualDeviceManager"
    getVirtualDevices = JavaMethod("()Ljava/util/List;")
    registerVirtualDeviceListener = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/companion/virtual/VirtualDeviceManager$VirtualDeviceListener;)V")
    getVirtualDevice = JavaMethod("(I)Landroid/companion/virtual/VirtualDevice;")
    unregisterVirtualDeviceListener = JavaMethod("(Landroid/companion/virtual/VirtualDeviceManager$VirtualDeviceListener;)V")

    class VirtualDeviceListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/companion/virtual/VirtualDeviceManager$VirtualDeviceListener"
        onVirtualDeviceClosed = JavaMethod("(I)V")
        onVirtualDeviceCreated = JavaMethod("(I)V")

class VirtualDevice(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/companion/virtual/VirtualDevice"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getDisplayIds = JavaMethod("()[I")
    getPersistentDeviceId = JavaMethod("()Ljava/lang/String;")
    hasCustomSensorSupport = JavaMethod("()Z")
    getName = JavaMethod("()Ljava/lang/String;")
    toString = JavaMethod("()Ljava/lang/String;")
    getDeviceId = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getDisplayName = JavaMethod("()Ljava/lang/CharSequence;")