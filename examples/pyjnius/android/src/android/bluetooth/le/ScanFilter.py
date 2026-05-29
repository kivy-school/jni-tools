from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ScanFilter"]

class ScanFilter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/bluetooth/le/ScanFilter"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getServiceUuidMask = JavaMethod("()Landroid/os/ParcelUuid;")
    getServiceData = JavaMethod("()[B")
    getServiceDataUuid = JavaMethod("()Landroid/os/ParcelUuid;")
    getServiceDataMask = JavaMethod("()[B")
    getManufacturerId = JavaMethod("()I")
    getServiceUuid = JavaMethod("()Landroid/os/ParcelUuid;")
    getAdvertisingData = JavaMethod("()[B")
    getAdvertisingDataMask = JavaMethod("()[B")
    getAdvertisingDataType = JavaMethod("()I")
    getManufacturerData = JavaMethod("()[B")
    getManufacturerDataMask = JavaMethod("()[B")
    getServiceSolicitationUuid = JavaMethod("()Landroid/os/ParcelUuid;")
    getServiceSolicitationUuidMask = JavaMethod("()Landroid/os/ParcelUuid;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    matches = JavaMethod("(Landroid/bluetooth/le/ScanResult;)Z")
    getDeviceName = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getDeviceAddress = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/bluetooth/le/ScanFilter$Builder"
        __javaconstructor__ = [("()V", False)]
        build = JavaMethod("()Landroid/bluetooth/le/ScanFilter;")
        setServiceUuid = JavaMultipleMethod([("(Landroid/os/ParcelUuid;Landroid/os/ParcelUuid;)Landroid/bluetooth/le/ScanFilter$Builder;", False, False), ("(Landroid/os/ParcelUuid;)Landroid/bluetooth/le/ScanFilter$Builder;", False, False)])
        setDeviceAddress = JavaMethod("(Ljava/lang/String;)Landroid/bluetooth/le/ScanFilter$Builder;")
        setServiceData = JavaMultipleMethod([("(Landroid/os/ParcelUuid;[B[B)Landroid/bluetooth/le/ScanFilter$Builder;", False, False), ("(Landroid/os/ParcelUuid;[B)Landroid/bluetooth/le/ScanFilter$Builder;", False, False)])
        setDeviceName = JavaMethod("(Ljava/lang/String;)Landroid/bluetooth/le/ScanFilter$Builder;")
        setAdvertisingDataType = JavaMethod("(I)Landroid/bluetooth/le/ScanFilter$Builder;")
        setAdvertisingDataTypeWithData = JavaMethod("(I[B[B)Landroid/bluetooth/le/ScanFilter$Builder;")
        setManufacturerData = JavaMultipleMethod([("(I[B[B)Landroid/bluetooth/le/ScanFilter$Builder;", False, False), ("(I[B)Landroid/bluetooth/le/ScanFilter$Builder;", False, False)])
        setServiceSolicitationUuid = JavaMultipleMethod([("(Landroid/os/ParcelUuid;Landroid/os/ParcelUuid;)Landroid/bluetooth/le/ScanFilter$Builder;", False, False), ("(Landroid/os/ParcelUuid;)Landroid/bluetooth/le/ScanFilter$Builder;", False, False)])