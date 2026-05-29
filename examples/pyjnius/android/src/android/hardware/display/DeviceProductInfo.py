from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DeviceProductInfo"]

class DeviceProductInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/display/DeviceProductInfo"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;II)V", False)]
    CONNECTION_TO_SINK_BUILT_IN = JavaStaticField("I")
    CONNECTION_TO_SINK_DIRECT = JavaStaticField("I")
    CONNECTION_TO_SINK_TRANSITIVE = JavaStaticField("I")
    CONNECTION_TO_SINK_UNKNOWN = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getManufactureYear = JavaMethod("()I")
    getManufactureWeek = JavaMethod("()I")
    getConnectionToSinkType = JavaMethod("()I")
    getManufacturerPnpId = JavaMethod("()Ljava/lang/String;")
    getModelYear = JavaMethod("()I")
    getName = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getProductId = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")