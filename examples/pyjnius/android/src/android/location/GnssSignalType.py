from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GnssSignalType"]

class GnssSignalType(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/location/GnssSignalType"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    create = JavaStaticMethod("(IDLjava/lang/String;)Landroid/location/GnssSignalType;")
    getConstellationType = JavaMethod("()I")
    getCarrierFrequencyHz = JavaMethod("()D")
    getCodeType = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")