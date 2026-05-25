from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SignalStrength"]

class SignalStrength(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/SignalStrength"
    __javaconstructor__ = [("(Landroid/telephony/SignalStrength;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    INVALID = JavaStaticField("I")
    getCellSignalStrengths = JavaMultipleMethod([("()Ljava/util/List;", False, False), ("(Ljava/lang/Class;)Ljava/util/List;", False, False)])
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getTimestampMillis = JavaMethod("()J")
    describeContents = JavaMethod("()I")
    getGsmSignalStrength = JavaMethod("()I")
    getGsmBitErrorRate = JavaMethod("()I")
    getCdmaDbm = JavaMethod("()I")
    getCdmaEcio = JavaMethod("()I")
    getEvdoDbm = JavaMethod("()I")
    getEvdoEcio = JavaMethod("()I")
    getEvdoSnr = JavaMethod("()I")
    getLevel = JavaMethod("()I")
    isGsm = JavaMethod("()Z")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")