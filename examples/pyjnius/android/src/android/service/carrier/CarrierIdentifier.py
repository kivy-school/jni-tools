from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CarrierIdentifier"]

class CarrierIdentifier(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/carrier/CarrierIdentifier"
    __javaconstructor__ = [("([BLjava/lang/String;Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;II)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getCarrierId = JavaMethod("()I")
    getGid1 = JavaMethod("()Ljava/lang/String;")
    getGid2 = JavaMethod("()Ljava/lang/String;")
    getImsi = JavaMethod("()Ljava/lang/String;")
    getMcc = JavaMethod("()Ljava/lang/String;")
    getMnc = JavaMethod("()Ljava/lang/String;")
    getSpecificCarrierId = JavaMethod("()I")
    getSpn = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")