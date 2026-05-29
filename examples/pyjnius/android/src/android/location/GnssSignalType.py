from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GnssSignalType"]

class GnssSignalType(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/location/GnssSignalType"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getCodeType = JavaMethod("()Ljava/lang/String;")
    getConstellationType = JavaMethod("()I")
    getCarrierFrequencyHz = JavaMethod("()D")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    create = JavaStaticMethod("(IDLjava/lang/String;)Landroid/location/GnssSignalType;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")