from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CellInfoTdscdma"]

class CellInfoTdscdma(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/CellInfoTdscdma"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    CONNECTION_NONE = JavaStaticField("I")
    CONNECTION_PRIMARY_SERVING = JavaStaticField("I")
    CONNECTION_SECONDARY_SERVING = JavaStaticField("I")
    CONNECTION_UNKNOWN = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    UNAVAILABLE = JavaStaticField("I")
    UNAVAILABLE_LONG = JavaStaticField("J")
    getCellIdentity = JavaMultipleMethod([("()Landroid/telephony/CellIdentityTdscdma;", False, False), ("()Landroid/telephony/CellIdentity;", False, False)])
    getCellSignalStrength = JavaMultipleMethod([("()Landroid/telephony/CellSignalStrengthTdscdma;", False, False), ("()Landroid/telephony/CellSignalStrength;", False, False)])
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")