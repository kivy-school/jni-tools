from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TransportBlock"]

class TransportBlock(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/bluetooth/le/TransportBlock"
    __javaconstructor__ = [("(III[B)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getOrgId = JavaMethod("()I")
    getTdsFlags = JavaMethod("()I")
    getTransportDataLength = JavaMethod("()I")
    getTransportData = JavaMethod("()[B")
    toByteArray = JavaMethod("()[B")
    totalBytes = JavaMethod("()I")