from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NetworkScanRequest"]

class NetworkScanRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/NetworkScanRequest"
    __javaconstructor__ = [("(I[Landroid/telephony/RadioAccessSpecifier;IIZILjava/util/ArrayList;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    SCAN_TYPE_ONE_SHOT = JavaStaticField("I")
    SCAN_TYPE_PERIODIC = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getIncrementalResults = JavaMethod("()Z")
    getIncrementalResultsPeriodicity = JavaMethod("()I")
    getMaxSearchTime = JavaMethod("()I")
    getPlmns = JavaMethod("()Ljava/util/ArrayList;")
    getScanType = JavaMethod("()I")
    getSearchPeriodicity = JavaMethod("()I")
    getSpecifiers = JavaMethod("()[Landroid/telephony/RadioAccessSpecifier;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")