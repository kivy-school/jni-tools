from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TransportBlock"]

class TransportBlock(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/bluetooth/le/TransportBlock"
    __javaconstructor__ = [("(III[B)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    totalBytes = JavaMethod("()I")
    getOrgId = JavaMethod("()I")
    getTdsFlags = JavaMethod("()I")
    getTransportData = JavaMethod("()[B")
    getTransportDataLength = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    toByteArray = JavaMethod("()[B")