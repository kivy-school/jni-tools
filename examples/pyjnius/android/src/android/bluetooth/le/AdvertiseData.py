from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdvertiseData"]

class AdvertiseData(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/bluetooth/le/AdvertiseData"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getIncludeTxPowerLevel = JavaMethod("()Z")
    getIncludeDeviceName = JavaMethod("()Z")
    getManufacturerSpecificData = JavaMethod("()Landroid/util/SparseArray;")
    getServiceSolicitationUuids = JavaMethod("()Ljava/util/List;")
    getTransportDiscoveryData = JavaMethod("()Ljava/util/List;")
    getServiceUuids = JavaMethod("()Ljava/util/List;")
    getServiceData = JavaMethod("()Ljava/util/Map;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/bluetooth/le/AdvertiseData$Builder"
        __javaconstructor__ = [("()V", False)]
        addServiceData = JavaMethod("(Landroid/os/ParcelUuid;[B)Landroid/bluetooth/le/AdvertiseData$Builder;")
        addManufacturerData = JavaMethod("(I[B)Landroid/bluetooth/le/AdvertiseData$Builder;")
        addServiceSolicitationUuid = JavaMethod("(Landroid/os/ParcelUuid;)Landroid/bluetooth/le/AdvertiseData$Builder;")
        addTransportDiscoveryData = JavaMethod("(Landroid/bluetooth/le/TransportDiscoveryData;)Landroid/bluetooth/le/AdvertiseData$Builder;")
        setIncludeDeviceName = JavaMethod("(Z)Landroid/bluetooth/le/AdvertiseData$Builder;")
        setIncludeTxPowerLevel = JavaMethod("(Z)Landroid/bluetooth/le/AdvertiseData$Builder;")
        addServiceUuid = JavaMethod("(Landroid/os/ParcelUuid;)Landroid/bluetooth/le/AdvertiseData$Builder;")
        build = JavaMethod("()Landroid/bluetooth/le/AdvertiseData;")