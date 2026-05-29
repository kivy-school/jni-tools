from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SignalStrength"]

class SignalStrength(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/SignalStrength"
    __javaconstructor__ = [("(Landroid/telephony/SignalStrength;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    INVALID = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getCdmaDbm = JavaMethod("()I")
    getCdmaEcio = JavaMethod("()I")
    getCellSignalStrengths = JavaMultipleMethod([("(Ljava/lang/Class;)Ljava/util/List;", False, False), ("()Ljava/util/List;", False, False)])
    getEvdoDbm = JavaMethod("()I")
    getEvdoEcio = JavaMethod("()I")
    getEvdoSnr = JavaMethod("()I")
    getGsmBitErrorRate = JavaMethod("()I")
    getGsmSignalStrength = JavaMethod("()I")
    isGsm = JavaMethod("()Z")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getTimestampMillis = JavaMethod("()J")
    getLevel = JavaMethod("()I")