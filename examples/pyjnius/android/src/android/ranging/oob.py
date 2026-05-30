from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class TransportHandle(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/ranging/oob/TransportHandle"
    sendData = JavaMethod("([B)V")
    registerReceiveCallback = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/ranging/oob/TransportHandle$ReceiveCallback;)V")

    class ReceiveCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/ranging/oob/TransportHandle$ReceiveCallback"
        onClose = JavaMethod("()V")
        onDisconnect = JavaMethod("()V")
        onReceiveData = JavaMethod("([B)V")
        onReconnect = JavaMethod("()V")
        onSendFailed = JavaMethod("()V")

class OobInitiatorRangingConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/ranging/oob/OobInitiatorRangingConfig"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    RANGING_MODE_AUTO = JavaStaticField("I")
    RANGING_MODE_FUSED = JavaStaticField("I")
    RANGING_MODE_HIGH_ACCURACY = JavaStaticField("I")
    RANGING_MODE_HIGH_ACCURACY_PREFERRED = JavaStaticField("I")
    SECURITY_LEVEL_BASIC = JavaStaticField("I")
    SECURITY_LEVEL_SECURE = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    RANGING_SESSION_OOB = JavaStaticField("I")
    RANGING_SESSION_RAW = JavaStaticField("I")
    getSecurityLevel = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    getDeviceHandles = JavaMethod("()Ljava/util/List;")
    getFastestRangingInterval = JavaMethod("()Ljava/time/Duration;")
    getRangingIntervalRange = JavaMethod("()Landroid/util/Range;")
    getRangingMode = JavaMethod("()I")
    getSlowestRangingInterval = JavaMethod("()Ljava/time/Duration;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/ranging/oob/OobInitiatorRangingConfig$Builder"
        __javaconstructor__ = [("()V", False)]
        setSecurityLevel = JavaMethod("(I)Landroid/ranging/oob/OobInitiatorRangingConfig$Builder;")
        setFastestRangingInterval = JavaMethod("(Ljava/time/Duration;)Landroid/ranging/oob/OobInitiatorRangingConfig$Builder;")
        addDeviceHandle = JavaMethod("(Landroid/ranging/oob/DeviceHandle;)Landroid/ranging/oob/OobInitiatorRangingConfig$Builder;")
        setRangingMode = JavaMethod("(I)Landroid/ranging/oob/OobInitiatorRangingConfig$Builder;")
        addDeviceHandles = JavaMethod("(Ljava/util/List;)Landroid/ranging/oob/OobInitiatorRangingConfig$Builder;")
        setSlowestRangingInterval = JavaMethod("(Ljava/time/Duration;)Landroid/ranging/oob/OobInitiatorRangingConfig$Builder;")
        build = JavaMethod("()Landroid/ranging/oob/OobInitiatorRangingConfig;")

class DeviceHandle(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/ranging/oob/DeviceHandle"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getTransportHandle = JavaMethod("()Landroid/ranging/oob/TransportHandle;")
    getRangingDevice = JavaMethod("()Landroid/ranging/RangingDevice;")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/ranging/oob/DeviceHandle$Builder"
        __javaconstructor__ = [("(Landroid/ranging/RangingDevice;Landroid/ranging/oob/TransportHandle;)V", False)]
        build = JavaMethod("()Landroid/ranging/oob/DeviceHandle;")

class OobResponderRangingConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/ranging/oob/OobResponderRangingConfig"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    RANGING_SESSION_OOB = JavaStaticField("I")
    RANGING_SESSION_RAW = JavaStaticField("I")
    getDeviceHandle = JavaMethod("()Landroid/ranging/oob/DeviceHandle;")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/ranging/oob/OobResponderRangingConfig$Builder"
        __javaconstructor__ = [("(Landroid/ranging/oob/DeviceHandle;)V", False)]
        build = JavaMethod("()Landroid/ranging/oob/OobResponderRangingConfig;")