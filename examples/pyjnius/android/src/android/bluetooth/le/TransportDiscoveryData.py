from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TransportDiscoveryData"]

class TransportDiscoveryData(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/bluetooth/le/TransportDiscoveryData"
    __javaconstructor__ = [("([B)V", False), ("(ILjava/util/List;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    totalBytes = JavaMethod("()I")
    getTransportDataType = JavaMethod("()I")
    getTransportBlocks = JavaMethod("()Ljava/util/List;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    toByteArray = JavaMethod("()[B")