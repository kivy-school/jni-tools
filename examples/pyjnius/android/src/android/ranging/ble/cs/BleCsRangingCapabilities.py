from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BleCsRangingCapabilities"]

class BleCsRangingCapabilities(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/ranging/ble/cs/BleCsRangingCapabilities"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CS_SECURITY_LEVEL_FOUR = JavaStaticField("I")
    CS_SECURITY_LEVEL_ONE = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    getSupportedSecurityLevels = JavaMethod("()Ljava/util/Set;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")