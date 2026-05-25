from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CarrierIdentifier"]

class CarrierIdentifier(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/carrier/CarrierIdentifier"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;II)V", False), ("([BLjava/lang/String;Ljava/lang/String;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getMcc = JavaMethod("()Ljava/lang/String;")
    getMnc = JavaMethod("()Ljava/lang/String;")
    getSpn = JavaMethod("()Ljava/lang/String;")
    getImsi = JavaMethod("()Ljava/lang/String;")
    getGid1 = JavaMethod("()Ljava/lang/String;")
    getGid2 = JavaMethod("()Ljava/lang/String;")
    getCarrierId = JavaMethod("()I")
    getSpecificCarrierId = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    toString = JavaMethod("()Ljava/lang/String;")