from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NetworkScanRequest"]

class NetworkScanRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/NetworkScanRequest"
    __javaconstructor__ = [("(I[Landroid/telephony/RadioAccessSpecifier;IIZILjava/util/ArrayList;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    SCAN_TYPE_ONE_SHOT = JavaStaticField("I")
    SCAN_TYPE_PERIODIC = JavaStaticField("I")
    getScanType = JavaMethod("()I")
    getSearchPeriodicity = JavaMethod("()I")
    getMaxSearchTime = JavaMethod("()I")
    getIncrementalResults = JavaMethod("()Z")
    getIncrementalResultsPeriodicity = JavaMethod("()I")
    getSpecifiers = JavaMethod("()[Landroid/telephony/RadioAccessSpecifier;")
    getPlmns = JavaMethod("()Ljava/util/ArrayList;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")