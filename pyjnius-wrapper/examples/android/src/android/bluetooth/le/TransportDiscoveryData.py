from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TransportDiscoveryData"]

class TransportDiscoveryData(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/bluetooth/le/TransportDiscoveryData"
    __javaconstructor__ = [("(ILjava/util/List;)V", False), ("([B)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    describeContents = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getTransportDataType = JavaMethod("()I")
    getTransportBlocks = JavaMethod("()Ljava/util/List;")
    toByteArray = JavaMethod("()[B")
    toString = JavaMethod("()Ljava/lang/String;")
    totalBytes = JavaMethod("()I")