from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdvertiseData"]

class AdvertiseData(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/bluetooth/le/AdvertiseData"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getServiceUuids = JavaMethod("()Ljava/util/List;")
    getServiceSolicitationUuids = JavaMethod("()Ljava/util/List;")
    getTransportDiscoveryData = JavaMethod("()Ljava/util/List;")
    getManufacturerSpecificData = JavaMethod("()Landroid/util/SparseArray;")
    getServiceData = JavaMethod("()Ljava/util/Map;")
    getIncludeTxPowerLevel = JavaMethod("()Z")
    getIncludeDeviceName = JavaMethod("()Z")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/bluetooth/le/AdvertiseData/Builder"
        __javaconstructor__ = [("()V", False)]
        addServiceUuid = JavaMethod("(Landroid/os/ParcelUuid;)Landroid/bluetooth/le/AdvertiseData$Builder;")
        addServiceSolicitationUuid = JavaMethod("(Landroid/os/ParcelUuid;)Landroid/bluetooth/le/AdvertiseData$Builder;")
        addServiceData = JavaMethod("(Landroid/os/ParcelUuid;[B)Landroid/bluetooth/le/AdvertiseData$Builder;")
        addTransportDiscoveryData = JavaMethod("(Landroid/bluetooth/le/TransportDiscoveryData;)Landroid/bluetooth/le/AdvertiseData$Builder;")
        addManufacturerData = JavaMethod("(I[B)Landroid/bluetooth/le/AdvertiseData$Builder;")
        setIncludeTxPowerLevel = JavaMethod("(Z)Landroid/bluetooth/le/AdvertiseData$Builder;")
        setIncludeDeviceName = JavaMethod("(Z)Landroid/bluetooth/le/AdvertiseData$Builder;")
        build = JavaMethod("()Landroid/bluetooth/le/AdvertiseData;")