from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DeviceProductInfo"]

class DeviceProductInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/display/DeviceProductInfo"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;II)V", False)]
    CONNECTION_TO_SINK_BUILT_IN = JavaStaticField("I")
    CONNECTION_TO_SINK_DIRECT = JavaStaticField("I")
    CONNECTION_TO_SINK_TRANSITIVE = JavaStaticField("I")
    CONNECTION_TO_SINK_UNKNOWN = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getName = JavaMethod("()Ljava/lang/String;")
    getManufacturerPnpId = JavaMethod("()Ljava/lang/String;")
    getProductId = JavaMethod("()Ljava/lang/String;")
    getModelYear = JavaMethod("()I")
    getManufactureYear = JavaMethod("()I")
    getManufactureWeek = JavaMethod("()I")
    getConnectionToSinkType = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")