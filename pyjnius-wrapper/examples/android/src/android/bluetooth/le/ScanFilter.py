from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ScanFilter"]

class ScanFilter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/bluetooth/le/ScanFilter"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getDeviceName = JavaMethod("()Ljava/lang/String;")
    getServiceUuid = JavaMethod("()Landroid/os/ParcelUuid;")
    getServiceUuidMask = JavaMethod("()Landroid/os/ParcelUuid;")
    getServiceSolicitationUuid = JavaMethod("()Landroid/os/ParcelUuid;")
    getServiceSolicitationUuidMask = JavaMethod("()Landroid/os/ParcelUuid;")
    getDeviceAddress = JavaMethod("()Ljava/lang/String;")
    getServiceData = JavaMethod("()[B")
    getServiceDataMask = JavaMethod("()[B")
    getServiceDataUuid = JavaMethod("()Landroid/os/ParcelUuid;")
    getManufacturerId = JavaMethod("()I")
    getManufacturerData = JavaMethod("()[B")
    getManufacturerDataMask = JavaMethod("()[B")
    getAdvertisingDataType = JavaMethod("()I")
    getAdvertisingData = JavaMethod("()[B")
    getAdvertisingDataMask = JavaMethod("()[B")
    matches = JavaMethod("(Landroid/bluetooth/le/ScanResult;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/bluetooth/le/ScanFilter/Builder"
        __javaconstructor__ = [("()V", False)]
        setDeviceName = JavaMethod("(Ljava/lang/String;)Landroid/bluetooth/le/ScanFilter$Builder;")
        setDeviceAddress = JavaMethod("(Ljava/lang/String;)Landroid/bluetooth/le/ScanFilter$Builder;")
        setServiceUuid = JavaMultipleMethod([("(Landroid/os/ParcelUuid;)Landroid/bluetooth/le/ScanFilter$Builder;", False, False), ("(Landroid/os/ParcelUuid;Landroid/os/ParcelUuid;)Landroid/bluetooth/le/ScanFilter$Builder;", False, False)])
        setServiceSolicitationUuid = JavaMultipleMethod([("(Landroid/os/ParcelUuid;)Landroid/bluetooth/le/ScanFilter$Builder;", False, False), ("(Landroid/os/ParcelUuid;Landroid/os/ParcelUuid;)Landroid/bluetooth/le/ScanFilter$Builder;", False, False)])
        setServiceData = JavaMultipleMethod([("(Landroid/os/ParcelUuid;[B)Landroid/bluetooth/le/ScanFilter$Builder;", False, False), ("(Landroid/os/ParcelUuid;[B[B)Landroid/bluetooth/le/ScanFilter$Builder;", False, False)])
        setManufacturerData = JavaMultipleMethod([("(I[B)Landroid/bluetooth/le/ScanFilter$Builder;", False, False), ("(I[B[B)Landroid/bluetooth/le/ScanFilter$Builder;", False, False)])
        setAdvertisingDataTypeWithData = JavaMethod("(I[B[B)Landroid/bluetooth/le/ScanFilter$Builder;")
        setAdvertisingDataType = JavaMethod("(I)Landroid/bluetooth/le/ScanFilter$Builder;")
        build = JavaMethod("()Landroid/bluetooth/le/ScanFilter;")