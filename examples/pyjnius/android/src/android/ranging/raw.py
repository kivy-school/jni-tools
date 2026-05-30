from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class RawInitiatorRangingConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/ranging/raw/RawInitiatorRangingConfig"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    RANGING_SESSION_OOB = JavaStaticField("I")
    RANGING_SESSION_RAW = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    getRawRangingDevices = JavaMethod("()Ljava/util/List;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/ranging/raw/RawInitiatorRangingConfig$Builder"
        __javaconstructor__ = [("()V", False)]
        addRawRangingDevice = JavaMethod("(Landroid/ranging/raw/RawRangingDevice;)Landroid/ranging/raw/RawInitiatorRangingConfig$Builder;")
        addRawRangingDevices = JavaMethod("(Ljava/util/List;)Landroid/ranging/raw/RawInitiatorRangingConfig$Builder;")
        build = JavaMethod("()Landroid/ranging/raw/RawInitiatorRangingConfig;")

class RawRangingDevice(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/ranging/raw/RawRangingDevice"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    UPDATE_RATE_FREQUENT = JavaStaticField("I")
    UPDATE_RATE_INFREQUENT = JavaStaticField("I")
    UPDATE_RATE_NORMAL = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getRangingDevice = JavaMethod("()Landroid/ranging/RangingDevice;")
    toString = JavaMethod("()Ljava/lang/String;")
    getBleRssiRangingParams = JavaMethod("()Landroid/ranging/ble/rssi/BleRssiRangingParams;")
    getCsRangingParams = JavaMethod("()Landroid/ranging/ble/cs/BleCsRangingParams;")
    getRttRangingParams = JavaMethod("()Landroid/ranging/wifi/rtt/RttRangingParams;")
    getUwbRangingParams = JavaMethod("()Landroid/ranging/uwb/UwbRangingParams;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/ranging/raw/RawRangingDevice$Builder"
        __javaconstructor__ = [("()V", False)]
        setBleRssiRangingParams = JavaMethod("(Landroid/ranging/ble/rssi/BleRssiRangingParams;)Landroid/ranging/raw/RawRangingDevice$Builder;")
        setCsRangingParams = JavaMethod("(Landroid/ranging/ble/cs/BleCsRangingParams;)Landroid/ranging/raw/RawRangingDevice$Builder;")
        setRangingDevice = JavaMethod("(Landroid/ranging/RangingDevice;)Landroid/ranging/raw/RawRangingDevice$Builder;")
        setRttRangingParams = JavaMethod("(Landroid/ranging/wifi/rtt/RttRangingParams;)Landroid/ranging/raw/RawRangingDevice$Builder;")
        setUwbRangingParams = JavaMethod("(Landroid/ranging/uwb/UwbRangingParams;)Landroid/ranging/raw/RawRangingDevice$Builder;")
        build = JavaMethod("()Landroid/ranging/raw/RawRangingDevice;")

class RawResponderRangingConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/ranging/raw/RawResponderRangingConfig"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    RANGING_SESSION_OOB = JavaStaticField("I")
    RANGING_SESSION_RAW = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    getRawRangingDevice = JavaMethod("()Landroid/ranging/raw/RawRangingDevice;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/ranging/raw/RawResponderRangingConfig$Builder"
        __javaconstructor__ = [("()V", False)]
        setRawRangingDevice = JavaMethod("(Landroid/ranging/raw/RawRangingDevice;)Landroid/ranging/raw/RawResponderRangingConfig$Builder;")
        build = JavaMethod("()Landroid/ranging/raw/RawResponderRangingConfig;")