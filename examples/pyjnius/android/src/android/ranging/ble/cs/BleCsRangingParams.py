from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BleCsRangingParams"]

class BleCsRangingParams(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/ranging/ble/cs/BleCsRangingParams"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    LOCATION_TYPE_INDOOR = JavaStaticField("I")
    LOCATION_TYPE_OUTDOOR = JavaStaticField("I")
    LOCATION_TYPE_UNKNOWN = JavaStaticField("I")
    SIGHT_TYPE_LINE_OF_SIGHT = JavaStaticField("I")
    SIGHT_TYPE_NON_LINE_OF_SIGHT = JavaStaticField("I")
    SIGHT_TYPE_UNKNOWN = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getLocationType = JavaMethod("()I")
    getSightType = JavaMethod("()I")
    getSecurityLevel = JavaMethod("()I")
    getPeerBluetoothAddress = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getRangingUpdateRate = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/ranging/ble/cs/BleCsRangingParams$Builder"
        __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
        setRangingUpdateRate = JavaMethod("(I)Landroid/ranging/ble/cs/BleCsRangingParams$Builder;")
        setSecurityLevel = JavaMethod("(I)Landroid/ranging/ble/cs/BleCsRangingParams$Builder;")
        setLocationType = JavaMethod("(I)Landroid/ranging/ble/cs/BleCsRangingParams$Builder;")
        setSightType = JavaMethod("(I)Landroid/ranging/ble/cs/BleCsRangingParams$Builder;")
        build = JavaMethod("()Landroid/ranging/ble/cs/BleCsRangingParams;")